require( [ "jquery", "ControlPanel/ControlPanel_c", "ControlPanel/ControlPanelModel", "backbone" ], function( $, template )
{
	var CPView = Backbone.View.extend({
		el: $("#control_panel"),
		render: function()
		{
			var self = this;
			dust.render( "ControlPanel", { username: "Testing" }, function( err, out )
			{
				console.log( out );
				self.el.html( out );
			});

		}
	});

	window.CPView = new CPView();

	window.CPView.render();
});
