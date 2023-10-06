console.log("Sanity check from index.js.");

// focus 'roomInput' when user opens the page
document.querySelector("#roomInput").focus();

// submit if the user presses the enter key
document.querySelector("#roomInput").onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter key
        document.querySelector("#roomConnect").click();
    }
};

// // redirect to '/room/<roomInput>/'
// document.querySelector("#roomConnect").onclick = function() {
//     let roomName = document.querySelector("#roomInput").value;
//     window.location.pathname = window.location.host + roomName + "/";
// }

// redirect to '/room/<roomSelect>/'
// document.querySelector("#roomSelect").onchange = function() {
//     let roomName = document.querySelector("#roomSelect").value.split(" (")[0];
//     window.location.pathname = window.location.host + roomName + "/";
// }

// document.querySelector("#roomSelect").addEventListener("change", function () {
//     const selectedRoom = this.value;
//     if (selectedRoom) {
//         window.location.pathname = window.location.host + selectedRoom + "/";
//     }
// });

// Assuming you have an event listener for the "Live Stream" button
document.querySelector('#roomConnect').addEventListener('click', function () {
    // Trigger a click event on the "Join the General Room" link
    document.querySelector('#joinGeneralRoom').click();
});