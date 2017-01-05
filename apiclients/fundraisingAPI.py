from baseclient import *
from ..http.urllib2_wrapper import URLLib2Wrapper
from model import *
import jsonpickle
import urllib
from django.utils import simplejson as json

''' Bongani Ndlovu :: Justgiving API PYTHON CLIENT FundraisingAPI '''

class FundraisingAPI(BaseClient):
	"""docstring for FundraisingAPI"""
	@SetterProperty
	def parent(self, value):
		self.__dict__['parent'] = value
	@SetterProperty
	def urllib2Wrapper(self, value):
		self.__dict__['urllib2Wrapper'] = value
	
	
	def create(self, pageData):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/fundraising/pages'
		url = self.buildURL(locationFromat)
		payload = jsonpickle.encode(pageData, unpicklable=False)
		return self.urllib2Wrapper.put(url,self.buildAuthenticationValue(),payload,None)
	
	def createEventForPage(self, eventData):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/event'
		url = self.buildURL(locationFromat)
		payload = jsonpickle.encode(eventData, unpicklable=False)
		return self.urllib2Wrapper.post(url,self.buildAuthenticationValue(),payload,None)

	def validate(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account/validate'
		url = self.buildURL(locationFromat)
		
		return self.urllib2Wrapper.post(url,self.buildAuthenticationValue(),payload,None)

	def listAllPages(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/account/' + payload + '/pages'
		url = self.buildURL(locationFromat)
		
		return self.urllib2Wrapper.get(url,None,'application/json')
		
	def retrievePages(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/fundraising/pages/' 
		url = self.buildURL(locationFromat)
			
		return self.urllib2Wrapper.get(url,self.buildAuthenticationValue(),'application/json')
	
	def getPageDetails(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/fundraising/pages/' + payload 
		url = self.buildURL(locationFromat)
			
		return self.urllib2Wrapper.get(url,self.buildAuthenticationValue(),'application/json')

	def getPageDonations(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/fundraising/pages/' + payload +'/donations'
		url = self.buildURL(locationFromat)
			
		return self.urllib2Wrapper.get(url,self.buildAuthenticationValue(),'application/json')

	def suggestPageShortNames(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/fundraising/pages/suggest?' + urllib.urlencode({'preferredName' : payload, 'format':'json'})
		url = self.buildURL(locationFromat)
		
		return self.urllib2Wrapper.get(url,None,'application/json')
	
	def isShortNameRegistered(self, payload):
		locationFromat = self.parent.rootDomain + '{apiKey}/v{apiVersion}/fundraising/pages/' + urllib.quote_plus(payload)
		url = self.buildURL(locationFromat)
		response = self.urllib2Wrapper.head(url,None,'application/json')
		
		if response['code'] == 200:
			return {'status': True, 'alternatives':json.loads(self.suggestPageShortNames(payload)['content'])} 
		elif response['code'] == 404:
			return {'status': False, 'message':'not found' }
		else:
			return {'status': False, 'message':'unknown error with http code: '+ str(response['code']) }

	def __init__(self, justgivingAPI):
		self.parent = justgivingAPI
		self.urllib2Wrapper = URLLib2Wrapper()
		super(FundraisingAPI, self).__init__()
