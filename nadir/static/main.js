$(document).ready(
    function(){
        
        function initWebsocket () {
            let url = "ws://" + window.location.host + "/ws/socket-server/"

            const socket = new WebSocket(url)

            console.log('websocket initialized')

            socket.onmessage = function(e){
                console.log('message recieved')
                let data = JSON.parse(e.data)
                console.log(data)
            }
        }

        $("#proceed_button").click(
            function(){
                var formData = new FormData();
                formData.append('file', $('#data_form')[0].files[0]);
                console.log(formData);
                
                $.ajax({
                    url : '/calculate',
                    type: 'POST',
                    data: formData,
                    async: false,
                    success: function (data) {
                        console.log(data)
                        initWebsocket()
                    },
                    cache: false,
                    contentType: false,
                    processData: false
                });
            }
        );

    }
);