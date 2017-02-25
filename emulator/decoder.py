from .blowfish import blowfish
import base64
import struct
import json
import zlib
from . import settings
import sys

DECODE_PACK = '>l'
if sys.maxsize > 2**32:
	DECODE_PACK = '>L'

# D:\Users\unknown\Desktop\WiresharkPortable\App\Wireshark\tshark.exe -r J:\mgs\ssl\dump_with_a_key.cap.pcap -o ssl.keys_list:"0.0.0.0","443","http","D:\Users\unknown\Desktop\OZH.pem" -2  -Y "ip.addr == 210.149.133.135 and http" -T fields -e http.file_data > C:\testout.txt
# replace %2B with +
# remove ',' and line breaks

class Decoder(object):
	"""class for decoding messages sent from server to client"""
	def __init__(self, static_key=None, crypto_key=None):
		super(Decoder, self).__init__()
		self.__static_blowfish__ = blowfish()
		if not static_key:
			static_key = bytearray(open(settings.STATIC_KEY_FILE_PATH,'rb').read(16))
		self.__static_blowfish__.initialize(static_key)

		self.__session_blowfish__ = None
		self.__crypto_key__ = None
		if crypto_key:
			self.__crypto_key__ = crypto_key
			self.__init_session_blowfish__()

	def __get_crypto_key__(self, data):
		crypto_key = None
		if 'data' in data:
			if type(data['data']) == dict:
				if 'crypto_key' in data['data']:
					if len(data['data']['crypto_key']) > 0:
						crypto_key = bytearray(base64.decodestring(data['data']['crypto_key'].encode()))
						self.__crypto_key__ = crypto_key
		return crypto_key

	def __init_session_blowfish__(self):
		self.__session_blowfish__ = blowfish()
		self.__session_blowfish__.initialize(self.__crypto_key__)

	def __get_json__(self, text):
		text = text[:text.rfind('}')+1]
		text = text.replace('\\\\r\\\\n','')
		text = text.replace('\\r\\n','')
		text = text.replace('\\','')
		text = text.replace('"{','{')
		text = text.replace('}"','}')
		text = json.loads(text)
		return text

	def __decipher__(self, blow, data):
		offset = 0
		full_text = bytes()
		while offset!= len(data):
			chunk = data[offset:offset+8]
			x = struct.unpack(DECODE_PACK,chunk[0:4])[0]
			y = struct.unpack(DECODE_PACK, chunk[4:8])[0]
			x,y = blow.blowfish_decipher(x, y)

			x_text = struct.pack(DECODE_PACK,x)
			y_text = struct.pack(DECODE_PACK,y)
			
			full_text += x_text + y_text
			offset = offset+8
		return full_text

	def decode(self, data):
		# accepts base64-encoded strings from server
		# you need to remove all line breaks, commas and html-escapes before decoding
		encoded_text = None
		try:
			data_encoded = base64.decodestring(data.encode())
		except Exception as e:
			raise e
		else:
			data_decoded = self.__decipher__(self.__static_blowfish__, data_encoded)

		try:
			# json conversions can be wonky
			data_json = self.__get_json__(data_decoded.decode())
		except Exception as e:
			raise e

		if not self.__session_blowfish__:
			# there was no crypto_key set during class initialization
			self.__get_crypto_key__(data_json)
			if self.__crypto_key__:
				self.__init_session_blowfish__()

		if data_json['session_crypto']:
			if self.__session_blowfish__:
				# COMPOUND encryption with blowfish
				embedded = base64.decodestring(data_json['data'].encode())
				data_json['data'] = self.__decipher__(self.__session_blowfish__, embedded)
				if data_json['compress']:
					data_json['data'] = zlib.decompress(data_json['data'])
			else:
				# encryption is used, but we have no session key
				raise ValueError('Message is encoded, but no crypto_key was provided')
		else:
			# no encryption, used in CMD_GET_URLLIST and others before getting session key
			if data_json['compress']:
				data_json['data'] = zlib.decompress(base64.decodestring(data_json['data'].encode()))			

		if type(data_json['data']) == bytes:
			data_json['data'] = data_json['data'].decode()

		if 'original_size' in data_json and type(data_json['data']) == str:
			# remove padding and convert to json
			data_json['data'] = data_json['data'][:data_json['original_size']]
			try:
				j = json.loads(data_json['data'])
			except Exception as e:
				# not json, skipping
				pass
			else:
				data_json['data'] = j

		return data_json

# TODO: move to tests
# d = Decoder()
# text = "YnHdLj/1b4SBvSa1/0bYhcd4UAB70VUxUp9R+E7nlQqbd/CfasI2cHERrSHJdSMpyXeXDjDyVZA9ZW+a9XxS/njMyTWS86ztRmyJ6yr6RICSRqkSq/14sMwyaWtw5heV+Sz+EYH1y2pbbsdaoU5hYHVAPWVjLqPUc8dYBIG7yZXPEmu0H3/N2z6uhACqfTgyrJvd8dOR+t4ekBWWFsLFTzO4yUOlMIk4kV7NHmMm2QPwfUE8/YY05Pog0Cu6r6wGSIZJghUfd8Ko9jzdAqyHkq/07vhNMcet3RBbi7BJty7zbN01+7nuywzb3bZh3MnWjqhs3swuQUADCo4k4+0PrfmWJY5kTwNXGALVleozNL2CR0pLVHimlfKohUvBlLP6kOzrli7EIC5EBqPPUTTptMmfkE2PTm9wDf1Lk+MPib7YpYqgOsPbIjONlpiur+19VdzkXTpOJBir1mVkNGGxdgTntsNuRyLpE1VkE7ngGSnX6jNAs8vFF65LERPnvE6jnsAlzQt7YDRpzTvu0nOD4I5YAzAdBaJkaiPelF7/nmdTt5T1ic2LNbWcg37hPPar2PTXrReJtq6xwMvNY/IzZMamJefkWTTC"
# print(d.decode(text))
