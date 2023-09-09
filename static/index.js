document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("qr-form");
    var textInput = document.getElementById("text");
    var qrCodeContainer = document.getElementById("qr-code-container");
    var qrCodeImage = document.getElementById("qr-code-image");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        var text = textInput.value;

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/generate_qr", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var imgData = xhr.responseText;
                qrCodeImage.src = 'data:image/png;base64,' + imgData;
                qrCodeContainer.style.display = "block";
            }
        };
        xhr.send("text=" + encodeURIComponent(text));
    });
});