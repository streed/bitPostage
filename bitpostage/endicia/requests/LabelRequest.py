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
from lxml import etree
from urllib import urlencode

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
	def __init__( self, endiciaPartnerId, endiciaAccountId, endiciaPassPhrase, endiciaBaseUrl, endiciaUrlPath, endiciaCommand ):
		self.endiciaPartnerId = endiciaPartnerId
		self.endiciaAccountId = endiciaAccountId
		self.endiciaBaseUrl = endiciaBaseUrl
		self.endiciaUrlPath = endiciaUrlPath
		self.endiciaCommand = endiciaCommand

		logging.info( "Making requsets to %s" % ( endiciaBaseUrl ) )

		self.http = httplib2.Http()

	def get( self, label ):
		logging.info( "Sending Request to Label Server" )
		
		url = "https://%s%s%s" % ( self.endiciaBaseUrl, self.endiciaUrlPath, self.endiciaCommand )

		logging.info( "Sending request to \"%s\"" % ( url ) )
		
		requestString = self.buildRequest( label )	

		#print requestString

		headers = { "Content-Type": "application/x-www-form-urlencoded" }

		response, content = self.http.request( url, "POST", body=requestString, headers=headers )

		#print response
		#print content



	def buildRequest( self, label ):
		xmlString = etree.tostring( label.to_xml() )

		#print etree.tostring( label.to_xml(), pretty_print=True )

		#return urlencode( { "labelRequestXML" : xmlString } )
		return "labelRequestXML=%s" % (xmlString )
