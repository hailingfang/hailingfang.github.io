function change_css_to_cv() {
    const my_css_link = document.querySelector("#about-me-css");
    my_css_link.setAttribute("href", "css/about-me-cv.css");
    const my_photo = document.querySelector("#myphoto img");
    my_photo.setAttribute("src", "imgs/fanghl_1inch.jpg");
}


let print_cv_but = document.getElementById("print-cv-button");
print_cv_but.addEventListener("click", change_css_to_cv);