document.addEventListener('DOMContentLoaded', function() {
    const socket = io();

    function sendMessage() {
        console.log("Hello World")
        let message = document.getElementById('message');
        socket.emit('message',message)
    }

    document.getElementById("send").onclick(sendMessage())

    socket.on('message', function(data) {
        var messageDiv = document.createElement('div');
        messageDiv.textContent = data;
        document.getElementById('messages').appendChild(messageDiv);
    });
})