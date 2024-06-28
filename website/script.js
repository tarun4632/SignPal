if ('webkitSpeechRecognition' in window) {
    const recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    document.getElementById('speakButton').addEventListener('click', () => {
        recognition.start();
    });

    recognition.onstart = function() {
        console.log('Speech recognition started');
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        console.log('Speech recognized: ' + transcript);
    };

    recognition.onerror = function(event) {
        console.error('Speech recognition error', event);
    };

    recognition.onend = function() {
        console.log('Speech recognition ended');
    };
} else {
    console.error('Web Speech API is not supported by this browser.');
}
