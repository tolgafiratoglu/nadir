$(document).ready(
    function(){
        
        $("#proceed_button").click(
            function(){
                var formData = new FormData();
                formData.append('file', $('#data_form')[0].files[0]);
                console.log(formData);
                
                $.ajax({
                    url : 'http://127.0.0.1:8000/calculate',
                    type: 'POST',
                    data: formData,
                    async: false,
                    success: function (data) {
                        console.log(data)
                    },
                    cache: false,
                    contentType: false,
                    processData: false
                });
            }
        );

    }
);