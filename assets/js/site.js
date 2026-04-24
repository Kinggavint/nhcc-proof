// NHCC — front-end behaviors
// - Mobile nav drawer
// - Sticky header on scroll
// - Mark current nav item aria-current
// - Initialize AOS fade animations if available

(function(){
  'use strict';

  // Sticky header
  var header = document.querySelector('.site-header');
  var mainEl = document.querySelector('main.site-main');
  var firstSection = mainEl && mainEl.firstElementChild;
  var hasHero = firstSection && (firstSection.classList.contains('hero') || firstSection.classList.contains('interior_hero'));
  function onScroll(){
    if (!header) return;
    if (!hasHero || window.scrollY > 40) header.classList.add('sticky');
    else header.classList.remove('sticky');
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  onScroll();
  // Add top padding on pages without hero so content isn't hidden under fixed header
  if (!hasHero && mainEl) { mainEl.style.paddingTop = '6rem'; }

  // Mobile nav
  var menuBtn = document.querySelector('.menu-btn');
  var mobileNav = document.querySelector('.mobile-nav');
  var overlay = document.querySelector('.site-overlay');
  var closeBtn = document.querySelector('.mobile-close');
  function openMenu(){
    if (!mobileNav) return;
    mobileNav.classList.add('open');
    if (overlay) overlay.classList.add('open');
    if (menuBtn) menuBtn.setAttribute('aria-expanded','true');
    document.body.style.overflow='hidden';
  }
  function closeMenu(){
    if (!mobileNav) return;
    mobileNav.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    if (menuBtn) menuBtn.setAttribute('aria-expanded','false');
    document.body.style.overflow='';
  }
  if (menuBtn) menuBtn.addEventListener('click', openMenu);
  if (overlay) overlay.addEventListener('click', closeMenu);
  if (closeBtn) closeBtn.addEventListener('click', closeMenu);
  document.addEventListener('keydown', function(e){ if (e.key==='Escape') closeMenu(); });

  // Mark current nav
  var path = window.location.pathname.replace(/\/+$/,'') || '/';
  document.querySelectorAll('.main-navigation a, .mobile-nav a').forEach(function(a){
    try{
      var u = new URL(a.getAttribute('href'), window.location.origin);
      var href = u.pathname.replace(/\/+$/,'') || '/';
      if (href === path) a.setAttribute('aria-current','page');
    }catch(e){}
  });

  // AOS init (script loaded separately)
  if (window.AOS) window.AOS.init({duration:800, once:true, easing:'ease-out'});
})();
