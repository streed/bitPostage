from EndiciaXmlBreaker import EndiciaXmlBreaker
from lxml import etree
from StringIO import StringIO

class LabelXmlBreaker( EndiciaXmlBreaker ):

	def __init__( self ):
		EndiciaXmlBreaker.__init__( self )

	def setXmlString( self, xml ):
		self.xml = StringIO( xml )

	def to_map( self ):
		self.map = {}

		tree = etree.parse( self.xml )

		print( etree.tostring( tree.getroot(), pretty_print=True ) )
		



