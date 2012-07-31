from nose.tools import assert_raises
from bitpostage.endicia.helpers.ChangePassPhraseXmlBuilder import ChangePassPhraseXmlBuilder
from bitpostage.endicia.helpers.EndiciaXmlBuilder import ValueToLongError

def test_ChangePassPhraseXmlBuilder_invalid_values():
	builder = ChangePassPhraseXmlBuilder()
	
	assert_raises( ValueToLongError, builder.setPartnerID, "123456789012345678901234567890123456789012345678901" )
	assert_raises( ValueToLongError, builder.setRequestID, "123456789012345678901234567890123456789012345678901" )
	assert_raises( ValueToLongError, builder.setAccountID, "1234567" )
	assert_raises( ValueToLongError, builder.setPassPhrase, "12345678901234567890123456789012345678901234567890123456789012345" )
