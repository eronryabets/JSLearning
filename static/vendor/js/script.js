import tabs from '/static/vendor/js/modules/tabs.js';
import modal, {openModal} from '/static/vendor/js/modules/modal.js';
import timer from '/static/vendor/js/modules/timer.js';
import cards from '/static/vendor/js/modules/cards.js';
import calc from '/static/vendor/js/modules/calc.js';
import forms from '/static/vendor/js/modules/forms.js';
import slider from '/static/vendor/js/modules/slider.js';

window.addEventListener('DOMContentLoaded', () => {
    // const modalTimerId = setTimeout(openModal, 50000);
    const modalTimerId = setTimeout(() =>
        openModal('.modal', modalTimerId), 50000);

    tabs('.tabheader__item',
        '.tabcontent',
        '.tabheader__items',
        'tabheader__item_active');
    modal('[data-modal]','.modal', modalTimerId);
    timer('.timer', '2024-05-11');
    cards();
    calc();
    forms('form',modalTimerId);
     slider({
        container: '.offer__slider',
        slide: '.offer__slide',
        nextArrow: '.offer__slider-next',
        prevArrow: '.offer__slider-prev',
        totalCounter: '#total',
        currentCounter: '#current',
        wrapper: '.offer__slider-wrapper',
        field: '.offer__slider-inner'
    });

});