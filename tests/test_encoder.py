from unittest import TestCase
import difflib
import emulator.encoder as encoder
import emulator.settings as settings
import base64

class TestEncoder(TestCase):
	def test_encode_with_compress_without_encrypt(self):

		result = "YnHdLj/1b4RBZXynl0xG1B0domEayp/1lLk99kX4wjo7Nblx\
Ikhv1ByeVvdNenjEJTavALlsfZfSgBpLKuCMvHkaMHdNOW9g+4ytGq/cFcXO\
pW6W3rjoDzBVAFXLVj+HRATx/hb68EX3+00fDqDfc0/wdXEaV+G7h5Z\
c4M2QoF5juLcqskL1iLDYQlLVsTH5VCgC7mK204ygBrK6BopI6RZN6pX+6R\
+lfT/01GExQVs="
		command = {
				"data": {
					"lang": "ANY",
					"msgid": "CMD_GET_URLLIST",
					"region": "REGION_ALL",
					"rqid": 0
					},
				"session_crypto": False,
				"session_key": "",
				"compress": False,
				"original_size": 0
			}
		e = encoder.Encoder()
		r = e.encode(command).replace('\r\n','')
		for i,s in enumerate(difflib.ndiff(r,result)):
			if s[0] != ' ':
				print(i,repr(s))

		self.assertTrue(r==result)

	def test_encode_without_compress_with_encrypt(self):
		result = 'YnHdLj/1b4RBZXynl0xG1B0domEayp/1r6/7NjG6F2U9Ae2eQbur7I3Ut7uCkhUMWQGwmYBA/S0VK1lXXMaNrEPVvZWBu5Ndy/bySChwovOXpo8ls4oONh8j3ik9e0jQzRHBOxwVRtxks3Dmd04APKyErq5SvlJqAz7HLxVMS2ubMlYyftO14gMSQOXOn7OCk0puj0E4g3l3hdTUrnfFagZokIRsOIUhnh2Pdq6iBqOwv+1LGrLsfFO3lPWJzYs1mw7U1OmIkY1Cjm5lNz8sSyFMDh0PzigWHxo8XU7hIVnhk+z2iBlwOobGz++t2d19FeZX3PM+CBbknmSYyEqopw=='
		command = {
			'session_key': settings.TESTS_SESSION_HASH,
			'data': {
                                 'server_item_platform_info': {
                                     'platform_base_rank': 0
                                },
                        'msgid': 'CMD_GET_LOGIN_PARAM',
                       'rqid': 0},
                       'original_size': 0,
                       'session_crypto': True,
                       'compress': False
			}
		e = encoder.Encoder(crypto_key=bytearray(base64.decodestring(settings.TESTS_MAGIC_HASH.encode())))
		r = e.encode(command).replace('\r\n','')
		self.assertTrue(r==result)


	def test_encode_with_compress_with_encrypt(self):
		result = 'YnHdLj/1b4SBvSa1/0bYhcd4UAB70VUxyHv6whR4ARq0VmzU+tVGsFoR9Wd4Gi+WxsgVOVVnSXxScgtvvGefUbX7G3Ak0d01UYtsI2BBRDIHJULc8i/SM4/pMDTr3TQjtVwdHMlJi+z5PQEduWGyiSEMDW7JT8Q/6Tha3CBhup4kxzlfvtn+geZRWZHIiUxLNBmk7ozQeMm2qp+pmARHCFcdit7ETqtxREhrJSw2VymRFZFu6RuEuB/I9LK1ZHtUyDxKW0KHwLOyE35tXGFlzJrSB7Ptvc0nIg5S+ye/6oH9dH6akUdStMpxQ9nxYSmBPMUG3hbf3ocRZv14UO4wVfhT9jvWz+UPI+GRWSFrsJ7XPoBpTietoOGi7Tf32SsmwvCD7O9lSq6nm+ScqNdUorCc6RzotY2t1RDb/ekMbJDrhqBV++bczGf6G/YUvLmdnsAlzQt7YDRpzTvu0nOD4Ht3Towsb+7bBVwkqMUCxn9Tt5T1ic2LNZsO1NTpiJGNQo5uZTc/LEshTA4dD84oFh8aPF1O4SFZ4ZPs9ogZcDqGxs/vrdndfRXmV9zzPggW5J5kmMhKqKc='

		from emulator import decoder as decoder
		e = decoder.Decoder(crypto_key=bytearray(base64.decodestring(settings.TESTS_MAGIC_HASH.encode())))
		print(e.decode(result))
		command = {
			'compress': True,
			'original_size': 300,
			'session_key': '',
			'data': {
				'flowid': None,
				'crypto_type': 'COMPOUND',
				'msgid': 'CMD_GET_FOB_STATUS',
				'xuid': None,
				'rqid': 0,
				'fob_index': -1,
				'record':settings.TESTS_FOB_STATUS_RECORD,
				'sneak_mode': -1,
				'is_rescue': 0,
				'is_reward': 0,
				'result': 'NOERR',
				'kill_count': settings.TESTS_KILL_COUNT
			},
			'session_crypto': True
			}

		e = encoder.Encoder(crypto_key=bytearray(base64.decodestring(settings.TESTS_MAGIC_HASH.encode())))
		r = e.encode(command).replace('\r\n','')
		print('My result:\n{}'.format(r))
		print('their result:\n{}'.format(result))
#		for i,s in enumerate(difflib.ndiff(r,result)):
#			if s[0] != ' ':
#				print(i,repr(s))


		self.assertTrue(r==result)
