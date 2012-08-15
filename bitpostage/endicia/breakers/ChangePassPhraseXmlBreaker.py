from EndiciaXmlBreaker import EndiciaXmlBreaker
from EndiciaXmlBreaker import MissingValueXmlError
from lxml import etree

class ChangePassPhraseXmlBreaker( EndiciaXmlBreaker ):

	def __init__( self ):
		EndiciaXmlBreaker.__init__( self )

	def to_map( self ):
		_map = {}

		tree = etree.fromstring( self.xml )

		_map["Status"] = tree.findtext( "Status" )
		_map["RequesterID"] = tree.findtext( "RequesterID" )
		_map["RequestID"] = tree.findtext( "RequestID" )

		if _map["Status"] != "0":
			_map["ErrorMessage"] = tree.findtext( "ErrorMessage" )

		self.map = _map

		return self.map
