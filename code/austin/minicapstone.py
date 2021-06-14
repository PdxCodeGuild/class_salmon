import PySimpleGUI as sg
sg.theme('Material2')
layout = [[sg.Text(''  * 10)],
          [sg.Text('', size = (24, 1), font = (18),
                text_color = 'black', key = 'input')],
          [sg.Text('', size = (24, 1), font = (18),
                text_color = 'black', key = 'answer', justification = 'right')],  
          [sg.Text(''  * 10)],
          [sg.Button('c'), sg.Button('<x|'),sg.Button('('), sg.Button(')')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
          [sg.Button('.'), sg.Button('0'), sg.Button('='), sg.Button('+')]
          ]
window = sg.FlexForm('Calculator', default_button_element_size = (5, 2),
                auto_size_buttons = False, grab_anywhere = False)
window.Layout(layout)
userinput=''
while True:
    event, values = window.read()  #opens window
    window.FindElement('answer').Update('')
    if event == sg.WIN_CLOSED: 
        break
    elif event == 'c':
        userinput = ''
        window.FindElement('input').Update(userinput)
    elif event == '<x|':
        userinput = userinput[:-1]
        window.FindElement('input').Update(userinput)
    elif event == '=':
        try:
            answer = round(eval(userinput),4)
        except SyntaxError:
            answer = 'Error'#could be more specific with errors
        except ZeroDivisionError:
            answer = 'Can\'t divide by zero!'
        window.FindElement('answer').Update(answer)
        userinput = ''
    else: 
        userinput += event  
        window.FindElement('input').Update(userinput)