let url_page = window.location.href;
url_page = url_page.split("/");
let lang_but = document.querySelector("#lang-url");

if ((url_page[url_page.length - 1]).match(/^about-me.html$/g)) {
    url_page[url_page.length - 1] = "about-me-cn.html";
    url_page = url_page.join("/");
    lang_but.setAttribute("href", url_page);

} else if ((url_page[url_page.length - 1]).match(/^about-me-cn.html/g)) {

    url_page[url_page.length - 1] = "about-me.html";
    url_page = url_page.join("/");
    lang_but.setAttribute("href", url_page);

}