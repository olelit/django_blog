let upload_images = document.querySelectorAll('.upload_field input');

upload_images.forEach((item) => {
    item.onchange = function (evt) {
        let tgt = evt.target || window.event.srcElement,
            files = tgt.files;
        if (FileReader && files && files.length) {
            let fr = new FileReader();
            fr.onload = function () {
                document.querySelector("img[data-upload="+evt.target.id+"]").src = fr.result;
            }
            fr.readAsDataURL(files[0]);
        } else {
        }
    }
});