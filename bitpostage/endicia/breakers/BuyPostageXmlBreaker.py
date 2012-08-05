from EndiciaXmlBreaker import EndiciaXmlBreaker
from EndiciaXmlBreaker import MissingValueXmlError
from lxml import etree

class BuyPostageXmlBreaker( EndiciaXmlBreaker ):

	def __init__( self ):
		EndiciaXmlBreaker.__init__( self )

	def to_map( self ):
		_map = {}

		tree = etree.fromstring( self.xml )

		_map["Status"] = tree.findtext( "Status" )
		_map["RequesterID"] = tree.findtext( "RequesterID" )
		_map["RequestID"] = tree.findtext( "RequestID" )
		_map["AccountID"] = tree.findtext( "./CertifiedIntermediary/AccountID" )
		_map["PostageBalance"] = tree.findtext( "./CertifiedIntermediary/PostageBalance" )
		_map["AscendingBalance"] = tree.findtext( "./CertifiedIntermediary/AscendingBalance" )

		if tree.find( "ErrorMessage" ) != None:
			_map["ErrorMessage"] = tree.findtext( "ErrorMessage" )

		self.map = _map 

		return self.map
