from lxmk.builder import E
from EndiciaXmlBuilder import EndiciaXmlBuilder

class EndiciaXmlAddressBuilder( EndiciaXmlBuilder ):

	xml = {}

	def __init__( self, _type="From" ):
		EndiciaXmlBuilder.__init__( self )
		self._type = _type

	def setName( self, name ):
		xml["Name"] = name
	
	def setCompany( self, company ):
		xml["Company"] = company

	def setAddress1( self, address ):
		xml["Address1"] = address
	
	def setAddress2( self, address ):
		xml["Address2"] = address

	def setCity( self, city ):
		xml["City"] = city

	def setState( self, state ):
		xml["State"] = state 
	
	def setPostalCode( self, postalCode ):
		xml["PostalCode"] = postalCode

	def setZIP4( self, zip4 ):
		xml["ZIP4"] = zip4
	
	def setCountry( self, country ):
		xml["Country"] = country

	def setPhone( self, phone ):
		xml["Phone"] = phone

	def setEmail( self, email ):
		xml["EMail"] = email

	def setCountryCode( self, countrycode ):
		xml["CountryCode"] = countrycode

	#TODO: The self.xmlString is completely different for both the To and From XML's.
	#	This needs to be redone :/
	def to_xml():
		
		NAME = None
		COMPANY = None
		ADDRESS1 = None
		ADDRESS2 = None
		CITY = None
		STATE = None
		ZIP4 = None
		COUNTRY = None
		PHONE = None
		EMAIL = None
		COUNTRYCODE = None

		if self._type == "From":
			NAME = E.FromName
			COMPANY = E.FromCompany
			ADDRESS1 = E.ReturnAddress1
			ADDRESS2 = E.ReturnAddress2
			CITY = E.FromCity
			STATE = E.FromState
			ZIP4 = E.FromZIP4
			COUNTRY = E.FromCountry
			PHONE = E.FromPhone
			EMAIL = E.FromEmail
			COUNTRYCODE = E.FromCountryCode
		else:
			NAME = E.ToName
			COMPANY = E.ToCompany
			ADDRESS1 = E.ReturnAddress1
			ADDRESS2 = E.ReturnAddress2
			CITY = E.ToCity
			STATE = E.ToState
			ZIP4 = E.ToZIP4
			COUNTRY = E.ToCountry
			PHONE = E.ToPhone
			EMAIL = E.ToEmail
			COUNTRYCODE = E.ToCountryCode
			

		self.xmlString = (
			NAME( xml["Name"] ),
			COMPANY( xml["Company"] ),
			ADDRESS1( xml["Address1"] ),
			ADDRESS2( xml["Address2"] ),
			CITY( xml["City"] ),
			STATE( xml["State"] ),
			POSTALCODE( xml["PostalCode"] ),
			ZIP4( xml["ZIP4"] ),
			COUNTRYCODE( xml["CountryCode"] )
		)

		
