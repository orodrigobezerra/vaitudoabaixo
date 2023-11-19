function toggleMenu(event) {
    console.log("Função toggleMenu chamada");
    var menu = document.getElementById("menu");
    var logo = document.querySelector(".logo-header");
    if (event.type === "mouseover") {
        menu.style.display = "block";
        logo.src = "/static/images/VaiTudoAbaixo-LOGO-WTEXT.png";
        logo.style.width = '150px';
        logo.style.marginTop = "20px";
        logo.style.marginBottom = "20px";
    } else if (event.type === "mouseout") {
        menu.style.display = "none";
        logo.src = "/static/images/VaiTudoAbaixo-LOGO-white.png";
        logo.style.width = '60%';
        logo.style.marginTop = "0";
        logo.style.marginBottom = "0";
    }
}


