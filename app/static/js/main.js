/* CFP Dental — main.js */
(function () {
  'use strict';

  const navbar  = document.getElementById('navbar');
  const toggle  = document.getElementById('navToggle');
  const drawer  = document.getElementById('navDrawer');

  // --- Navbar scroll (hero pages only) ---
  if (navbar && navbar.classList.contains('navbar--hero')) {
    function onScroll() {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // run once on load
  }

  // --- Mobile drawer ---
  if (toggle && drawer) {
    toggle.addEventListener('click', function () {
      const open = drawer.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open);
    });

    // Close on any drawer link click
    drawer.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        drawer.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

}());