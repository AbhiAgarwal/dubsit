var search = []; // Search Array
var categories = ['web', 'image', 'gif', 'news'];
var prevType = "";

$(document).ready(function(){
  if(search.length > 1){
    analysis(search[1]);
  }
});

function addType(tag) {
  History.pushState({state: tag}, "Dubsit", ("?type=" + tag));
}
function addSearch(tag) {
  History.pushState({state: tag}, "Dubsit", ("?type=" + prevType + "&search=" + tag));
}

// Analysis of either image, web or gif etc:
function analysis(tag){
  if($.inArray(tag, categories) == 0){console.log(tag);}
  else{
  // 'web'
    if($.inArray(categories[0], search) != -1){ // == 0 means is present
      console.log('web');
    }
    // 'image'
    if($.inArray(categories[1], search) != -1){
      console.log('image');
    }
    // 'gif'
    if($.inArray(categories[2], search) != -1){
      // appending results
      $('#results').append('<div id="gif_division"><section id="id' + tag + '"><div id="h2' + tag + '"><h2>' + tag + '</h2></div><ul id=' + tag + '>');
      $.getJSON( "api/gif/rank/" + tag + ".json", function(data){
        if($.isEmptyObject(data)){$("#h2" + tag).html('<h2>' + tag + ': Nothing found</h2>');}
        else{
          $.each(data, function(i, field){
            // to check if image exists
            $("<img src=" + field.media_url +  ">").load(function(){
              // if exists then adds it to the GIF layer :)
              var html_img = '<li>';
              html_img += '<img data-original="' + field.media_url + '" src="' + field.media_url + '" width="240" height="150" />'
              html_img += '</li>'
              $("#" + tag).append(html_img);
            });
          });
        }
      });
      $('#results').append('</ul></section></div>');
      $("#" + tag).least();
      $("#h2" + tag).click(function(){
        $("#" + tag).toggle();
      });
    }
    // 'news'
    if($.inArray(categories[3], search) != -1){
      $('#results').append('<div id="news_division"><section id="id' + tag + '"><div id="h2' + tag + '"><h2>' + tag + '</h2></div><ul id=' + tag + '>');
      $.getJSON( "api/news/rank/" + tag + ".json", function(data){
        if($.isEmptyObject(data)){$("#h2" + tag).html('<h2>' + tag + ': Nothing found</h2>');}
          $.each(data, function(i, field){
            var html_img = '';
            html_img += '<a data-original="' + field.url + '" href="' + field.url + '" target="_news">'
            html_img += field.title
            html_img += '</a>'
            html_img += ''
            html_img += '<br>'
            $("#" + tag).append(html_img);
          });      
      });
      $('#results').append('</ul></section></div>');
      $("#" + tag).least();
      $("#h2" + tag).click(function(){
        $("#" + tag).toggle();
      }); 
    }
  }
}

// Adds Tag to Search
function onAddTag(tag){
  if(typeof(tag) != 'undefined'){
    search.push(tag);
    if($.inArray(tag, categories) == -1){
      addSearch(tag);
      analysis(tag); 
    } else {
      addType(tag);
      prevType = tag;
    }
  }
}

// Remove Tag from Array
function onRemoveTag(tag) {
  History.pushState({state: tag}, "Dubsit", ("?type=" + prevType));
  var index = search.indexOf(tag);
  if (search.length == 0){ 
    search = [];
    $('#results').remove(); 
    $('#h2' + tag).remove();
    $('#id' + tag).remove();
    $('#' + tag).remove();
  }
  if (search.length == 1){ 
    search = [];
    History.pushState({state: tag}, "Dubsit", "?");
    prevType = ""
    $('#h2' + tag).remove();
    $('#id' + tag).remove();
    $('#' + tag).remove();
  }
  else if (index > -1) { 
    $('#h2' + tag).remove();
    $('#id' + tag).remove();
    $('#' + tag).remove();
    search.splice(index, 1);
  }
}

// Supposed to find the Tag (Autocomplete)
function onChange(tag){
  var languages = ['gif','image','web'];
  $('.tag', tag).each(function(){
    if($(this).text().search(new RegExp('\\b(' + languages.join('|') + ')\\b')) >= 0)
      $(this).css('background-color', 'yellow');
  });
}

// Initializes the Search Bar
$(function() {
  $('#tags_1').tagsInput({
    width: 'auto',
    onRemoveTag: onRemoveTag,
    onAddTag: onAddTag,
    onChange: onChange,
  });                
});  