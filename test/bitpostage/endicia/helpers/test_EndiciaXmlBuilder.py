from nose.tools import assert_raises
from bitpostage.endicia.helpers.EndiciaXmlBuilder import LabelXmlBuilder
from bitpostage.endicia.helpers.EndiciaXmlBuilder import InvalidLabelValueError
from lxml import etree

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

	
	print etree.tostring( builder.to_xml(), pretty_print=True )
	assert false
