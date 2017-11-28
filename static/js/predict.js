$(document).ready(() => {

    function getFormData($form) {
        var array = $form.serializeArray();
        // var FD = new FormData();
        // FD.append('trung', 'dai ca');
        // for (i = 0; i < array.length; i++) {
        //     FD[array[i].name] = array[i].value;
        // }
        var object = {};
        for (i = 0; i < array.length; i++) {
            object[array[i].name] = array[i].value;
        }
        var json = JSON.stringify(object);
        return json;

    }

    $('#predict').on('click', function() {
        data = getFormData($("#form_predict"))
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: data,
            contentType: "application/json",
            success: function(result) {
                console.log(result);
                $("#rs").text(result);
            }

        });

    });

})