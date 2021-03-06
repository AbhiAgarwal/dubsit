var search = []; // Search Array
var categories = ['web', 'image', 'gif', 'news'];
var prevType = "";
var urlsVisited = [];

$(document).ready(function(){
  if(search.length > 1){
    analysis(search[1]);
  }
});

function imgError(image){
    $(image).remove();
}

// Analysis of either image, web or gif etc:
function analysis(tag){
  // 'welcome'
  if(tag == 'welcome' && search.length == 1 && prevType == ""){
    // HTML to be added to the welcome
    var html_to_add = '<div id="welcome_division">';
    html_to_add += '<section id="id' + tag + '">';
    html_to_add += '<div id="h2' + tag + '"><h2>' + tag + '</h2></div>'
    html_to_add += '<ul id=' + tag + '>'
    html_to_add += '<li>heh</li>'
    html_to_add += '</ul></section></div>'
    // Adding the HTML & Checking Cache
    $('#results').append(html_to_add);
    $("#" + tag).least();
    // Create instance of a toggle
    $("#h2" + tag).click(function(){
      $("#" + tag).toggle();
    });
    // Stop execution
    return;
  }
  // not 'welcome'
  if($.inArray(tag, categories) == 0){}
  else{
    // 'web'
    if($.inArray(categories[0], search) != -1){
      console.log('web');
    }
    // 'image'
    if($.inArray(categories[1], search) != -1){
      console.log('image');
    }
    // 'gif'
    if($.inArray(categories[2], search) != -1){

      var html_to_add = '<div id="gif_division">';
      html_to_add += '<section id="id' + tag + '" class="panel panel-default">';
      html_to_add += '<div id="h2' + tag + '" class="panel-heading">' + tag + '</div>';
      html_to_add += '<ul class="pager" id="' + tag + '-pagination"><li><a id="' + tag + '-previous" href="#">Previous</a></li> <li><a id="' + tag + '-next" href="#">Next</a></li></ul>';
      html_to_add += '<div class="panel-body">';
      html_to_add += '<ul id="' + tag + '">';

      $.getJSON( "api/gif/rank/" + tag + ".json", function(data){

      if($.isEmptyObject(data)){
        $("#h2" + tag).html(tag + ': Nothing found');
      }

        $.each(data, function(i, field){
          var splitData = ((field.media_url).split(".com"))[1];

          if(!($.inArray(splitData, urlsVisited) != -1)){
            var current_html = '<li>'
            current_html += '<img src="' + field.media_url + '" data-src="' + field.media_url + '" alt="" width="240" height="180" onerror="imgError(this);">';
            current_html += '</a>';
            current_html += '</li>';

            $('#' + tag).append(current_html);
            $('#' + tag).paginate({itemsPerPage: 15});
          }
          urlsVisited.push(splitData);
        }); 

      });

      html_to_add += '</ul></div></section></div>';
      $('#results').append(html_to_add);
      $("#h2" + tag).click(function(){
        $("#" + tag).toggle();
      });

      $(document).ready(function() {
        $('#' + tag).paginate({itemsPerPage: 15});
      });
    }
    // 'news'
    if($.inArray(categories[3], search) != -1){
      
      var html_to_add = '<div id="news_division">';
      html_to_add += '<section id="id' + tag + '" class="panel panel-default">';
      html_to_add += '<div id="h2' + tag + '" class="panel-heading">' + tag + '</div>';
      html_to_add += '<div class="panel-body">';
      html_to_add += '<ul id="' + tag + '" class="list-group">';

      $.getJSON( "api/news/rank/" + tag + ".json", function(data){

        $.each(data, function(i, field){

          var current_html = '<a href="' + field.url + '" class="list-group-item" target="_news">'
          current_html += '<span class="badge">14</span>';
          current_html += '<h4 class="list-group-item-heading">' + field.title + '</h4>';
          current_html += '</a>';

          $('#' + tag).append(current_html);

          });      

      });

      html_to_add += '</ul></div></section></div>';
      $('#results').append(html_to_add);
      $("#h2" + tag).click(function(){
        $("#" + tag).toggle();
      });
    }
    // 'chart gif'
    if(tag == 'chart'){
      $.getScript("static/to_js/Chart.js", function(){
        var html_to_add = '<div id="chart_division">';
        html_to_add += '<section id="id' + tag + '" class="panel panel-default">';
        html_to_add += '<div id="h2' + tag + '" class="panel-heading">GIF Analytics</div>';
        html_to_add += '<div class="panel-body">';
        html_to_add += '<ul id="' + tag + '">';
        html_to_add += '<li>';
        html_to_add += '<canvas id="gif_analytics" width="600" height="400"></canvas>';
        html_to_add += '</li></ul></div></section></div>';
        $('#results').append(html_to_add);

        var GraphLabels = [];
        var GraphData = [];

        $.getJSON( "api/graph/GIF.json" + tag + ".json", function(data){
          $.each(data, function(i, field){
            GraphLabels.push(field.name);
            GraphData.push(field.count);
          }); 
          var barChartData = {
            labels : GraphLabels,
            datasets : [
            {
              fillColor : "rgba(151,187,205,0.5)",
              strokeColor : "rgba(151,187,205,1)",
              data : GraphData
            }
            ]                       
          }
          var myLine = new Chart(document.getElementById("gif_analytics").getContext("2d")).Bar(barChartData);
        });
      });
    }
  }
}

function addType(tag) {
  History.pushState({state: tag}, "Dubsit", ("?type=" + tag));
}
function addSearch(tag) {
  History.pushState({state: tag}, "Dubsit", ("?type=" + prevType + "&search=" + tag));
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

// Initializes the Search Bar
$(function() {
  $('#tags_1').tagsInput({
    width: 'auto',
    onRemoveTag: onRemoveTag,
    onAddTag: onAddTag,
  });                
});  