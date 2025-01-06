const imagepanel = document.getElementById('imagepanel');

imagepanel.addEventListener('mouseover', function(){
    imagepanel.classList.add('zoomed');
});

imagepanel.addEventListener('mouseout', function(){
    imagepanel.classList.remove('zoomed');
});

imagepanel.addEventListener('mousemove', function(e) {
    const x = e.offsetX;
    const y = e.offsetY;
    const originX = (x / imagepanel.width) * 100;
    const originY = (y / imagepanel.height) * 100;

    imagepanel.style.transformOrigin = `${originX}% ${originY}%`;
});
