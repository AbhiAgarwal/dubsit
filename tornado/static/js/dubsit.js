var search = []; // Search Array
      search.push('gif');
      var categories = ['web', 'image', 'gif'];
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
            $('#results').append('<div id="gif_division"><section id="id' + tag + '"><div id="h2' + tag + '"><h2>' + tag + '</h2></div><ul id=' + tag + '>');
            $.getJSON( "api/gif/rank/" + tag + ".json", function(data){
              if($.isEmptyObject(data)){$("#h2" + tag).html('<h2>' + tag + ': Nothing found</h2>');}
              $.each(data, function(i, field){
                var html_img = '<li>';
                html_img += '<img data-original="' + field.media_url + '" src="' + field.media_url + '" width="240" height="150" />'
                html_img += '</li>'
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
            analysis(tag); 
          }
        }
      }
      // Remove Tag from Array
      function onRemoveTag(tag) {
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