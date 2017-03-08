from unittest import TestCase
import difflib
import emulator.decoder as decoder
import emulator.settings as settings
import base64

class TestEncoder(TestCase):
	def test_decode_with_compress_without_encrypt(self):

		encoded_input = "YnHdLj/1b4RBZXynl0xG1B0domEayp/1lLk99kX4wjo7Nblx\
Ikhv1ByeVvdNenjEJTavALlsfZfSgBpLKuCMvHkaMHdNOW9g+4ytGq/cFcXO\
pW6W3rjoDzBVAFXLVj+HRATx/hb68EX3+00fDqDfc0/wdXEaV+G7h5Z\
c4M2QoF5juLcqskL1iLDYQlLVsTH5VCgC7mK204ygBrK6BopI6RZN6pX+6R\
+lfT/01GExQVs="
		result = {
				"data": {
					"lang": "ANY",
					"msgid": "CMD_GET_URLLIST",
					"region": "REGION_ALL",
					"rqid": 0
					},
				"session_crypto": False,
				"session_key": "",
				"compress": False,
				"original_size": 71
			}
		d = decoder.Decoder()
		r = d.decode(encoded_input)
		print(r)

		self.assertTrue(r==result)

	def test_decode_without_compress_with_encrypt(self):
		encoded_input = 'YnHdLj/1b4RBZXynl0xG1B0domEayp/1r6/7NjG6F2U9Ae2eQbur7I3Ut7uCkhUMWQGwmYBA/S0VK1lXXMaNrEPVvZWBu5Ndy/bySChwovOXpo8ls4oONh8j3ik9e0jQzRHBOxwVRtxks3Dmd04APKyErq5SvlJqAz7HLxVMS2ubMlYyftO14gMSQOXOn7OCk0puj0E4g3l3hdTUrnfFagZokIRsOIUhnh2Pdq6iBqOwv+1LGrLsfFO3lPWJzYs1mw7U1OmIkY1Cjm5lNz8sSyFMDh0PzigWHxo8XU7hIVnhk+z2iBlwOobGz++t2d19FeZX3PM+CBbknmSYyEqopw=='
		result = {
				'session_key': '',
				'data': {
					'server_item_platform_info': {
						'platform_base_rank': 0
					},
					'msgid': 'CMD_GET_LOGIN_PARAM',
					'rqid': 0},
				'original_size': 93,
				'session_crypto': True,
				'compress': False
			}

		d = decoder.Decoder(crypto_key=bytearray(base64.decodestring(settings.TESTS_MAGIC_HASH.encode())))
		r = d.decode(encoded_input)
		r['session_key'] = ''
		self.assertTrue(result==r)

	def test_decode_with_compress_with_encrypt(self):
		pass

