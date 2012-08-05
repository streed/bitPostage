"""
	LabelRequest -- This makes the request to Endicia to do the actual grab of the label inforamtion.
			the other requests.

			This class will return a Hash of the xml which will be returned by the EndiciaXmlHelper
"""
#bitpostage stuff
from bitpostage.endicia.breakers.LabelXmlBreaker import LabelXmlBreaker
from bitpostage.endicia.requests.EndiciaRequest import EndiciaRequest

class LabelRequest( EndiciaRequest ):
	def __init__( self ):
		EndiciaRequest.__init__( self )
		self.breaker = LabelXmlBreaker()
		self.endiciaCommand = "/GetPostageLabelXML"
		self.endiciaPostName = "labelRequestXML"
