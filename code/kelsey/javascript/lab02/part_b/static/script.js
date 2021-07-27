// # Index	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
// # English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
// # ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m

// 1. queries from html
// 2. submit
// 3. match value from html to cipher using rot13 function
// 4. return output

const letters = 'abcdefghijklmnopqrstuvwxyz'
const btn = document.querySelector('#submit')

function rot13(code) {
    let output = ''
    for (let i = 0; i < code.length; i++) {
        let startingIndex = letters.indexOf(code[i]) + 1
        if (startingIndex <= 12) {
            output += letters[startingIndex + 13]
        } else if (startingIndex > 12 && startingIndex < 26) {
            output += letters[startingIndex - 13]
        }
    }
    return output
}

btn.addEventListener("click", function(event) {
    event.preventDefault()
    let input = document.querySelector('#code')
    let messageArea = document.querySelector('#message')
    let code = input.value
    messageArea.innerText = rot13(code)
})