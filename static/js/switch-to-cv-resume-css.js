function change_css_to_cv() {
    const my_css_link = document.querySelector("#about-me-css");
    my_css_link.setAttribute("href", "/static/css/about-me-cv.css");
    const tilte = document.querySelector("head title");
    tilte.textContent = "CV-Hailing-Fang";
}


function change_css_to_resume() {
    const my_css_link = document.querySelector("#about-me-css");
    my_css_link.setAttribute("href", "/static/css/about-me-resume.css");
    const tilte = document.querySelector("head title");
    tilte.textContent = "resume-Hailing-Fang";
}


let print_cv_but = document.getElementById("print-cv");
print_cv_but.addEventListener("click", change_css_to_cv);
let print_resume_but = document.getElementById("print-resume");
print_resume_but.addEventListener("click", change_css_to_resume);

