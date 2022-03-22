let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let download_link = document.querySelector("#download-video");

let camera_stream = null;
let media_recorder = null;
let blobs_recorded = [];

camera_button.addEventListener('click', async function() {
   	camera_stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
	video.srcObject = camera_stream;
});


start_button.addEventListener('click', function() {
    
    // set MIME type of recording as video/webm
    media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/webm' });

    // event : new recorded video blob available 
    media_recorder.addEventListener('dataavailable', function(e) {
		blobs_recorded.push(e.data);
    });

    // event : recording stopped & all blobs sent
    media_recorder.addEventListener('stop', function() {
    	// create local object URL from the recorded video blobs
    	let video_local = URL.createObjectURL(new Blob(blobs_recorded, { type: 'video/webm' }));
        var v = document.getElementById("videoup");
        v.value=video_local;
    });

    // start recording with each recorded blob having 1 second video
    media_recorder.start(1000);
    
    setTimeout(() => {
        media_recorder.stop();
        camera_stream.getTracks().forEach(track => track.stop());
        var vid = document.getElementById("video");
        vid.style.display="none";
        var sub = document.getElementById("hid");
        sub.style.display= "block";
        var h1 = document.getElementById("start-camera");
        h1.style.display="none";
        var h2 = document.getElementById("start-record");
        h2.style.display="none";
    }, 4000);
});
