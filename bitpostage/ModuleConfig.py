import inject

import logging

from database.default import DefaultDatabaseConnection
from database.mongo import MongoDatabaseConnection

class ModuleConfig( object ):
	def __call__(self, injector ):
		#Server information
		injector.bind( 'configPath', to='./config.json' )
		injector.bind( 'listenPort', to=8080 )
		injector.bind( 'listenAddress', to='192.168.1.5' )

		#Endicia information
		#injector.bind( "endiciaPartnerId", "123456" )
		#injector.bind( "endiciaAccountId", "123456" )
		#injector.bind( "endiciaPassPhrase", "x" )
		#injector.bind( "endiciaBaseUrl", "https://www.envmgr.com/LabelService/EwsLabelService.asmx" )

		injector.bind( DefaultDatabaseConnection,  to=MongoDatabaseConnection )

		logging.basicConfig( level=logging.INFO, format='%(asctime)s: %(name)s - %(levelname)s - %(message)s' )

		logging.info( "Setting up dependecies for injection" )
