from unittest import TestCase
import difflib
import emulator.decoder as decoder

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
		e = decoder.Decoder()
		r = e.decode(encoded_input)
		print(r)

		self.assertTrue(r==result)

	def test_decode_without_compress_with_encrypt(self):
		pass

	def test_decode_with_compress_with_encrypt(self):
		pass

