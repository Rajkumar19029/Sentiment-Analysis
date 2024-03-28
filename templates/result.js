document.addEventListener("DOMContentLoaded", function() {

    var sentimentText = document.getElementById("sentimentText");
    
    var initialText = "{{ sentiment }}";
    sentimentText.textContent = initialText;

    animateText(initialText, "Positive", 0);
});

function animateText(initialText, finalText, index) {
    if (index >= finalText.length) return;
    var delay = 100;
    var sentimentText = document.getElementById("sentimentText");
    var currentText = initialText.slice(0, index) + finalText.charAt(index);
    sentimentText.textContent = currentText;
    setTimeout(function() {
        animateText(initialText, finalText, index + 1);
    }, delay);
}