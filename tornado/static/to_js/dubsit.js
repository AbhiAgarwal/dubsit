function addType(e){History.pushState({state:e},"Dubsit","?type="+e)}function addSearch(e){History.pushState({state:e},"Dubsit","?type="+prevType+"&search="+e)}function analysis(e){if(e=="welcome"&&search.length==1&&prevType==""){$("#results").append('<div id="welcome_division"><section id="id'+e+'"><div id="h2'+e+'"><h2>'+e+"</h2></div><ul id="+e+">");$("#results").append("</ul></section></div>");$("#"+e).least();$("#h2"+e).click(function(){$("#"+e).toggle()})}if($.inArray(e,categories)==0){console.log(e)}else{if($.inArray(categories[0],search)!=-1){console.log("web")}if($.inArray(categories[1],search)!=-1){console.log("image")}if($.inArray(categories[2],search)!=-1){$("#results").append('<div id="gif_division"><section id="id'+e+'"><div id="h2'+e+'"><h2>'+e+'</h2></div><ul id="'+e+'">');$.getJSON("api/gif/rank/"+e+".json",function(t){if($.isEmptyObject(t)){$("#h2"+e).html("<h2>"+e+": Nothing found</h2>")}else{$.each(t,function(t,n){var r=n.media_url.split(".com")[1];if(!($.inArray(r,urlsVisited)!=-1)){$("<img src="+n.media_url+">").load(function(){var t="<li>";t+='<img data-original="'+n.media_url+'" src="'+n.media_url+'" width="240" height="150" />';t+="</li>";$("#"+e).append(t)})}urlsVisited.push(r)})}});$("#results").append("</ul></section></div>");$("#h2"+e).click(function(){$("#"+e).toggle()});$("#"+e).least()}if($.inArray(categories[3],search)!=-1){$("#results").append('<div id="news_division"><section id="id'+e+'"><div id="h2'+e+'"><h2>'+e+"</h2></div><ul id="+e+">");$.getJSON("api/news/rank/"+e+".json",function(t){if($.isEmptyObject(t)){$("#h2"+e).html("<h2>"+e+": Nothing found</h2>")}$.each(t,function(t,n){var r="";r+='<a data-original="'+n.url+'" href="'+n.url+'" target="_news">';r+=n.title;r+="</a>";r+="";r+="<br>";$("#"+e).append(r)})});$("#results").append("</ul></section></div>");$("#"+e).least();$("#h2"+e).click(function(){$("#"+e).toggle()})}}}function onAddTag(e){if(typeof e!="undefined"){search.push(e);if($.inArray(e,categories)==-1){addSearch(e);analysis(e)}else{addType(e);prevType=e}}}function onRemoveTag(e){History.pushState({state:e},"Dubsit","?type="+prevType);var t=search.indexOf(e);if(search.length==0){search=[];$("#results").remove();$("#h2"+e).remove();$("#id"+e).remove();$("#"+e).remove()}if(search.length==1){search=[];History.pushState({state:e},"Dubsit","?");prevType="";$("#h2"+e).remove();$("#id"+e).remove();$("#"+e).remove()}else if(t>-1){$("#h2"+e).remove();$("#id"+e).remove();$("#"+e).remove();search.splice(t,1)}}var search=[];var categories=["web","image","gif","news"];var prevType="";var urlsVisited=[];$(document).ready(function(){if(search.length>1){analysis(search[1])}});$(function(){$("#tags_1").tagsInput({width:"auto",onRemoveTag:onRemoveTag,onAddTag:onAddTag})})