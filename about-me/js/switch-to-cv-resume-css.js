function change_css_to_cv() {
    const my_css_link = document.querySelector("#about-me-css");
    my_css_link.setAttribute("href", "./css/about-me-cv.css");
    const my_photo = document.querySelector(".contact-right img");
    my_photo.setAttribute("src", "./imgs/fanghl_1inch.jpg");
    my_photo.setAttribute("width", "344")
    my_photo.setAttribute("height", "397")
    const tilte = document.querySelector("head title");
    tilte.textContent = "CV-Hailing-Fang";
    let page_url = window.location.href;
}


function change_css_to_resume() {
    const my_css_link = document.querySelector("#about-me-css");
    my_css_link.setAttribute("href", "./css/about-me-resume.css");
    const my_photo = document.querySelector(".contact-right img");
    my_photo.setAttribute("src", "./imgs/fanghl_1inch.jpg");
    my_photo.setAttribute("width", "344")
    my_photo.setAttribute("height", "397")
    const tilte = document.querySelector("head title");
    tilte.textContent = "resume-Hailing-Fang";
}


let print_cv_but = document.getElementById("print-cv");
print_cv_but.addEventListener("click", change_css_to_cv);
let print_resume_but = document.getElementById("print-resume");
print_resume_but.addEventListener("click", change_css_to_resume);

