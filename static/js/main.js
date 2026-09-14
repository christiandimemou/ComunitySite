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


document.addEventListener("DOMContentLoaded", function () {

    const faqItems = document.querySelectorAll(".faq-item");

    faqItems.forEach(function (item) {

        const question = item.querySelector(".faq-question");

        if (!question) {
            return;
        }

        question.addEventListener("click", function () {

            const isOpen = item.classList.contains("open");

            /*
             * Fermer toutes les questions
             */
            faqItems.forEach(function (otherItem) {

                otherItem.classList.remove("open");

                const otherQuestion =
                    otherItem.querySelector(".faq-question");

                if (otherQuestion) {
                    otherQuestion.setAttribute(
                        "aria-expanded",
                        "false"
                    );
                }

            });


            /*
             * Si la question cliquée était fermée,
             * on l'ouvre.
             */
            if (!isOpen) {

                item.classList.add("open");

                question.setAttribute(
                    "aria-expanded",
                    "true"
                );

            }

        });

    });

});


/* =====================================================
   NAVIGATION RAPIDE — HAUT / BAS
===================================================== */

const scrollUp = document.getElementById("scrollUp");
const scrollDown = document.getElementById("scrollDown");


if (scrollUp) {

    scrollUp.addEventListener("click", function () {

        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });

    });

}


if (scrollDown) {

    scrollDown.addEventListener("click", function () {

        window.scrollTo({
            top: document.documentElement.scrollHeight,
            behavior: "smooth"
        });

    });

}


/* =====================================================
   GESTION DU CONSENTEMENT COOKIES
===================================================== */

document.addEventListener("DOMContentLoaded", function () {

    const cookieBanner =
        document.getElementById("cookieBanner");

    const cookieSettingsPanel =
        document.getElementById("cookieSettingsPanel");

    const cookieAccept =
        document.getElementById("cookieAccept");

    const cookieRefuse =
        document.getElementById("cookieRefuse");

    const cookieSettings =
        document.getElementById("cookieSettings");

    const cookieSettingsClose =
        document.getElementById("cookieSettingsClose");

    const cookieSettingsRefuse =
        document.getElementById("cookieSettingsRefuse");

    const cookieSettingsSave =
        document.getElementById("cookieSettingsSave");


    /* -------------------------------------------------
       AFFICHAGE DU BANDEAU
    ------------------------------------------------- */

    const savedConsent =
        localStorage.getItem("comunity_cookie_consent");


    if (!savedConsent && cookieBanner) {

        setTimeout(function () {

            cookieBanner.classList.add("visible");

        }, 500);

    }


    /* -------------------------------------------------
       ENREGISTRER LE CHOIX
    ------------------------------------------------- */

    function saveConsent(
        analytics,
        preferences
    ) {

        const consent = {

            necessary: true,

            analytics: analytics,

            preferences: preferences,

            date: new Date().toISOString()

        };


        localStorage.setItem(
            "comunity_cookie_consent",
            JSON.stringify(consent)
        );


        if (cookieBanner) {

            cookieBanner.classList.remove(
                "visible"
            );

        }


        if (cookieSettingsPanel) {

            cookieSettingsPanel.classList.remove(
                "visible"
            );

            cookieSettingsPanel.setAttribute(
                "aria-hidden",
                "true"
            );

        }

    }


    /* -------------------------------------------------
       TOUT ACCEPTER
    ------------------------------------------------- */

    if (cookieAccept) {

        cookieAccept.addEventListener(
            "click",
            function () {

                saveConsent(
                    true,
                    true
                );

            }
        );

    }


    /* -------------------------------------------------
       TOUT REFUSER
    ------------------------------------------------- */

    if (cookieRefuse) {

        cookieRefuse.addEventListener(
            "click",
            function () {

                saveConsent(
                    false,
                    false
                );

            }
        );

    }


    /* -------------------------------------------------
       PERSONNALISER
    ------------------------------------------------- */

    if (cookieSettings) {

        cookieSettings.addEventListener(
            "click",
            function () {

                cookieSettingsPanel.classList.add(
                    "visible"
                );

                cookieSettingsPanel.setAttribute(
                    "aria-hidden",
                    "false"
                );

            }
        );

    }


    /* -------------------------------------------------
       FERMER PERSONNALISATION
    ------------------------------------------------- */

    if (cookieSettingsClose) {

        cookieSettingsClose.addEventListener(
            "click",
            function () {

                cookieSettingsPanel.classList.remove(
                    "visible"
                );

                cookieSettingsPanel.setAttribute(
                    "aria-hidden",
                    "true"
                );

            }
        );

    }


    /* -------------------------------------------------
       REFUS DEPUIS PERSONNALISATION
    ------------------------------------------------- */

    if (cookieSettingsRefuse) {

        cookieSettingsRefuse.addEventListener(
            "click",
            function () {

                saveConsent(
                    false,
                    false
                );

            }
        );

    }


    /* -------------------------------------------------
       ENREGISTRER LES PRÉFÉRENCES
    ------------------------------------------------- */

    if (cookieSettingsSave) {

        cookieSettingsSave.addEventListener(
            "click",
            function () {

                const analytics =
                    document.getElementById(
                        "analyticsCookies"
                    ).checked;


                const preferences =
                    document.getElementById(
                        "preferenceCookies"
                    ).checked;


                saveConsent(
                    analytics,
                    preferences
                );

            }
        );

    }

});


const manageCookies =
    document.getElementById("manageCookies");

if (manageCookies) {

    manageCookies.addEventListener(
        "click",
        function (event) {

            event.preventDefault();

            const panel =
                document.getElementById(
                    "cookieSettingsPanel"
                );

            if (panel) {

                panel.classList.add("visible");

                panel.setAttribute(
                    "aria-hidden",
                    "false"
                );

            }

        }
    );

}