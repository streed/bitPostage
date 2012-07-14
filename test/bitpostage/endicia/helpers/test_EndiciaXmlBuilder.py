from nose.tools import assert_raises
from bitpostage.endicia.helpers.LabelXmlBuilder import LabelXmlBuilder
from bitpostage.endicia.helpers.AddressXmlBuilder import AddressXmlBuilder

from bitpostage.endicia.helpers.LabelXmlBuilder import InvalidLabelValueError
from bitpostage.endicia.helpers.AddressXmlBuilder import InvalidAddressTypeError
from lxml import etree
from lxml.builder import E

def test_LabelXmlBuilder_exception_setLabelType():
	"""Passing the wrong values to LabelXmlBuilder should throw a InvalidLabelValueError"""
	builder = LabelXmlBuilder()
	
	assert_raises( InvalidLabelValueError, builder.setLabelType, "wrong" )
	assert_raises( InvalidLabelValueError, builder.setLabelSubType, "wrong" )
	assert_raises( InvalidLabelValueError, builder.setLabelSize, "wrong" )
	assert_raises( InvalidLabelValueError, builder.setImageFormat, "wrong" )
	assert_raises( InvalidLabelValueError, builder.setImageResolution, "wrong" )
	assert_raises( InvalidLabelValueError, builder.setMailClass, "wrong" )
	assert_raises( InvalidLabelValueError, builder.setMailPieceShape, "wrong" )
	
def test_LabelXmlBuilder_exception_setDateAdvance():
	"""Passing a value outside of the [0,7] range should throw a InvalidLabelValueError"""
	builder = LabelXmlBuilder()
	
	assert_raises( InvalidLabelValueError, builder.setDateAdvance, -1 )
	assert_raises( InvalidLabelValueError, builder.setDateAdvance, 8 )

def test_LavelXmlBuilder_to_string():
	"""The to_string() should return a valid XML request"""
	def mockToAddress():
		ret = (
			E.ToCompany( "fake" ),
			E.ToAddress1( "1234 Fake St" ),
			E.ToAddress2( "Apartment 1" ),
			E.ToCity( "Faketilly" ),
			E.ToState( "VA" ),
			E.ToPostalCode( "12345" ),
			E.ToZIP4( "1234" ),
			E.ToPhone( "1234567890" ),
			E.ToEMail( "fake@fake.com" )
		)

		return ret

	def mockFromAddress():
		ret = (
			E.FromName( "Fakeson" ),
			E.FromCompany( "Fake company" ),
			E.ReturnAddress1( "12345 Fake ave." ),
			E.ReturnAddress2( "Room 10" ),
			E.FromCity( "Fakeville" ),
			E.FromState( "VA" ),
			E.FromPostalCode( "12345" ),
			E.FromZIP4( "1234" ),
			E.FromPhone( "1234567890" )
		)

		return ret
	builder = LabelXmlBuilder()

	builder.setTest()
	builder.setLabelType( "Default" )
	builder.setLabelSubType( "None" )
	builder.setLabelSize( "4x6" )
	builder.setImageFormat( "JPEG" )
	builder.setImageResolution( "300" )
	builder.setRequestID( "123456" )
	builder.setAccountID( "123456" )
	builder.setPassPhrase( "x" )
	builder.setMailClass( "First" )
	builder.setDateAdvance( 0 )
	builder.setWeightOunces( 4.1 )
	builder.setMailPieceShape( "Letter" )
	builder.setDimensions( ( 10, 10, 0.5 ) )
	builder.setToAddress( mockToAddress )
	builder.setFromAddress( mockFromAddress )

	ret = builder.to_xml()

	assert ret.tag == "LabelRequest"
	assert ret[0].tag == "Test"
	assert ret[1].tag == "LabelType"
	assert ret[2].tag == "LabelSubType"
	assert ret[3].tag == "LabelSize"
	assert ret[4].tag == "ImageFormat"
	assert ret[5].tag == "ImageResolution"
	assert ret[6].tag == "RequesterID"
	assert ret[7].tag == "AccountID"
	assert ret[8].tag == "PassPhrase"
	assert ret[9].tag == "MailClass"
	assert ret[10].tag == "DateAdvance"
	assert ret[11].tag == "WeightOz"
	assert ret[12].tag == "MailpieceShape"
	assert ret[13].tag == "MailpieceDimensions"

#TODO: Write out this length test
def test_LabelXmlBuilder_test_should_notn_raise_exception_when_setup_from_correct_map():
	"""This should not raise any exceptions because the information is valid"""
	def mockToAddress():
		ret = (
			E.ToCompany( "fake" ),
			E.ToAddress1( "1234 Fake St" ),
			E.ToAddress2( "Apartment 1" ),
			E.ToCity( "Faketilly" ),
			E.ToState( "VA" ),
			E.ToPostalCode( "12345" ),
			E.ToZIP4( "1234" ),
			E.ToPhone( "1234567890" ),
			E.ToEMail( "fake@fake.com" )
		)

		return ret

	def mockFromAddress():
		ret = (
			E.FromName( "Fakeson" ),
			E.FromCompany( "Fake company" ),
			E.ReturnAddress1( "12345 Fake ave." ),
			E.ReturnAddress2( "Room 10" ),
			E.FromCity( "Fakeville" ),
			E.FromState( "VA" ),
			E.FromPostalCode( "12345" ),
			E.FromZIP4( "1234" ),
			E.FromPhone( "1234567890" )
		)

		return ret

	builder = LabelXmlBuilder()

	builder.setTest()
	builder.setLabelType( "Default" )
	builder.setLabelSubType( "None" )
	builder.setLabelSize( "4x6" )
	builder.setImageFormat( "JPEG" )
	builder.setImageResolution( "300" )
	builder.setRequestID( "123456" )
	builder.setAccountID( "123456" )
	builder.setPassPhrase( "x" )
	builder.setMailClass( "First" )
	builder.setDateAdvance( 0 )
	builder.setWeightOunces( 4.1 )
	builder.setMailPieceShape( "Letter" )
	builder.setDimensions( ( 10, 10, 0.5 ) )
	builder.setToAddress( mockToAddress )
	builder.setFromAddress( mockFromAddress )
	builder.setShipDate( "10/7/2012" )

	_map = builder.xml

	assert_raises( Exception, builder.setByMap, _map )

	

def test_AddressXmlBuilder_exception_thrown_for_invalid_address_type():
	"""If the _type is not in ["To", "From"] then it should throw a InvalidAddressTypeError when to_xml is called"""
	builder = AddressXmlBuilder( _type="wrong" )

	assert_raises( InvalidAddressTypeError, builder.to_xml )

def test_AddressXmlBuilder_produces_correct_xml():
	"""AddressXmlBuilder should produce a correct xml sub document"""
	addr = AddressXmlBuilder( _type="To" )

	addr.setName( "Fake name" )
	addr.setCompany( "Fake company" )
	addr.setAddress1( "1234 Fake St" )
	addr.setAddress2( "" )
	addr.setCity( "Fakeville" )
	addr.setState( "VA" )
	addr.setPostalCode( "12345" )
	addr.setZIP4( "1234" )
	addr.setCountry( "US" )
	addr.setPhone( "1234567890" )
	addr.setEmail( "fake@fake.com" )
	addr.setCountryCode( "US" )

	ret = addr.to_xml()	

	assert ret[0].tag == "ToName"
	assert ret[1].tag == "ToCompany"
	assert ret[2].tag == "ToAddress1"
	assert ret[3].tag == "ToAddress2"
	assert ret[4].tag == "ToCity"
	assert ret[5].tag == "ToState"
	assert ret[6].tag == "ToPostalCode"
	assert ret[7].tag == "ToZIP4"
	assert ret[8].tag == "ToPhone"
	assert ret[9].tag == "ToEMail"

	addr._type = "From"
	ret = addr.to_xml()	

	assert ret[0].tag == "FromName"
	assert ret[1].tag == "FromCompany"
	assert ret[2].tag == "ReturnAddress1"
	assert ret[3].tag == "ReturnAddress2"
	assert ret[4].tag == "FromCity"
	assert ret[5].tag == "FromState"
	assert ret[6].tag == "FromPostalCode"
	assert ret[7].tag == "FromZIP4"
	assert ret[8].tag == "FromCountry"
	assert ret[9].tag == "FromPhone"
	assert ret[10].tag == "FromEMail"

