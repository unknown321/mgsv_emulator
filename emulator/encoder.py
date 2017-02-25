# -*- coding: utf-8 -*-
from .blowfish import blowfish
import base64
import struct
import json
import zlib
import warnings
from . import settings
import sys

ENCODE_PACK = '>l'
if sys.maxsize > 2**32:
	ENCODE_PACK = '>L'

class Encoder(object):
	"""docstring for Encoder"""
	def __init__(self, static_key=None, crypto_key=None):
		super(Encoder, self).__init__()
		self.__static_blowfish__ = blowfish()
		if not static_key:
			static_key = bytearray(open(settings.STATIC_KEY_FILE_PATH,'rb').read(16))
		self.__static_blowfish__.initialize(static_key)

		self.__session_blowfish__ = None
		self.__crypto_key__ = None
		if crypto_key:
			self.__crypto_key__ = crypto_key
			self.__init_session_blowfish__()

	def __init_session_blowfish__(self, crypto_key=None):
		self.__session_blowfish__ = blowfish()
		if crypto_key:
			self.__crypto_key__ = crypto_key
		self.__session_blowfish__.initialize(self.__crypto_key__)

	def __encipher__(self, blow, data):
		offset = 0
		full_text = bytes()
		while offset!= len(data):
			chunk = data[offset:offset+8]
			x = struct.unpack('>l',chunk[0:4].encode())[0]
			y = struct.unpack('>l', chunk[4:8].encode())[0]
			x,y = blow.blowfish_encipher(x, y)

			x_text = struct.pack(ENCODE_PACK,x)
			y_text = struct.pack(ENCODE_PACK,y)
			
			full_text += x_text + y_text
			offset = offset+8
		return full_text

	def __add_padding__(self, text):
		if len(text)%8!=0:
			x = bytes([8-len(text)%8])*(8-len(text)%8)
			text = text + x.decode()
			# print("---",text)
		return text

	def __compress_data__(self, data):
		text = json.dumps(data, sort_keys=True)
		text = text.replace(' ','')
		return text

	def encode(self, _data):
		if type(_data) != dict:
			warnings.warn('You are using plain text, parameters might be not in the right order!', Warning, stacklevel=2)


		# encrypt everything inside command
		if (type(_data) == dict) and ('data' in _data):
			# 
			_data['original_size'] = len( self.__compress_data__(_data['data']) )
			# _data['data'] =  json.dumps(_data['data'], sort_keys=True)
			_data['data'] = self.__compress_data__(_data['data'])
			

			if _data['session_crypto']:
				_data['data'] = self.__add_padding__(_data['data'])
				
				if _data['compress']:
					_data['data'] = zlib.compress(_data['data'])
				_data['data'] = base64.encodestring(self.__encipher__(self.__session_blowfish__, _data['data'])).decode()
				_data['data'] = _data['data'].replace('\n','\r\n').rstrip('\r\n')
		# print("---",_data['data'])
		text = json.dumps(_data,sort_keys=True).replace(" ",'')
		text = self.__add_padding__(text)
		text = base64.encodestring(self.__encipher__(self.__static_blowfish__, text))
		text = text.decode().replace('\n','\r\n').rstrip('\r\n')
		return text