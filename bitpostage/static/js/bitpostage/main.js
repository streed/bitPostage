require( [ "jquery.validate", "jquery" ], function( jqueryValidator, $ )
{
	$(function()
	{

		$("#mtgox-wrapper" ).hide();

		$("#progress-usps").css( "width", (parseFloat( $("#progress-usps").css( "width" ) ) + 5 ) );
	
		$.validator.addMethod( "zipCode", function( v, e )
		{
			return /[0-9]{5}/.test( v );
		}, "Improper Zipcode format.");
	
		$('#bitpostage-address-form').validate(  
		{ 
			rules: 
			{
				email:{ required: true, email: true },
				first_name:{ required: true, minlength: 2 },
				last_name:{ required: true, minlength: 2 },
				address1:{ required: true, minlength: 2 },
				city:{ required: true, minlength: 2 },
				state:{ required: true, minlength: 2 },
				zip:{ required: true, zipCode: true },
				first_name_2:{ required: true, minlength: 2 },
				last_name_2:{ required: true, minlength: 2 },
				address1_2:{ required: true, minlength: 2 },
				city_2:{ required: true, minlength: 2 },
				state_2:{ required: true, minlength: 2 },
				zip_2:{ required: true, zipCode: true }
			},
			messages:
			{
				first_name: "Please enter in the receipient's first name.",
				last_name: "Please enter in the receipient's last name.",
				email: "Please enter a valid email address as this will be the only way to deliver your postage.",
				address1: "Please enter in the address you wish to send post to.",
				city: "Please enter in the destination's city.",
				state: "Please enter in the destination's state.",
				zip: "Please enter in a valid five digit zip code.",
				first_name_2: "Please enter in the return address's first name.",
				last_name_2: "Please enter in the return address's last name.",
				address1_2: "Please enter in the return address.",
				city_2: "Please enter in the return address's city.",
				state_2: "Please enter in the return address's state.",
				zip_2: "Please enter in a valid five digit zip code."
			}
		});	
	});
});
