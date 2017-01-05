from baseclient import *
from ..http.urllib2_wrapper import URLLib2Wrapper
import jsonpickle
import urllib

''' Bongani Ndlovu :: Justgiving API PYTHON CLIENT AccountAPI '''

class AccountAPI(BaseClient):
	"""docstring for AccountAPI"""
	@SetterProperty
	def parent(self, value):
		self.__dict__['parent'] = value
	@SetterProperty
	def urllib2Wrapper(self, value):
		self.__dict__['urllib2Wrapper'] = value
	
	
	def create(self, registrationData):
		locationFormat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account'
		url = self.buildURL(locationFormat)
		payload = jsonpickle.encode(registrationData, unpicklable=False)
		return self.urllib2Wrapper.put(url,self.buildAuthenticationValue(),payload,None)
	
	def retrieveAccount(self):
		locationFormat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account'
		url = self.buildURL(locationFormat)
		return self.urllib2Wrapper.get(url,self.buildAuthenticationValue(),'application/json')

	def validate(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account/validate'
		url = self.buildURL(locationFromat)
		
		return self.urllib2Wrapper.post(url,self.buildAuthenticationValue(),payload,None)

	def listAllPages(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account/' + payload + '/pages'
		url = self.buildURL(locationFromat)
		
		return self.urllib2Wrapper.get(url,None,'application/json')

	def requestPasswordReminder(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account/' + payload + '/requestpasswordreminder'
		url = self.buildURL(locationFromat)
		
		return self.urllib2Wrapper.get(url,None,'application/json')
	
	def isEmailRegistered(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account/' + payload
		url = self.buildURL(locationFromat)
		response = self.urllib2Wrapper.head(url,None,'application/json')
		
		if response['code'] == 200:
			return True 
		elif response['code'] == 404:
			return False
		else:
			return False

	def isEmailRegisteredIfSoGetPages(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account/' + payload
		url = self.buildURL(locationFromat)
		response = self.urllib2Wrapper.head(url,None,'application/json')
		
		if response['code'] == 200:
			return self.listAllPages(payload)
		elif response['code'] == 404:
			return {'code':404}
		else:
			return {'code':404}

	def __init__(self, justgivingAPI):
		self.parent = justgivingAPI
		self.urllib2Wrapper = URLLib2Wrapper()
		super(AccountAPI, self).__init__()




		