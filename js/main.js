/**
 * Stefano Davide Ciancimino — Portfolio Professionale
 * Navigation, Dark Mode, Animations, Forms
 */

(function () {
  'use strict';

  const header = document.querySelector('.header');
  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  const themeToggle = document.querySelector('.theme-toggle');
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  /* Theme */
  function getPreferredTheme() {
    const stored = localStorage.getItem('theme');
    if (stored) return stored;
    return 'dark';
  }

  function setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }

  setTheme(getPreferredTheme());

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const current = document.documentElement.getAttribute('data-theme');
      setTheme(current === 'dark' ? 'light' : 'dark');
    });
  }

  /* Header scroll */
  function handleScroll() {
    if (!header) return;
    header.classList.toggle('header--scrolled', window.scrollY > 20);
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();

  /* Mobile nav */
  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      navToggle.classList.toggle('nav-toggle--active');
      nav.classList.toggle('nav--open');
      document.body.style.overflow = nav.classList.contains('nav--open') ? 'hidden' : '';
    });

    nav.querySelectorAll('.nav__link').forEach(function (link) {
      link.addEventListener('click', function () {
        navToggle.classList.remove('nav-toggle--active');
        nav.classList.remove('nav--open');
        document.body.style.overflow = '';
      });
    });
  }

  /* Active nav */
  document.querySelectorAll('.nav__link').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('nav__link--active');
    }
  });

  /* Reveal */
  const revealElements = document.querySelectorAll('.reveal');

  if (revealElements.length > 0 && 'IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('reveal--visible');
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );

    revealElements.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    revealElements.forEach(function (el) {
      el.classList.add('reveal--visible');
    });
  }

  /* Timeline animation */
  const timelineItems = document.querySelectorAll('.timeline__item');

  if (timelineItems.length > 0 && 'IntersectionObserver' in window) {
    const timelineObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('timeline__item--visible');
            timelineObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.2 }
    );

    timelineItems.forEach(function (item, index) {
      item.style.transitionDelay = index * 0.1 + 's';
      timelineObserver.observe(item);
    });
  } else {
    timelineItems.forEach(function (item) {
      item.classList.add('timeline__item--visible');
    });
  }

  /* Smooth scroll */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const offset = header ? header.offsetHeight + 16 : 0;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  /* Contact form */
  const contactForm = document.getElementById('contact-form');

  if (contactForm) {
    const successMessage = document.getElementById('form-success');

    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      let isValid = true;
      const fields = [
        { id: 'nome', required: true, minLength: 2 },
        { id: 'email', required: true, type: 'email' },
        { id: 'telefono', required: false },
        { id: 'servizio', required: true },
        { id: 'messaggio', required: true, minLength: 10 }
      ];

      fields.forEach(function (field) {
        const input = document.getElementById(field.id);
        if (!input) return;

        const group = input.closest('.form-group');
        const existingError = group.querySelector('.form-error');

        if (existingError) existingError.remove();
        group.classList.remove('form-group--error');

        let error = '';

        if (field.required && !input.value.trim()) {
          error = 'Questo campo è obbligatorio';
        } else if (field.type === 'email' && input.value.trim()) {
          const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailRegex.test(input.value.trim())) {
            error = 'Inserisci un indirizzo email valido';
          }
        } else if (field.minLength && input.value.trim().length < field.minLength) {
          error = 'Inserisci almeno ' + field.minLength + ' caratteri';
        }

        if (error) {
          isValid = false;
          group.classList.add('form-group--error');
          const errorEl = document.createElement('p');
          errorEl.className = 'form-error';
          errorEl.textContent = error;
          group.appendChild(errorEl);
        }
      });

      if (isValid) {
        if (successMessage) {
          successMessage.classList.add('form-success--visible');
          successMessage.textContent =
            'Grazie per il messaggio! Ti risponderò entro 24 ore lavorative.';
        }
        contactForm.reset();

        setTimeout(function () {
          if (successMessage) {
            successMessage.classList.remove('form-success--visible');
          }
        }, 8000);
      }
    });
  }

  /* QR Code generator */
  const qrCanvas = document.getElementById('qr-cv');

  if (qrCanvas && typeof QRCode !== 'undefined') {
    const cvUrl = window.location.origin + window.location.pathname.replace(/[^/]+$/, 'cv.html');
    QRCode.toCanvas(qrCanvas, cvUrl, {
      width: 160,
      margin: 2,
      color: { dark: '#0f172a', light: '#ffffff' }
    });
  }

  /* CV download */
  const cvDownloadBtn = document.getElementById('download-cv');

  if (cvDownloadBtn) {
    cvDownloadBtn.addEventListener('click', function (e) {
      if (this.getAttribute('href') === 'cv.html') {
        e.preventDefault();
        window.open('cv.html', '_blank');
        setTimeout(function () {
          window.print();
        }, 500);
      }
    });
  }
})();