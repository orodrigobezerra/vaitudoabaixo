function toggleMenu(event) {
    var menu = document.getElementById("menu");
    var logo = document.getElementById("logo");

    if (event.type === "mouseover") {
        menu.style.display = "block";
        logo.src = "{% static 'images/VaiTudoAbaixo-LOGO-NOTEXT.png' %}";
    } else if (event.type === "mouseout") {
        menu.style.display = "none";
        logo.src = "{% static 'images/VaiTudoAbaixo-LOGO2.png' %}";
    }
}