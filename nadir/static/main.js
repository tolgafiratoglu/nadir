$(document).ready(
    function(){
        
        function initWebsocket (taskList) {
            let url = "ws://" + window.location.host + "/ws/socket-server/"

            const socket = new WebSocket(url)

            socket.onopen = function () {
                console.log('init websocket')
                socket.send(taskList)
            }

            socket.onmessage = function(e){
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
                        initWebsocket(data)
                    },
                    cache: false,
                    contentType: false,
                    processData: false
                });
            }
        );

    }
);