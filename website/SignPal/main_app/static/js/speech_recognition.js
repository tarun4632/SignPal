document.addEventListener('DOMContentLoaded', function() {
    const micButton = document.getElementById('mic-button');
    const speechText = document.getElementById('speech-text');

    if ('webkitSpeechRecognition' in window) {
        const recognition = new webkitSpeechRecognition();
        recognition.continuous = false;
        recognition.interimResults = false;

        recognition.onresult = function(event) {
            const result = event.results[0][0].transcript;
            speechText.value = result;
        };

        recognition.onerror = function(event) {
            console.error('Speech recognition error:', event.error);
        };

        micButton.addEventListener('click', function() {
            recognition.start();
        });
    } else {
        micButton.style.display = 'none';
        speechText.value = 'Speech recognition is not supported in this browser.';
    }
});