from django.utils import simplejson as json
import urllib2
import base64

''' Bongani Ndlovu :: Justgiving API PYTHON CLIENT BaseClient'''

class SetterProperty(object):
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc if doc is not None else func.__doc__
    def __set__(self, obj, value):
        return self.func(obj, value)

class BaseClient(object):
	"""docstring for BaseClient"""
	

  	@SetterProperty
	def debug(self, value):
		self.__dict__['debug'] = value

	def buildURL(self,loctionFormat):
		url = str(loctionFormat)
		url = url.replace('{apiKey}',str(self.parent.APIKey))
		url = url.replace('{apiVersion}',str(self.parent.APIVersion))
		return url

	def buildAuthenticationValue(self):
		if self.parent.userName and self.parent.userName is not '':
			stringToEncode = self.parent.userName+':'+self.parent.password
			return base64.b64encode(stringToEncode)
	
	def writeLine(self,string):
		return string + '<br/>'

	def __init__(self):
		self.debug = False
		super(BaseClient, self).__init__()
		