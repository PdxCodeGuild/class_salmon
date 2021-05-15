let canvas = document.getElementById("canvas");
let ctx = canvas.getContext('2d');

ctx.fillStyle = "coral";
ctx.fillRect(100, 100, 200, 200);

ctx.fillStyle = "darkslateblue";
ctx.fillRect(200, 200, 200, 200);

ctx.strokeStyle = "black";
ctx.strokeRect(100, 100, 200, 200);

ctx.rect(125, 125, 50, 50);
ctx.fill();
ctx.stroke();

ctx.beginPath();
ctx.arc(150, 150, 100, Math.PI/2, Math.PI, true);
ctx.strokeStyle = 'deeppink';
ctx.lineWidth = 5;
ctx.stroke();

ctx.beginPath();
ctx.moveTo(0,75);
ctx.lineTo(300,225);
ctx.strokeStyle = "dodgerblue";
ctx.stroke();

let mouseDown = false;
canvas.addEventListener("mousedown", function(e) {
    mouseDown = true;
});
canvas.addEventListener("mouseup", function(e) {
    mouseDown = false;
});
canvas.addEventListener("mousemove", function(e) {
    console.log(e.clientX, e.clientY);
    if (mouseDown) {
        ctx.beginPath();
        ctx.arc(e.clientX, e.clientY, 10, 0, 2*Math.PI, false);
        ctx.fillStyle = 'deeppink';
        ctx.fill();
    };
});
