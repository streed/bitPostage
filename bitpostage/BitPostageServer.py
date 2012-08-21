import inject
import sys
import os
import base64
import uuid
import logging
import tornado.web
import tornado.ioloop

#Database stuff
from database.default.DefaultDatabaseConnection import DefaultDatabaseConnection

#Configuration
from config.Config import Config

#Handlers
from handlers.DefaultHandler import DefaultHandler

class BitPostageApplication( tornado.web.Application ):

	databaseConnection = inject.attr( 'databaseConnection', DefaultDatabaseConnection )
	
	@inject.param( 'configPath', bindto='configPath' )
	@inject.param( 'listenPort', bindto='listenPort' )
	@inject.param( 'listenAddress', bindto='listenAddress' )
	def __init__( self, configPath, listenPort, listenAddress ):
		self.configPath = configPath
		self.listenPort = listenPort
		self.listenAddress = listenAddress

		logging.info( "Setting up BitPostage Server" )	
		logging.info( "Listening on %s:%d", self.listenAddress, self.listenPort )
		#logging.info( "Reading config @ %s", self.configPath )

		#self.config = None
		#try:
		#	self.config = Config( self.configPath )
		#except:
		#	logging.exception( "Could not load %s", self.configPath )

		logging.info( "Creating the handlers" )

		#TODO: Make this configurable from the config.json
		settings = {
			"static_path": os.path.join( os.path.dirname( __file__ ), "static" ),
			"template_path": os.path.join( os.path.dirname( __file__ ), "templates" ),
			"cookie_secret": base64.b64encode( uuid.uuid4().bytes + uuid.uuid4().bytes ),
			"login_url": "/login",
			"debug": True
		}

		logging.info( "Looking for templates in: %s" % ( settings["template_path"] ) )

		handlers = [ 
			( r"/(\w*)", DefaultHandler ),
			( r"/static/(.*)", tornado.web.StaticFileHandler, dict( path=settings['static_path'] ) ),
		]

		tornado.web.Application.__init__( self, handlers, **settings )

		self.listen( self.listenPort )

		tornado.ioloop.IOLoop.instance().start()
