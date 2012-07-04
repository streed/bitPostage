
import tornado.web

class DefaultHandler( tornado.web.RequestHandler ):
	def get( self, uri ):
		if( uri == "" ):
			self.render( "templates/main.html" )
		elif( uri == "about" ):
			self.render( "templates/about.html" )
		elif( uri == "faq" ):
			self.render( "templates/faq.html" )
		elif( uri == "login" ):
			self.render( "templates/login.html" )
		elif( uri == "register" ):
			self.render( "templates/register.html" )
