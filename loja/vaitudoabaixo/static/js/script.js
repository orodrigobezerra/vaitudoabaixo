function toggleMenu(event) {
  console.log("Função toggleMenu chamada");
  var menu = document.getElementById("menu");
  var logo = document.querySelector(".logo-header");
  if (event.type === "mouseover") {
    menu.style.display = "block";
    logo.src = "/static/images/VaiTudoAbaixo-LOGO-WTEXT.png";
    logo.style.width = "150px";
    logo.style.marginTop = "20px";
    logo.style.marginBottom = "20px";
    logo.style.marginLeft = "20px";
  } else if (event.type === "mouseout") {
    menu.style.display = "none";
    logo.src = "/static/images/VaiTudoAbaixo-LOGO-white.png";
    logo.style.width = "50%";
    logo.style.marginTop = "0";
    logo.style.marginBottom = "0";
  }
}

function toggleSubMenu(subMenuId) {
    var subMenu = document.getElementById(subMenuId);

    // Oculta todos os submenus
    var allSubMenus = document.querySelectorAll('.submenu');
    allSubMenus.forEach(function (menu) {
        menu.style.display = 'none';
    });

    // Exibe ou oculta o submenu atual com base no estado atual
    if (subMenu.style.display === 'none') {
        subMenu.style.display = 'block';
    } else {
        subMenu.style.display = 'none';
    }
}

// Adiciona um manipulador de eventos mouseout para recolher os submenus quando o mouse sai do elemento pai
document.addEventListener('mouseout', function (event) {
    var allSubMenus = document.querySelectorAll('.submenu');
    allSubMenus.forEach(function (menu) {
        // Verifica se o mouse está realmente saindo do elemento pai ou do submenu
        if (!menu.contains(event.relatedTarget)) {
            menu.style.display = 'none';
        }
    });
});
