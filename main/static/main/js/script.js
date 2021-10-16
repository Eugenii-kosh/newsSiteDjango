let offset = 0;
const sliderLine = document.querySelector('.slider-line');

document.querySelector('.btn__next').addEventListener('click', function(){
    offset = offset + 1200;
    if (offset > 1200*4) {
        offset = 0;
    };
    sliderLine.style.left = -offset + 'px';
});

document.querySelector('.btn__prev').addEventListener('click', function(){
    offset = offset - 1200;
    if (offset < 0) {
        offset = 1200*4;
    };
    sliderLine.style.left = -offset + 'px';
});