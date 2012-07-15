from bitpostage.endicia.requests.LabelRequest import LabelRequest
from bitpostage.endicia.helpers.LabelXmlBuilder import LabelXmlBuilder

from lxml.builder import E

def test_LabelRequest_make_request():
	request = LabelRequest()

	def mockToAddress():
		ret = (
			#E.ToCompany( "fake" ),
			E.ToName( "sean" ),
			E.ToAddress1( "4411 galesbury ln" ),
			E.ToAddress2( "" ),
			E.ToCity( "chantilly" ),
			E.ToState( "VA" ),
			E.ToPostalCode( "20151" ),
			#E.ToZIP4( "1234" ),
			#E.ToPhone( "1234567890" ),
			#E.ToEMail( "fake@fake.com" )
		)

		return ret

	def mockFromAddress():
		ret = (
			E.FromName( "david" ),
			#E.FromCompany( "Fake company" ),
			E.ReturnAddress1( "4419 galesbury ln" ),
			E.ReturnAddress2( "" ),
			E.FromCity( "chantilly" ),
			E.FromState( "VA" ),
			E.FromPostalCode( "20151" ),
			#E.FromZIP4( "1234" ),
			#E.FromPhone( "1234567890" )
		)

		return ret
	builder = LabelXmlBuilder()

	builder.setTest()
	builder.setLabelType( "Domestic" )
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
	builder.setMailPieceShape( "Parcel" )
	builder.setDimensions( ( 10.0, 10.0, 1 ) )
	builder.setToAddress( mockToAddress )
	builder.setFromAddress( mockFromAddress )
	builder.setPartnerCustomerID( "123456" )
	builder.setPartnerTransactionID( "123456" )

	request.get( builder )

	assert False
