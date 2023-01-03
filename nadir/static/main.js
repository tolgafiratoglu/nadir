$(document).ready(
    function(){
        
        function initWebsocket () {
            let url = "ws://" + window.location.host + "/ws/socket-server/"

            const socket = new WebSocket(url)

            console.log('websocket initialized')

            socket.onmessage = function(e){
                let data = JSON.parse(e.data)
                console.log(data);
                if(data.type === 'task_results'){
                    for (var result in data.results['SUCCESS']) {
                        var processResult = '[' + data.results['SUCCESS'][result].toString() + ']'
                        $("#task_" + result+" .result-text").html(processResult);
                        $("#task_" + result+" .loading-icon").addClass('d-none');
                        $("#task_" + result+" .check-icon").removeClass('d-none');
                    }
                    for (var result in data.results['FAILURE']) {
                        $("#task_" + result+" .result-text").html('Task Failed');
                        $("#task_" + result+" .loading-icon").addClass('d-none');
                        $("#task_" + result+" .warning-icon").removeClass('d-none');
                    }    
                }
            }
        }

        function initWorkerStatus (data) {
            for(var key in data){
                $("#task_results").append('<div id="task_' + key + '" class="task-result"><h6>'+key+'</h6><div><i class="loading-icon fas fa-spinner fa-spin"></i><i class="d-none warning-icon fa fa-exclamation-triangle" aria-hidden="true"></i><i class="check-icon d-none fa fa-check" aria-hidden="true"></i><span class="result-text">Processing task: "celery-task-meta-' +data[key]+ '"</span></div></div>')
            }
        }

        $("#proceed_button").click(
            function(){
                var formData = new FormData();
                formData.append('file', $('#data_form')[0].files[0]);
                
                $.ajax({
                    url : '/calculate',
                    type: 'POST',
                    data: formData,
                    async: false,
                    success: function (data) {
                        initWorkerStatus(data)
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