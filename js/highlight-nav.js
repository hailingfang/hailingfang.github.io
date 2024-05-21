let url_page = window.location.href;

if ((url_page).match(/index.html/g)) {
    let nav = document.getElementById("home");
    nav.style.backgroundColor="#636363";
} else if ((url_page).match(/about-me.html/g)) {
    let nav = document.getElementById("about-me");
    nav.style.backgroundColor="#636363";
} else if ((url_page).match(/study.html/g)) {
    let nav = document.getElementById("study");
    nav.style.backgroundColor="#636363";
} else if ((url_page).match(/life.html/g)) {
    let nav = document.getElementById("life");
    nav.style.backgroundColor="#636363";
}

