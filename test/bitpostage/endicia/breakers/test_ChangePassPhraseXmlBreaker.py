from nose.tools import assert_raises
from bitpostage.endicia.breakers.ChangePassPhraseXmlBreaker import ChangePassPhraseXmlBreaker

from lxml.builder import E
from lxml import etree

def test_ChangePassPhraseXmlBreaker_parses_correctly():
	"""The ChangePassPhraseXmlBreaker should parse the response correctly."""
	def mock_response():
		return etree.tostring( E.ChangePassPhraseRequestResponse(
			E.Status( str( 0 ) ),
			E.RequesterID( "abcd" ),
			E.RequestID( "CPP123" )
		) )

	breaker = ChangePassPhraseXmlBreaker()

	breaker.setXmlString( mock_response() )

	ret = breaker.to_map()

	assert ret["Status"] == "0"
	assert ret["RequesterID"] == "abcd"
	assert ret["RequestID"] == "CPP123"
