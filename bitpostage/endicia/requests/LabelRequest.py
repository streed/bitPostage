"""
	LabelRequest -- This makes the request to Endicia to do the actual grab of the label inforamtion.
			the other requests.

			This class will return a Hash of the xml which will be returned by the EndiciaXmlHelper
"""
#System stuff
import inject
import logging
import urllib
import httplib2

#bitpostage stuff
from bitpostage.endicia.helpers.LabelXmlBuilder import LabelXmlBuilder

#TODO: Make this use a object pool to insure that it does not block
class LabelRequest:
	@inject.param( "endiciaPartnerId", bindto="123456" )
	@inject.param( "endiciaAccountId", bindto="123456" )
	@inject.param( "endiciaPassPhrase", bindto="x" )
	@inject.param( "endiciaBaseUrl", bindto="www.envmgr.com" )
	@inject.param( "endiciaUrlPath", bindto="/LabelService/EwsLabelService.asmx" )
	@inject.param( "endiciaCommand", bindto="/GetPostageLabelXML" )
	def __init__( endiciaPartnerId, endiciaAccountId, endiciaPassPhrase, endiciaBaseUrl, endiciaUrlPath, endiciaCommand ):
		self.endiciaPartnerId = endiciaPartnerId
		self.endiciaAccountId = endiciaAccountId
		self.endiciaBaseUrl = endiciaBaseUrl
		self.endiciaUrlPath = endiciUrlPath
		self.endiciaCommand = endiciaCommand

		logging.info( "Making requsets to %s" % ( endiciaBaseUrl ) )

		self.http = httplib2.Http()

	def get( self, addressTuple ):
		logging.info( "Sending Request to Label Server" )
		
		url = "https://%s%s%s" % ( self.endiciaBaseUrl, self.endiciaUrlPath, self.endiciaCommand )

		logging.into( "Sending request to \"%s\"" % ( url ) )
		
		
