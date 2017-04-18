from requests import Request, Session

class HttpClient(object):
	"""docstring for HttpClient"""
	def __init__(self):
		super(HttpClient, self).__init__()

	def send(self, data, _url):
		url = 'https://mgstpp-game.konamionline.com' + _url
		p = {"httpMsg": data}
		headers = {"Content-Type": "application/x-www-form-urlencoded", "Connection":"Keep-Alive"}

		s = Session()
		req = Request('POST', url, data=p, headers=headers)
		prepped = req.prepare()
		response = s.send(prepped)
		return response
