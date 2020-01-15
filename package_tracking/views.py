from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    response = """
<h1>Register Package</h1>
<video id="player" autoplay></video>
<button id="capture"><img width="128px" src="data:image/png;base64,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"></button>
<canvas id="canvas" width=320 height=240></canvas>
<script>
  const player = document.getElementById('player');
  const canvas = document.getElementById('canvas');
  const context = canvas.getContext('2d');
  const captureButton = document.getElementById('capture');

  const constraints = {
    video: true,
  };

  captureButton.addEventListener('click', () => {
    //player.srcObject.getVideoTracks().forEach(track => track.start());
    // Draw the video frame to the canvas.
    context.drawImage(player, 0, 0, canvas.width, canvas.height);

    // Stop all video streams.
    player.srcObject.getVideoTracks().forEach(track => track.stop());
  });

  // Attach the video stream to the video element and autoplay.
  navigator.mediaDevices.getUserMedia(constraints)
    .then((stream) => {
      player.srcObject = stream;
    });

  function sendPic() {
    var imgSrc = canvas.toDataURL();

    // Send file here either by adding it to a `FormData` object 
    // and sending that via XHR, or by simply passing the file into 
    // the `send` method of an XHR instance.
  }
  captureButton.addEventListener('click', sendPic, false);
</script>
    """
    return HttpResponse(response)
