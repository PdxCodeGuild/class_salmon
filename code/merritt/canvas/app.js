let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');

ctx.fillStyle = 'green';
// ctx.fillRect(100, 100, 100, 100);
ctx.rect(100, 100, 100, 100);
ctx.fill();

ctx.clearRect(125, 125, 50, 50);

ctx.strokeStyle = 'red';
ctx.strokeRect(135, 135, 30, 30);

ctx.beginPath();
ctx.arc(150, 150, 50*Math.sqrt(2), 0, Math.PI * 2, false);
ctx.strokeStyle = 'black';
ctx.stroke();
ctx.fillStyle = 'rgba(0,0,0,.1)';
ctx.fill();

ctx.fillStyle = "black";
ctx.beginPath();
ctx.moveTo(0,150);
ctx.lineTo(300,150);
ctx.stroke();

ctx.beginPath();
ctx.moveTo(150, 0);
ctx.lineTo(150, 300);
ctx.stroke();

ctx.font = "26px Arial";
ctx.strokeText("Hello World", 10, 274);

ctx.beginPath();
let unClicked = true;
cnv.onclick = function(event) {
  var x = event.clientX;
  var y = event.clientY;
  if (unClicked) {
    ctx.moveTo(x,y)
    unClicked = false;
  } else {
    ctx.lineTo(x,y);
    ctx.stroke();
  }
}

function pixels() {
  let cnv = document.createElement('canvas');
  cnv.setAttribute("width", "500");
  cnv.setAttribute("height", "500");
  document.getElementById("body").appendChild(cnv);

  let ctx = cnv.getContext('2d');
  let img = ctx.createImageData(cnv.width, cnv.height);
  for (let i=0; i<cnv.width; ++i) {
    for (let j=0; j<cnv.height; ++j) {
      
      let r = 0;
      let g = 0;
      let b = 255;
      let a = 255;
      
      let k = 4*(j + i*cnv.height);
      img.data[k] = r;
      img.data[k+1] = g;
      img.data[k+2] = b;
      img.data[k+3] = a;
    }
  }
  ctx.putImageData(img, 0, 0);
}

pixels();