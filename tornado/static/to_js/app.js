$(window).load(function(){var url=$.url();if(url.param("type")!=undefined&&url.param("search")!=undefined){var typeQuery=url.param("type");var searchQuery=url.param("search");$("#tags_1").addTag(typeQuery);$("#tags_1").addTag(searchQuery)}else if(url.param("type")!=undefined){var typeQuery=url.param("type");$("#tags_1").addTag(typeQuery)}else if(url.param("search")!=undefined){var searchQuery=url.param("search");$("#tags_1").addTag(searchQuery)}else{$("#tags_1").addTag("gif")}});function imgError(image){$(image).remove()}$("#navbar_Dubsit").click(function(){resetDubsit()});