const colorForm = document.querySelector('#color-form')
const colorInput = document.querySelector('#color-input')
const main = document.querySelector('main')

colorForm.addEventListener('submit', function (event) {
  event.preventDefault()
  const newColor = colorInput.value
  const newColorDiv = document.createElement('div')
  newColorDiv.className = 'color'
  newColorDiv.style.backgroundColor = newColor
  main.appendChild(newColorDiv)
  colorInput.value = ''
})
