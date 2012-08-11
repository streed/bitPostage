import inject
import os
import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from tornado.template import Template
from tornado.template import Loader

#TODO: Add in some kind of email address validation and an appropiate error for invalid email address
class GmailEmailMsg:
	@inject.param( "gmailAccount", bindto="fake@gmail.com" )
	@inject.param( "gmailPassword", bindto="123456" )
	def __init__( self, gmailAccount, gmailPassword ):
		self.account = gmailAccount
		self.password = gmailPassword

	def sendMessage( self, to, subject, body ):	
		msg = MIMEMultipart( "alternative" )

		msg["From"] = self.account
		msg["To"] = to
		msg["Subject"] = subject

		html = MIMEText( body, "html" )

		msg.attach( html )

		server = smtplib.SMTP( "smtp.gmail.com:587" )

		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login( self.account, self.password )
		server.sendmail( self.account, to, msg.as_string() )
		server.quit()

class GmailEmailTemplate:
	
	@inject.param( "templateFolder", bindto="bitpostage/static/templates" )
	def __init__( self, templateFolder ):
		self.loader = Loader( templateFolder )
	
	def generate( self, template, args ):
		return self.loader.load( template ).generate( **args )
