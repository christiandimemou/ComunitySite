document.addEventListener("DOMContentLoaded", function () {

    const header = document.querySelector(".site-header");
    const toggle = document.getElementById("navbarToggle");
    const menu = document.getElementById("navbarMenu");


    /* =====================================================
       NAVBAR AU SCROLL
       ===================================================== */

    function handleScroll() {

        if (window.scrollY > 30) {

            header.classList.add("scrolled");

        } else {

            header.classList.remove("scrolled");

        }

    }


    window.addEventListener("scroll", handleScroll);

    handleScroll();


    /* =====================================================
       MENU MOBILE
       ===================================================== */

    if (toggle && menu) {

        toggle.addEventListener("click", function () {

            menu.classList.toggle("open");

            toggle.classList.toggle("active");

        });


        /* Fermer le menu après clic */

        const links = menu.querySelectorAll("a");

        links.forEach(function (link) {

            link.addEventListener("click", function () {

                menu.classList.remove("open");

                toggle.classList.remove("active");

            });

        });

    }

});


/* =====================================================
   FOOTER - ACCORDÉON MOBILE
   ===================================================== */

   document.addEventListener("DOMContentLoaded", function () {

    const footerColumns =
        document.querySelectorAll(".footer-column");


    footerColumns.forEach(function (column) {

        const button =
            column.querySelector(".footer-column-title");


        if (!button) {
            return;
        }


        button.addEventListener("click", function () {

            if (window.innerWidth <= 700) {

                column.classList.toggle("open");

            }

        });

    });

});