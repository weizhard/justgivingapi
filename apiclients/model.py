''' Bongani Ndlovu :: Justgiving API PYTHON CLIENT Models '''
class SetterProperty(object):
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc if doc is not None else func.__doc__
    def __set__(self, obj, value):
        return self.func(obj, value)

class Address(object):
    """docstring for Address"""
    @SetterProperty
    def country(self, value):
        self.__dict__['country'] = value
    @SetterProperty
    def countyOrState(self, value):
        self.__dict__['countyOrState'] = value
    @SetterProperty
    def line1(self, value):
        self.__dict__['line1'] = value
    @SetterProperty
    def line2(self, value):
        self.__dict__['line2'] = value
    @SetterProperty
    def postcodeOrZipcode(self, value):
        self.__dict__['postcodeOrZipcode'] = value
    @SetterProperty
    def townOrCity(self, value):
        self.__dict__['townOrCity'] = value
    
        
class RegistrationData(object):
    """docstring for RegistrationData"""
    @SetterProperty
    def acceptTermsAndConditions(self, value):
        self.__dict__['acceptTermsAndConditions'] = value
    @SetterProperty
    def address(self, value):
        self.__dict__['address'] = value
    @SetterProperty
    def causeId(self, value):
        self.__dict__['causeId'] = value
    @SetterProperty
    def email(self, value):
        self.__dict__['email'] = value
    @SetterProperty
    def firstName(self, value):
        self.__dict__['firstName'] = value
    @SetterProperty
    def lastName(self, value):
        self.__dict__['lastName'] = value
    @SetterProperty
    def password(self, value):
        self.__dict__['password'] = value
    @SetterProperty
    def reference(self, value):
        self.__dict__['reference'] = value
    @SetterProperty
    def title(self, value):
        self.__dict__['title'] = value

    def __init__(self):
        self.address = Address()
        super(RegistrationData, self).__init__()

class Event(object):
    """docstring for Event"""
    @SetterProperty
    def name(self, value):
        self.__dict__['name'] = value
    @SetterProperty
    def description(self, value):
        self.__dict__['description'] = value
    @SetterProperty
    def completionDate(self, value):
        self.__dict__['completionDate'] = value
    @SetterProperty
    def expiryDate(self, value):
        self.__dict__['expiryDate'] = value
    @SetterProperty
    def startDate(self, value):
        self.__dict__['startDate'] = value
    @SetterProperty
    def eventType(self, value):
        self.__dict__['eventType'] = value

class Image(object):
    """docstring for image"""
    @SetterProperty
    def url(self, value):
        self.__dict__['url'] = value
    @SetterProperty
    def caption(self, value):
        self.__dict__['caption'] = value
    @SetterProperty
    def isDefault(self, value):
        self.__dict__['isDefault'] = value
    

class RegisterPageRequest(object):
    """docstring for RegisterPageRequest"""
    @SetterProperty
    def images(self, value):
        self.__dict__['images'] = value
    
    @SetterProperty
    def reference(self, value):
        self.__dct__['reference'] = value
    @SetterProperty
    def eventId(self, value):
        self.__dict__['eventId'] = value
    @SetterProperty
    def pageShortName(self, value):
        self.__dict__['pageShortName'] = value
    @SetterProperty
    def pageTitle(self, value):
        self.__dict__['pageTitle'] = value
    @SetterProperty
    def activityType(self, value):
        self.__dict__['activityType'] = value
    @SetterProperty
    def targetAmount(self, value):
        self.__dict__['targetAmount'] = value
    @SetterProperty
    def justGivingOptIn(self, value):
        self.__dict__['justGivingOptIn'] = value
    @SetterProperty
    def charityOptIn(self, value):
        self.__dict__['charityOptIn'] = value
    @SetterProperty
    def eventDate(self, value):
        self.__dict__['eventDate'] = value
    @SetterProperty
    def eventName(self, value):
        self.__dict__['eventName'] = value
    @SetterProperty
    def attribution(self, value):
        self.__dict__['attribution'] = value
    @SetterProperty
    def charityFunded(self, value):
        self.__dict__['charityFunded'] = value
    @SetterProperty
    def causeId(self, value):
        self.__dict__['causeId'] = value
    @SetterProperty
    def charityId(self, value):
        self.__dict__['charityId'] = value
    

        
