// now we seek to parse the URL
$(window).load(function() {
    var url = $.url();
	if(url.param('type') != undefined && url.param('search') != undefined){
		var typeQuery = url.param('type');
		var searchQuery = url.param('search');
		$('#tags_1').addTag(typeQuery);
		$('#tags_1').addTag(searchQuery);
	} else {
		$('#tags_1').addTag('gif');
	} 
});

// checking if the image contains an error
// if it does then remove it
function imgError(image){$(image).remove()}

// way to reset the dubsit controls
$('#navbar_Dubsit').click(function(){
	resetDubsit();
});