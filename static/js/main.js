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


/* =====================================================
   HERO — SLIDER DOTS
   ===================================================== */

   document.addEventListener("DOMContentLoaded", function () {

    const dots = document.querySelectorAll(".hero-dot");


    dots.forEach(function (dot) {

        dot.addEventListener("click", function () {

            dots.forEach(function (item) {

                item.classList.remove("active");

            });


            dot.classList.add("active");

        });

    });

});


/* =====================================================
   COM'UNITY — ÉQUIPE
   CARROUSEL DES MEMBRES
   ===================================================== */

   document.addEventListener("DOMContentLoaded", function () {

    const members = document.querySelectorAll(".team-member");

    const previousButton =
        document.querySelector(".team-prev");

    const nextButton =
        document.querySelector(".team-next");

    const currentCounter =
        document.querySelector(".team-current");


    if (
        !members.length ||
        !previousButton ||
        !nextButton
    ) {
        return;
    }


    let currentIndex = 0;


    function showMember(index) {

        members.forEach(function (member) {

            member.classList.remove("active");

        });


        members[index].classList.add("active");


        if (currentCounter) {

            currentCounter.textContent = index + 1;

        }

    }


    previousButton.addEventListener(
        "click",
        function () {

            currentIndex--;

            if (currentIndex < 0) {

                currentIndex = members.length - 1;

            }

            showMember(currentIndex);

        }
    );


    nextButton.addEventListener(
        "click",
        function () {

            currentIndex++;

            if (currentIndex >= members.length) {

                currentIndex = 0;

            }

            showMember(currentIndex);

        }
    );

});