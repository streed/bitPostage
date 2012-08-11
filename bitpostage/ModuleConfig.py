import inject

import logging

from database.default import DefaultDatabaseConnection
from database.mongo import MongoDatabaseConnection

#TODO: Make this all configurable from the json.config file
#	Doing so will make it easier to manange and to update later
#	The only parts that will be configurable will be the bind's
#	to values not to classes.
#	But, for now this static wiring is ok.
class ModuleConfig( object ):
	def __call__(self, injector ):
		logging.basicConfig( level=logging.INFO, format='%(asctime)s: %(name)s - %(levelname)s - %(message)s' )
		logging.info( "Setting up dependecies for injection" )

		logging.info( "Injecting Server Information" )
		#Server information
		injector.bind( 'configPath', to='./config.json' )
		injector.bind( 'listenPort', to=8080 )
		injector.bind( 'listenAddress', to='192.168.1.10' )

		logging.info( "Injecting Endicia Information" )
		#Endicia information
		injector.bind( "endiciaPartnerId", to="123456" )
		injector.bind( "endiciaAccountId", to="123456" )
		injector.bind( "endiciaPassPhrase", to="x" )
		injector.bind( "endiciaBaseUrl", to="https://www.envmgr.com/LabelService/EwsLabelService.asmx" )

		logging.info( "Injecting Database Information" )
		#Database information
		injector.bind( DefaultDatabaseConnection,  to=MongoDatabaseConnection )
		injector.bind( "databaseAddress", to="127.0.0.1" )
		injector.bind( "databasePort", to=27017 )

		logging.info( "Injecting Email Information" )
		#Email information
		injector.bind( "gmailAccount", to="do-not-reply@bitpostage.net" )
		injector.bind( "gmailPassword", to="this is another test password" )

