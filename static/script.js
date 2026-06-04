const fileInput = document.getElementById("fileInput");

if(fileInput){

    fileInput.addEventListener("change", function(){

    const file = this.files[0];

    if(file){

        document.getElementById("preview").src =
            URL.createObjectURL(file);

        document.getElementById("fileName").innerText =
            file.name;

    }

});

}

function upload() {

    const file = fileInput.files[0];

    if (!file) {
        alert("Please upload image");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("/predict", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {

        console.log("API Response:", data);

        document.getElementById("disease").innerText =
          data.class_lo;

        const conf = ((data.confidence || 0) * 100).toFixed(2);

        document.getElementById("confidence").innerText =
            conf + "%";

        const bar = document.getElementById("confidenceFill");

        if (bar) {
            bar.style.width = conf + "%";
        }

    })
    .catch(err => {

        console.error(err);
        alert("Prediction failed!");

    });
}

function showPage(pageId){

    document.getElementById("home").style.display = "none";
    document.getElementById("upload").style.display = "none";
    document.getElementById("how").style.display = "none";
    document.getElementById("contact").style.display = "none";

    if(pageId === "home"){
        document.getElementById("home").style.display = "flex";
    }else{
        document.getElementById(pageId).style.display = "flex";
    }
}

window.onload = function(){
    showPage("home");
};