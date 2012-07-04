"""
	LabelRequest -- This makes the request to Endicia to do the actual grab of the label inforamtion.
			the other requests.

			This class will return a Hash of the xml which will be returned by the EndiciaXmlHelper
"""
import inject
import logging


#TODO: Make this use a threadpool and object pool to insure that it does not block
class LabelRequest:
	@inject.param( "endiciaPartnerId", bindto="123456" )
	@inject.param( "endiciaAccountId", bindto="123456" )
	@inject.param( "endiciaPassPhrase", bindto="x" )
	@inject.param( "endiciaBaseUrl", bindto="https://www.envmgr.com/LabelService/EwsLabelService.asmx" )
	def __init__( endiciaPartnerId, endiciaAccountId, endiciaPassPhrase, endiciaBaseUrl ):
		self.endiciaPartnerId = endiciaPartnerId
		self.endiciaAccountId = endiciaAccountId
		self.endiciaBaseUrl = endiciaBaseUrl

		logging.info( "Making requsets to %s" % ( endiciaBaseUrl ) )

	def get( self, addressTuple ):
		logging.info( "Sending Request to Label Server" )

