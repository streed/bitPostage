import tornado.web

class ApiHandler( tornado.web.RequestHandler ):

	def post( self, param ):
		pass

	def get( self, param ):
		self.write( "Cannot access the API via GET requests." )
