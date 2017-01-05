''' Bongani Ndlovu :: Justgiving API PYTHON CLIENT '''

from apiclients.accountAPI import AccountAPI
from apiclients.fundraisingAPI import FundraisingAPI
class SetterProperty(object):
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc if doc is not None else func.__doc__
    def __set__(self, obj, value):
        return self.func(obj, value)

class JustgivingClient(object):
	"""docstring for JustgivingClient"""
	
	@SetterProperty
	def APIKey(self, value):
		self.__dict__['APIKey'] = value
	@SetterProperty
	def APIVersion(self, value):
		self.__dict__['APIVersion'] = value
	@SetterProperty
	def userName(self, value):
		self.__dict__['userName'] = value
	@SetterProperty
	def password(self, value):
		self.__dict__['password'] = value
	@SetterProperty
	def rootDomain(self, value):
		self.__dict__['rootDomain'] = value

	@SetterProperty
	def fundraising(self, value):
		self.__dict__['fundraising'] = value
	@SetterProperty
	def account(self, value):
		self.__dict__['account'] = value
	@SetterProperty
	def charity(self, value):
		self.__dict__['charity'] = value
	@SetterProperty
	def donation(self, value):
		self.__dict__['donation'] = value
	@SetterProperty
	def search(self, value):
		self.__dict__['search'] = value
	@SetterProperty
	def event(self, value):
		self.__dict__['event'] = value
	@SetterProperty
	def team(self, value):
		self.__dict__['team'] = value


	def __init__(self, rootDomain=None, APIKey=None, APIVersion=None, userName=None, password=None):
		super(JustgivingClient, self).__init__()
		self.rootDomain = rootDomain and rootDomain or 'https://api.justgiving.com/'
		self.APIKey = APIKey or ''
		self.APIVersion = APIVersion and APIVersion or 1
		self.userName = userName and userName or ''
		self.password = password and password or ''
		self.debug = False

		''' init clients '''
		self.account = AccountAPI(self)
		self.fundraising = FundraisingAPI(self)
