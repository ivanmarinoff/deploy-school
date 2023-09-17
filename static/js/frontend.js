// frontend.js

const socket = new WebSocket('ws://localhost:8000/ws/live_video/');

const mediaSource = new MediaSource();
const video = document.getElementById('video');

mediaSource.addEventListener('sourceopen', () => {
    const sourceBuffer = mediaSource.addSourceBuffer('video/mp4; codecs="avc1.64001E"');

    socket.onmessage = (event) => {
        if (event.data instanceof Blob) {
            sourceBuffer.appendBuffer(event.data);
        }
    };
});

video.src = window.URL.createObjectURL(mediaSource);

const startButton = document.getElementById('startRecording');
const stopButton = document.getElementById('stopRecording');

startButton.addEventListener('click', () => {
    // Send a request to start recording
    fetch('/start_recording/')
        .then(response => {
            if (response.ok) {
                console.log('Recording started.');
            } else {
                console.error('Error starting recording.');
            }
        });
});

stopButton.addEventListener('click', () => {
    // Send a request to stop recording
    // Implement this part based on your application logic
});