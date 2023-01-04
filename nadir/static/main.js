$(document).ready(
    function(){
        
        function initWebsocket () {
            let url = "ws://" + window.location.host + "/ws/socket-server/"

            const socket = new WebSocket(url)

            socket.onmessage = function(e) {
                let data = JSON.parse(e.data)
                console.log(data, window.numOfTasks);
                
                if(data.type === 'task_results'){
                    if (window.numOfTasks === Object.keys(data.results['SUCCESS']).length) {
                        $('.show-after-upload').addClass('d-none')
                        socket.close()
                    }
                
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
            function () {
                $(".hide-after-action").addClass("d-none");
                $(".hide-after-upload").removeClass("d-none");
                
                var formData = new FormData();
                formData.append('file', $('#data_form')[0].files[0]);
                formData.append('ignore_first_row', $('#ignore_first_row').is(':checked'))
                
                setTimeout(
                    function () {
                        $.ajax({
                            url : '/calculate',
                            type: 'POST',
                            data: formData,
                            async: false,
                            success: function (data) {
                                window.numOfTasks = Object.keys(data).length
                                initWorkerStatus(data)
                                initWebsocket()
                                $(".show-after-upload").removeClass("d-none");
                                $('.no-workers').html(window.numOfTasks)
                                $(".hide-after-upload").addClass("d-none");
                            },
                            cache: false,
                            contentType: false,
                            processData: false
                        });
                    }, 1000
                )
            }
        );

    }
);