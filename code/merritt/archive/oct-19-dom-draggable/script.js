let draggable = document.getElementById("draggable");

let mouseButtonDown = false

draggable.addEventListener('mousedown', function() {
  mouseButtonDown = true;
});

draggable.addEventListener('mouseup', function() {
  mouseButtonDown = false;
});

draggable.addEventListener('mouseleave', function() {
  mouseButtonDown = false;
});

draggable.addEventListener('mousemove', function(event) {
  if (mouseButtonDown) {
    this.style.top = `${event.pageY - 100}px`;
    this.style.left = `${event.pageX - 100}px`;
  }
});