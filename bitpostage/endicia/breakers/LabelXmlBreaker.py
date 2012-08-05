from EndiciaXmlBreaker import EndiciaXmlBreaker
from EndiciaXmlBreaker import MissingValueXmlError
from lxml import etree

class LabelXmlBreaker( EndiciaXmlBreaker ):

	def __init__( self ):
		EndiciaXmlBreaker.__init__( self )

	def to_map( self ):
		_map = {}

		tree = etree.fromstring( self.xml )

		_map["Status"] = tree.findtext( "Status" )
		_map["Base64LabelImage"] = tree.findtext( "Base64LabelImage" )
		_map["PIC"] = tree.findtext( "PIC" )
		_map["TrackingNumber"] = tree.findtext( "TrackingNumber" )
		_map["FinalPostage"] = tree.findtext( "FinalPostage" )
		_map["TransactionID"] = tree.findtext( "TransactionID" )
		_map["TransactionDateTime"] = tree.findtext( "TransactionDateTime" )
		_map["PostmarkDate"] = tree.findtext( "PostmarkDate" )
		_map["PostageBalance"] = tree.findtext( "PostageBalance" )
		_map["ErrorMessage"] = tree.findtext( "ErrorMessage" )
		_map["FinalPostage"] = tree.findtext( "FinalPostage" )
		
		self.map = _map

		return self.map
