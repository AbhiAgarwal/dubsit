$(window).load(function(){var e=$.url();if(e.param("type")!=undefined&&e.param("search")!=undefined){var t=e.param("type");var n=e.param("search");$("#tags_1").addTag(t);$("#tags_1").addTag(n)}else{$("#tags_1").addTag("gif")}})