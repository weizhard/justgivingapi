import urllib2
import urllib

''' Bongani Ndlovu :: Justgiving API PYTHON CLIENT URLLib2Wrapper '''

class HeadRequest(urllib2.Request):
	def get_method(self):
		return 'HEAD'

class URLLib2Wrapper(object):
	"""docstring for URLLib2Wrapper"""
	def __init__(self):
		super(URLLib2Wrapper, self).__init__()

	def __makecall(self, opener, request):
		try:
			response = opener.open(request)
		except urllib2.HTTPError, response:
			pass

		#response.close()

		return dict(code=response.code and response.code or 'no code' , headers=response.info and response.info() or None , url=response.geturl and response.geturl() or None, content=response.read and response.read() or '')

	def setCredentials(self, request, base64Credentials=None, contentType=None):
		contentType = contentType and contentType or 'application/json'  
		if base64Credentials and base64Credentials is not '':
			request.add_header('Authorize', 'Basic ' + str(base64Credentials))
			request.add_header('Authorization', 'Basic ' + str(base64Credentials))
			request.add_header('Content-Type', contentType)
		else:
			request.add_header('Content-Type', contentType)
	
	def get(self, url, base64Credentials,contentType):
		opener = urllib2.build_opener(urllib2.HTTPHandler(),urllib2.HTTPDefaultErrorHandler())
		request = urllib2.Request(str(url))
		self.setCredentials(request, base64Credentials,contentType)
		request.get_method = lambda: 'GET'
		return self.__makecall(opener,request)
	
	def post(self, url, base64Credentials, payload, contentType):
		opener = urllib2.build_opener(urllib2.HTTPHandler(),urllib2.HTTPDefaultErrorHandler())
		request = urllib2.Request(str(url),data=payload)
		self.setCredentials(request, base64Credentials,contentType)
		request.get_method = lambda: 'POST'
		print opener.open(request)
		return self.__makecall(opener,request)
	
	def put(self, url, base64Credentials, payload, contentType):
		opener = urllib2.build_opener(urllib2.HTTPHandler(),urllib2.HTTPDefaultErrorHandler())
		request = urllib2.Request(str(url),data=payload)
		self.setCredentials(request, base64Credentials,contentType)
		request.get_method = lambda: 'PUT'
		return self.__makecall(opener,request)

	def head(self, url, base64Credentials,contentType):
		opener = urllib2.build_opener(urllib2.HTTPHandler(),urllib2.HTTPDefaultErrorHandler())
		request = HeadRequest(str(url))
		self.setCredentials(request, base64Credentials,contentType)
		request.get_method = lambda: 'HEAD'
		return self.__makecall(opener,request)



		