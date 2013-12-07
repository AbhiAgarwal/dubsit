var search = []; // Search Categories Array
var search_tag = []; // Tag Array
var urlsVisited = []; // URLS that you've visited
var categories = ['web', 'image', 'gif', 'news', 'chart', 'welcome']; // All categories you can use for the array

// Perform analysis
$(document).ready(function() {
  if(search.length > 1){
    analysis(search[1]);
  }
});

// Support Functions

// Capitalize the First Letter
String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

// Analytics of the Bar

// GIF Function
function gif(tag) {
  var html_to_add = '<div id="gif_division">';
      html_to_add += '<section id="id' + tag + '" class="panel panel-default">';
      html_to_add += '<div id="h2' + tag + '" class="panel-heading">' + 'GIF: ' +  tag.capitalize() + '</div>';
      html_to_add += '<ul class="pager" id="' + tag + '-pagination"><li><a id="' + tag + '-previous" href="#">Previous</a></li> <li><a id="' + tag + '-next" href="#">Next</a></li></ul>';
      html_to_add += '<div class="panel-body">';
      html_to_add += '<ul id="' + tag + '">';
  $.getJSON( "api/gif/rank/" + tag + ".json", function(data) {
    if($.isEmptyObject(data)){
      $("#h2" + tag).html(tag + ': Nothing found');
    }
    $.each(data, function(i, field) {
      var splitData = ((field.media_url).split(".com"))[1];
      if(!($.inArray(splitData, urlsVisited) != -1)) {
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
  $("#h2" + tag).click(function() {
    $("#" + tag).toggle();
  });
  $(document).ready(function() {
    $('#' + tag).paginate({itemsPerPage: 15});
  });
}

// News Function
function news(tag) {
  var html_to_add = '<div id="news_division">';
      html_to_add += '<section id="id' + tag + '" class="panel panel-default">';
      html_to_add += '<div id="h2' + tag + '" class="panel-heading">' + 'News: ' + tag.capitalize() + '</div>';
      html_to_add += '<div class="panel-body">';
      html_to_add += '<ul id="' + tag + '" class="list-group">';
  $.getJSON( "api/news/rank/" + tag + ".json", function(data) {
    $.each(data, function(i, field) {
      var current_html = '<a href="' + field.url + '" class="list-group-item" target="_news">'
          current_html += '<span class="badge">14</span>';
          current_html += '<h4 class="list-group-item-heading">' + field.title + '</h4>';
          current_html += '</a>';
      $('#' + tag).append(current_html);
    });
  });
  html_to_add += '</ul></div></section></div>';
  $('#results').append(html_to_add);
  $("#h2" + tag).click(function() {
    $("#" + tag).toggle();
  });
}

// Chart Function
function chart(tag) {
  if(tag != 'news' && tag != 'gif') {
    var html_to_add = '<div id="chart_division">';
        html_to_add += '<section id="id' + tag + '" class="panel panel-default">';
        html_to_add += '<div id="h2' + tag + '" class="panel-heading">' + tag.capitalize() + ': Not Found</div>';
        html_to_add += '<div class="panel-body">';
        html_to_add += '</li></ul></div></section></div>';
    $('#results').append(html_to_add);
  } else {
    $.getScript("static/to_js/Chart.js", function() {
      var GraphLabels = [];
      var GraphData = [];
      var html_to_add = '<div id="chart_division">';
          html_to_add += '<section id="id' + tag + '" class="panel panel-default">';
          html_to_add += '<div id="h2' + tag + '" class="panel-heading">' + tag.capitalize() + ' Analytics</div>';
          html_to_add += '<div class="panel-body">';
          html_to_add += '<ul id="' + tag + '">';
          html_to_add += '<li>';
          html_to_add += '<canvas id="' + tag + '_analytics" width="600" height="400"></canvas>';
          html_to_add += '</li></ul></div></section></div>';
      $('#results').append(html_to_add);
      $.getJSON('api/graph/' + tag + '.json', function(data) {
        $.each(data, function(i, field){
          GraphLabels.push(field.name);
          GraphData.push(field.count);
        });
        var barChartData = {
          labels : GraphLabels,
          datasets : [
          { fillColor: "rgba(151,187,205,0.5)",
            strokeColor: "rgba(151,187,205,1)",
            data: GraphData
        }]}
        var myLine = new Chart(document.getElementById(tag + '_analytics').getContext("2d")).Bar(barChartData);
      });
    });
  }
}

// Welcome
function welcome(tag) {
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
}

// Analytics
function analysis(tag){
  tag = tag.toLowerCase();
  if($.inArray(categories[0], search_tag) != -1) {
    console.log(tag);
  }
  if($.inArray(categories[1], search_tag) != -1) {
    console.log(tag);
  }
  if($.inArray(categories[2], search_tag) != -1) {
    gif(tag);
  }
  if($.inArray(categories[3], search_tag) != -1) {
    news(tag);
  }
  if($.inArray(categories[4], search_tag) != -1) {
    chart(tag);
  }
  if(($.inArray(categories[5], search_tag) != -1) && search.length == 0) {
    welcome(tag);
  }

}

// onError of Image

function imgError(image) {
  $(image).remove();
}

// URL Configuration

function addType(tag) {
  History.pushState({state: tag}, "Dubsit", ("?type=" + tag));
}

function addSearch(tag) {
  if(search_tag.length == 0){
    History.pushState({state: tag}, "Dubsit", ("?type=&search=" + tag));
  } else {
    History.pushState({state: tag}, "Dubsit", ("?type=" + search_tag[search_tag.length-1] + "&search=" + tag));
  }
}

// Tag Bar configuration

// Adds Tag to Search
function onAddTag(tag) {
  if(typeof(tag) != 'undefined'){
    // if the tag is NOT a category
    if($.inArray(tag, categories) == -1) {
      // push it into the tag array
      search.push(tag);
      // add the search to the URL
      addSearch(tag);
      analysis(tag);
    // if the tag IS a category
    } else {
      // to use chart you've to place it just before the tag
      // then this function would work
      if(search_tag[search_tag.length-1] == categories[4]){
        search.push(tag);
        addSearch(tag);
        analysis(tag);
      // special case when
      } else if(tag == categories[5]) {
        search_tag.push(tag);
        addType(tag);
        analysis(tag);

      } else {
        // push it into the category array
        search_tag.push(tag);
        // add the type to the URL
        addType(tag);
      }
    }
  }
}

// Reset the whole search bar
function resetDubsit() {
  // Sets the URL to static
  History.pushState({state: "removeAll"}, "Dubsit", "?");
  // Resets tag options at the top
  $('#tags_1').importTags('');
  // Goes through all the tag and empties them
  search.forEach(function(entry){
    onRemoveTag(entry);
  });
  // Reset both the search & search_tag arrays
  search = [];
  search_tag = [];
}

// Remove Tag from Array
function onRemoveTag(tag) {
  // Special Case Dealings:
  // 1. Chart ___, ____ needs to be a category deal with all the "CATEGORIES"
  if($.inArray(tag, categories) != -1 &&
    // dealing with special special case 1.
    !(search_tag[search_tag.length-1] == categories[4] && tag != 'chart')) {
    // set the URL to ?
    History.pushState({state: tag}, "Dubsit", "?");
    // remove the element from the array
    var index = search_tag.indexOf(tag);
    if (index > -1) {
      search_tag.splice(index, 1);
    }
    // remove the current TAG's division
    $('#' + tag.toLowerCase() + '_division').remove();
    // check to see if search_array is empty
    if(search_tag.length == 0) {
      search_tag = [];
      History.pushState({state: tag}, "Dubsit", "?");
      // remove the results
      // resets the list at the top
      $('#tags_1').importTags('');
    } else {
      History.pushState({state: tag}, "Dubsit", ("?type=" + search_tag[search_tag.length-1]));
      if(search.length != 0) {
        History.pushState({state: tag}, "Dubsit", ("?type=" + search_tag[search_tag.length-1] + "&search=" + search[search.length-1]));
      }
    }
  // now check through all the "TAGS"
  } else {
    // check if search array is empty
    if(search.length == 0) {
      search = [];
    } else { // else remove it
      var index = search.indexOf(tag);
      // remove the index from the array
      if (index > -1) {
        search.splice(index, 1);
      }
    }
    // remove the current from the div
    $('#h2' + tag).remove();
    $('#id' + tag).remove();
    $('#' + tag).remove();
    // Set the URL to be the last element in the search_tag array
    if(search_tag.length != 0) {
      // if there is an element before then add it to the URL
      if(search.length != 0) {
        History.pushState({state: tag}, "Dubsit", ("?type=" + search_tag[search_tag.length-1] + "&search=" + search[search.length-1]));
      } else {
        History.pushState({state: tag}, "Dubsit", ("?type=" + search_tag[search_tag.length-1]));
      }
    }
    // If no CATEGORY but has tag
    if(search_tag.length == 0){
      if(search.length != 0){
        History.pushState({state: tag}, "Dubsit", ("?type=&search=" + search[search.length-1]));
      } else {
        History.pushState({state: tag}, "Dubsit", ("?"));
      }
    }
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
