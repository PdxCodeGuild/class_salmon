// color palette
const colors = {
  sky: '#191247',
  mountain: '#423D07',
  stroke: '#080421',
  snow: '#A8A79D',
  moon: '#FCF9A2'
}

// canvas dimensions
const w = 1125
const h = 750

// moon object
const moon = {
  x: 401,
  y: 423,
  r: 75
}

// stars array (use makeStars)
const stars = makeStars(10000)

const cnv = document.querySelector('canvas')
const ctx = cnv.getContext('2d')

ctx.strokeStyle = colors.stroke
ctx.lineWidth = 3

cnv.addEventListener('click', e => {
  console.log(e.offsetX, e.offsetY)
  moon.x = e.offsetX
  moon.y = e.offsetY
})

animationLoop()

function animationLoop () {
  ctx.clearRect(0, 0, w, h)

  ctx.fillStyle = colors.sky
  ctx.fillRect(0, 0, w, h)

  ctx.fillStyle = 'white'
  stars.forEach(drawStar)

  drawMoon(moon)

  drawTriangle(w * 0.75, h * 0.25, h * 0.75, colors.mountain)
  drawTriangle(w * 0.75, h * 0.25, 125, colors.snow)
  drawTriangle(w * 0.25, h * 0.25, h * 0.75, colors.mountain)
  drawTriangle(w * 0.25, h * 0.25, 125, colors.snow)

  moon.x++
  moon.y -= 0.5

  window.requestAnimationFrame(animationLoop)
}

function drawTriangle (startX, startY, height, color) {
  ctx.fillStyle = color
  ctx.beginPath()
  ctx.moveTo(startX, startY)
  ctx.lineTo(startX + height, startY + height)
  ctx.lineTo(startX - height, startY + height)
  ctx.closePath()
  ctx.fill()
  ctx.stroke()
}

function drawMoon (moon) {
  // moon
  ctx.fillStyle = colors.moon
  ctx.beginPath()
  ctx.arc(moon.x, moon.y, moon.r, 0, 2 * Math.PI)
  ctx.fill()

  // glow
  const gradient = ctx.createRadialGradient(moon.x, moon.y, 1, moon.x, moon.y, moon.r * 2)
  gradient.addColorStop(0, 'rgba(255, 255, 255, 0.5)')
  gradient.addColorStop(1, 'rgba(255, 255, 255, 0)')
  ctx.fillStyle = gradient
  ctx.beginPath()
  ctx.arc(moon.x, moon.y, moon.r * 2, 0, 2 * Math.PI)
  ctx.fill()
}

function makeStars (numOfStars) {
  const starsArr = []
  for (let i = 0; i < numOfStars; i++) {
    const star = {
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 1.75
    }
    starsArr.push(star)
  }
  return starsArr
}

function drawStar (star) {
  ctx.beginPath()
  ctx.arc(star.x, star.y, star.r, 0, 2 * Math.PI)
  ctx.fill()
}

/* ARCHIVE BELOW */

// cnv.addEventListener('click', e => {
//   console.log(e.offsetX, e.offsetY)
//   moon.x = e.offsetX
//   moon.y = e.offsetY
//   drawMoon(moon)
// })

// animationLoop()

// function animationLoop () {
//   ctx.clearRect(0, 0, w, h)

//   ctx.fillStyle = colors.sky
//   ctx.fillRect(0, 0, w, h)

//   ctx.fillStyle = 'white'
//   // const stars = makeStars(10000)
//   stars.forEach(drawStar)

//   moon.x++
//   moon.y -= 0.5
//   drawMoon(moon)

//   drawTriangle(w * 0.75, h * 0.25, h * 0.75, colors.mountain)
//   drawTriangle(w * 0.75, h * 0.25, 150, colors.snow3)

//   drawTriangle(w * 0.25, h * 0.25, h * 0.75, colors.mountain)
//   drawTriangle(w * 0.25, h * 0.25, 150, colors.snow3)
//   window.requestAnimationFrame(animationLoop)
// }

// function drawTriangle (startX, startY, height, color) {
//   ctx.fillStyle = color
//   ctx.beginPath()
//   ctx.moveTo(startX, startY)
//   ctx.lineTo(startX + height, startY + height)
//   ctx.lineTo(startX - height, startY + height)
//   ctx.closePath()
//   ctx.fill()
//   ctx.stroke()
// }

// function drawMoon (moon) {
//   // moon
//   ctx.fillStyle = colors.moon
//   ctx.beginPath()
//   ctx.arc(moon.x, moon.y, moon.r, 0, 2 * Math.PI)
//   ctx.fill()
//   ctx.stroke()

//   // glow
//   const gradient = ctx.createRadialGradient(moon.x, moon.y, 1, moon.x, moon.y, moon.r * 2)
//   gradient.addColorStop(0, 'rgba(255, 255, 255, 1)')
//   gradient.addColorStop(1, 'rgba(255, 255, 255, 0)')
//   ctx.fillStyle = gradient
//   ctx.beginPath()
//   ctx.arc(moon.x, moon.y, moon.r * 2, 0, 2 * Math.PI)
//   ctx.fill()
// }

// function makeStars (numOfStars) {
//   const starsArray = []
//   for (let i = 0; i < numOfStars; i++) {
//     const star = {
//       x: Math.random() * w,
//       y: Math.random() * h,
//       r: Math.random() * 1.5
//     }
//     starsArray.push(star)
//   }
//   return starsArray
// }

// function drawStar (star) {
//   ctx.beginPath()
//   ctx.arc(star.x, star.y, star.r, 0, 2 * Math.PI)
//   ctx.fill()
// }
