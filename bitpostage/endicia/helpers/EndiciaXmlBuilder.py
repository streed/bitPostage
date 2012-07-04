from lxml.builder import E

class InvalidLabelValueError( Exception ):
	def __init__( self, value ):
		self.value = value
	
	def __str__( self ):
		return repr( "The value \"%s\" was not valid for this Label type" % ( self.value ) )

class EndiciaXmlBuilder:
	def __init__( self ):
		pass
	def to_string( self ):
		pass
	def to_hash( self ):
		pass
	def to_json( self ):
		pass

class LabelXmlBuilder( EndiciaXmlBuilder ):

	xml = {}
	
	def __init__( self ):
		EndiciaXmlBuilder.__init__( self)	
	
	def setTest( self ):
		self.xml['Test'] = "Yes"
	
	def setLabelType( self, _type ):
		if _type in [ "Default", "CertifiedMail", "DestinationConfirm", "Domestic", "International" ]:
			self.xml["LabelType"] = _type
		else:
			raise InvalidLabelValueError( _type )

	def setLabelSubType( self, subType ):
		if subType in [ "Integrated", "None" ]:
			self.xml["LabelSubType"] = subType
		else:
			raise InvalidLabelValueError( subType )

	def setLabelSize( self, size ):
		if size in [ "4x6", "4x5", "4x4.5" ]:
			self.xml["LabelSize"] = size
		else:
			raise InvalidLabelValueError( size )

	def setImageFormat( self, _format ):
		if _format in [ "GIF", "JPEG", "PDF", "PNG" ]:
			self.xml["ImageFormat"] = _format
		else:
			raise InvalidLabelValueError( _format )

	def setImageResolution( self, resolution ):
		if resolution in [ "203", "300" ]:
			self.xml["ImageResolution"] = resolution
		else:
			raise InvalidLabelValueError( resolution )

	def setRequestID( self, _id ):
		self.xml["RequesterID"] = _id

	def setAccountID( self, _id ):
		self.xml["AccountID"] = _id

	def setPassPhrase( self, passphrase ):
		self.xml["PassPhrase"] = passphrase

	def setMailClass( self, mailclass ):
		if mailclass in [ "Express", "First", "LibraryMail", "MediaMail", "ParcelPost", "ParcelSelect", "Priority", "CriticalMail",
					"StandardMail", "ExpressMailInternational", "FirstClassMailInternational", "PriorityMailInternational", "GXG" ]:
			self.xml["MailClass"] = mailclass
		else:
			raise InvalidLabelValueError( mailclass )

	def setDateAdvance( self, dateadvance ):
		if dateadvance >= 0 and dateadvance <= 7:
			self.xml["DateAdvance"] = dateadvance
		else:
			raise InvalidLabelValueError( dateadvance )

	def setWeightOunces( self, ounces ):
		self.xml["WeightOz"] = ounces	

	#TODO: Add the other mail piece shapes
	def setMailPieceShape( self, shape ):
		if shape in [ "Card", "Letter", "Flat", "Parcel", "LargeParcel", "IrregularParcel" ]:
			self.xml["MailpieceShape"] = shape
		else:
			raise InvalidLabelValueError( shape )

	def setDimensions( self, dimensions ):
		if len( dimensions ) == 3:
			self.xml["MailpieceDimensions"] = LabelDimensionsHelper( dimensions )
		else:
			raise TypeError( "Expected a 3-tuple for the mail dimensions" )

	def setShipDate( self, dateStr ):
		self.xml["ShipDate"] = dateStr

	def setShipTime( self, timeStr ):
		self.xml["ShipTime"] = timeStr

	def setIncludePostage( self, val ):
		self.xml["IncludePostage"] = val

	
	def to_xml( self ):
		self.xmlString = (
			E.LabelRequest(
				E.Test( self.xml["Test"] ),
				E.LabelType( self.xml["LabelType"] ),
				E.LabelSubType( self.xml["LabelSubType"] ),
				E.LabelSize( self.xml["LabelSize"] ),
				E.ImageFormat( self.xml["ImageFormat"] ),
				E.ImageResolution( self.xml["ImageResolution"] ),
				E.RequesterID( self.xml["RequesterID"] ),
				E.AccountID( self.xml["AccountID"] ),
				E.PassPhrase( self.xml["PassPhrase"] ),
				E.MailClass( self.xml["MailClass"] ),
				E.DateAdvance( str( self.xml["DateAdvance"] ) ),
				E.WeightOz( str( self.xml["WeightOz"] ) ),
				E.MailpieceShape( self.xml["MailpieceShape"] ),
				#E.MailPieceDimensions( self.xml["MailpieceDimensions"] )	
			)
		)

		return self.xmlString