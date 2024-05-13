window.addEventListener('DOMContentLoaded', () => {
    const tabs = require('/static/vendor/js/modules/tabs.js'),
        modal = require('/static/vendor/js/modules/modal.js'),
        timer = require('/static/vendor/js/modules/timer.js'),
        cards = require('/static/vendor/js/modules/cards.js'),
        calc = require('/static/vendor/js/modules/calc.js'),
        forms = require('/static/vendor/js/modules/forms.js'),
        slider = require('/static/vendor/js/modules/slider.js');

    tabs();
    modal();
    timer();
    cards();
    calc();
    forms();
    slider();

});