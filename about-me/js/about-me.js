function change_css_to_cv() {
    const my_css_link = document.querySelector("#about-me-css");
    my_css_link.setAttribute("href", "/about-me/css/about-me-cv.css");
    const my_photo = document.querySelector("#myphoto img");
    my_photo.setAttribute("src", "imgs/fanghl_1inch.jpg");
    const tilte = document.querySelector("head title");
    tilte.textContent = "CV-Benjami-Fang";
    let page_url = window.location.href;
    // change css when in Chinese
    if (page_url.match(/.*about-me-cn.html$/g)) {
        cv_entry = document.querySelector(".cv-entry-expand");
        cv_entry = document.getElementsByClassName("cv-entry-expand");
        for (let i = 0; i < cv_entry.length; i++) {

            cv_entry[i].style.gridTemplateColumns="30% 40% 30%";
        }
    }
}


function change_css_to_resume() {
    const my_css_link = document.querySelector("#about-me-css");
    my_css_link.setAttribute("href", "/about-me/css/about-me-resume.css");
    const my_photo = document.querySelector("#myphoto img");
    my_photo.setAttribute("src", "imgs/fanghl_1inch.jpg");
    const tilte = document.querySelector("head title");
    tilte.textContent = "resume-Benjami-Fang";
    let page_url = window.location.href;
    // change css when in Chinese
    if (page_url.match(/.*about-me-cn.html/g)) {
        cv_entry = document.getElementsByClassName("cv-entry-expand");
        for (let i = 0; i < cv_entry.length; i++) {

            cv_entry[i].style.gridTemplateColumns="30% 40% 30%";
        }

    }
}


let print_cv_but = document.getElementById("print-cv-button");
print_cv_but.addEventListener("click", change_css_to_cv);
let print_resume_but = document.getElementById("print-resume-button");
print_resume_but.addEventListener("click", change_css_to_resume);

