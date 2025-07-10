//fonction retourner en haut
(function() {
    "use strict";
    const select = (el, all = false) => {
      el = el.trim()
      if (all) {
        return [...document.querySelectorAll(el)]
      } else {
        return document.querySelector(el)
      }
    }
      const onscroll = (el, listener) => {
      el.addEventListener('scroll', listener)
    }
    let backtotop = select('.back-to-top')
    if (backtotop) {
      const toggleBacktotop = () => {
        if (window.scrollY > 100) {
          backtotop.classList.add('active')
        } else {
          backtotop.classList.remove('active')
        }
      }
      window.addEventListener('load', toggleBacktotop)
      onscroll(document, toggleBacktotop)
    }
   })()

/*Titre*/
anime.timeline({loop: false})
  .add({
    targets: '.ml5 .line',
    opacity: [0.5,1],
    scaleX: [0, 1],
    easing: "easeInOutExpo",
    duration: 700
  }).add({
    targets: '.ml5 .line',
    duration: 600,
    easing: "easeOutExpo",
    translateY: (el, i) => (-0.625 + 0.625*2*i) + "em"
  }).add({
    targets: '.ml5 .letters-left',
    opacity: [0,1],
    translateX: ["0.5em", 0],
    easing: "easeOutExpo",
    duration: 600,
    offset: '-=300'
  }).add({
    targets: '.ml5',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 100000000000000000
  });

  /*Telecharger le jeu*/
  function telecharger() {
    window.location.href = "https://www.mediafire.com/file/5b26xixk90b57s9/mot_le_plus_long_v1.4.rar/file";
  }

  /*Carrousel d'images*/
const slide = ["../images/connexion.png","../images/accueil.png", "../images/select.png", "../images/crea.png", "../images/fin.png","../images/accueil2.png","../images/regles.png","../images/ach.png","../images/fond.png","../images/rank.png","../images/compte.png"];
let numero = 0;

function ChangeSlide(sens) {
    numero = numero + sens;
    if (numero < 0)
        numero = slide.length - 1;
    if (numero > slide.length - 1)
        numero = 0;
    document.getElementById("slide").src = slide[numero];
}