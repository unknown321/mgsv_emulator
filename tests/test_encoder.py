from unittest import TestCase
import difflib
import emulator.encoder as encoder

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
		pass

	def test_encode_with_compress_with_encrypt(self):
		pass

