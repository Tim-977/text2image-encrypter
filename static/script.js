function updateButtonStatus() {
    const fileInput = document.getElementById('fileInput');
    const uploadButton = document.getElementById('uploadButton');

    if (fileInput.value) {
        uploadButton.disabled = false;
    } else {
        uploadButton.disabled = true;
    }
}
