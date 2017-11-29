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
       addFormParams(result['listColumn']);

     }

   });

  });
  function addFormParams(listColumn){

   var container = document.getElementById('form_predict');
   while (container.hasChildNodes()) {
     container.removeChild(container.lastChild);
   }

   for (i = 0; i < listColumn.length-1; i++) {
     var params = document.createElement("div");
     params.className="form-group";
     var divv= document.createElement("div");
     divv.className="col-sm-1";
     var div_input= document.createElement("div");
     div_input.className="col-sm-8";
     var input = document.createElement("input");
     input.name = "param"+i;
     input.className= "form-control";
     input.placeholder= "Enter params" +i;
     var label= document.createElement("Label");
     label.className="control-label col-sm-3"
     label.setAttribute("for", input);
     label.innerHTML = listColumn[i]+" :";
     div_input.appendChild(input);
     params.appendChild(label);
     params.appendChild(divv);
     params.appendChild(div_input);
     container.appendChild(params);


   }


 }

})
