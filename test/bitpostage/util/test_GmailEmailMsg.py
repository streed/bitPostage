from nose.tools import assert_raises
from bitpostage.util.GmailSmtp import GmailEmailMsg
from bitpostage.util.GmailSmtp import GmailEmailTemplate

from smtplib import SMTPAuthenticationError, SMTPSenderRefused

import inject

def closure( e, *args ):	
	try:
		e( *args ) 				
		raise Exception( "Everything is ok" )
	except:
		raise

def test_GmailEmailMsg_should_not_raise_any_exceptions_on_sending_email():		
	"""GmailEmailMsg should send the email fine without raising any exceptions"""
	injector = inject.Injector()
	injector.bind( "gmailAccount", to="do-not-reply@bitpostage.net" )
	injector.bind( "gmailPassword", to="this is another test password" )

	inject.register( injector )

	gmail = GmailEmailMsg()
	temp = GmailEmailTemplate()

	assert_raises( Exception, closure, gmail.sendMessage, "sean@bitpostage.net", "test message", temp.generate( "welcome_email.html", { "userName": "sean", "domain": "test.bitpostage.net", "userToken": "1234567890" } ) )
	assert_raises( Exception, closure, gmail.sendMessage, "sean@bitpostage.net", "completion email", temp.generate( "completion_email.html", { "userName": "sean", "domain": "test.bitpostage.net", } ) )

def test_GmailEmailMsg_should_raise_SMTPAuthenticationError():		
	"""GmailEmailMsg should raise SMTPAuthenticationError because of wrong password"""
	injector = inject.Injector()
	injector.bind( "gmailAccount", to="do-not-reply@bitpostage.net" )
	injector.bind( "gmailPassword", to="this is another test password wrong" )

	inject.register( injector )

	gmail = GmailEmailMsg()
	temp = GmailEmailTemplate()

	assert_raises( SMTPAuthenticationError, gmail.sendMessage, "sean@bitpostage.net", "test message", temp.generate( "welcome_email.html", { "userName": "sean", "domain": "test.bitpostage.net", "userToken": "1234567890" } ) )

