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
		if _map["Status"] == None:
			raise MissingValueXmlError( "Status" )

		_map["RequesterID"] = tree.findtext( "RequesterID" )
		if _map["RequesterID"] == None:
			raise MissingValueXmlError( "RequesterID" )

		_map["RequestID"] = tree.findtext( "RequestID" )
		if _map["RequestID"] == None:
			raise MissingValueXmlError( "RequestID" )

		_map["AccountID"] = tree.findtext( "./CertifiedIntermediary/AccountID" )
		if _map["AccountID"] == None:
			raise MissingValueXmlError( "AccountID" )

		_map["PostageBalance"] = tree.findtext( "./CertifiedIntermediary/PostageBalance" )
		if _map["PostageBalance"] == None: 
			raise MissingValueXmlError( "PostageBalance" )

		_map["AscendingBalance"] = tree.findtext( "./CertifiedIntermediary/AscendingBalance" )
		if _map["AscendingBalance"] == None:
			raise MissingValueXmlError( "AscendingBalance" )

		if tree.find( "ErrorMessage" ) != None:
			_map["ErrorMessage"] = tree.findtext( "ErrorMessage" )

		self.map = _map 

		return self.map
