import inject

import logging

from database.default import DefaultDatabaseConnection
from database.mongo import MongoDatabaseConnection

class ModuleConfig( object ):
	def __call__(self, injector ):
		injector.bind( 'configPath', to='./config.json' )
		injector.bind( 'listenPort', to=8080 )
		injector.bind( 'listenAddress', to='192.168.255.102' )

		injector.bind( DefaultDatabaseConnection,  to=MongoDatabaseConnection )

		logging.basicConfig( level=logging.INFO, format='%(asctime)s: %(name)s - %(levelname)s - %(message)s' )

		logging.info( "Setting up dependecies for injection" )
