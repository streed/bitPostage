
import tornado.web

class DefaultHandler( tornado.web.RequestHandler ):
	def get( self, uri ):
		if( uri == "" ):
			self.render( "main.html" )
		elif( uri == "about" ):
			self.render( "about.html" )
		elif( uri == "faq" ):
			self.render( "faq.html" )
		elif( uri == "login" ):
			self.render( "login.html" )
		elif( uri == "register" ):
			self.render( "register.html" )
		elif( uri == "CP" ):
			self.render( "control_panel.html" )
