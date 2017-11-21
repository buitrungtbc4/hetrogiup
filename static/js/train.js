$(document).ready(()=>{
  $('#train').on('click', function(){
      $.ajax({
        type: 'POST',
        url: '/train',
        data: '',
        contentType: false,
        cache: false,
        processData: false,
        success: function(result) {
             $("#theta").text( "Trọng số : " + result['theta']);
             $("#mean").text( "Trung bình : " + result['mu']);
             $("#sigma").text( "Độ lệch chuẩn : " + result['sigma']);
         }
    });

  })

})