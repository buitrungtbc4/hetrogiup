$(document).ready(()=> {
    $('#predict').on('click', function(){
        $.ajax({
          type: 'POST',
          url: '/predict',
          data: '',
          contentType: false,
          cache: false,
          processData: false,
          success: function(result) {
           $("#rs").text(result['name']);
     }

   });

  });


})