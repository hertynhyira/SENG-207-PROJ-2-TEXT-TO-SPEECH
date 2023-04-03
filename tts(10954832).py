# SENG 207 - PROGRAMMING FOR ENGINEERS
# NAME : HENRIETTA NHYIRA AFIA GYEKYI
# ID : 10954832
# PROJECT 2- PART 2
# MTEN DEPARTMENT

import PySimpleGUI as sg
import pyttsx3


sg.theme('TealMono')


Engine = pyttsx3.init()
VoicePick = Engine.getProperty('voices')


win_layout = [    [sg.Text('Select the type of voice:'),sg.Radio('Male', 'RADIO1', default=True, key='male'),sg.Radio('Female', 'RADIO1', key='female')],
     [sg.Text('Enter text to speak:')],
     [sg.InputText(key='type'),sg.Button('Speak')],
      [sg.Text("Volume:",text_color= 'white',background_color='blue',)],
    [sg.Slider(range=(0, 1), resolution=0.1, default_value=0.5, orientation="h", key="-VOLUME-")],
    [sg.Text("Rate:",text_color= 'white',background_color='blue')],
    [sg.Slider(range=(100, 300), resolution=10, default_value=200, orientation="h", key="-SPEED-")]
]

window = sg.Window('Text-To-Speech App', win_layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        if values['male']:
            Engine.setProperty('voice', VoicePick[0].id)
        elif values['female']:
           Engine.setProperty('voice', VoicePick[1].id)

        
        text = values['type']
        userVolume = values["-VOLUME-"]
        userRate = values["-SPEED-"]
        Engine.setProperty('volume', userVolume)
        Engine.setProperty("rate", userRate)
        Engine.say(text)
        Engine.runAndWait() 
    
        Engine.say(text)
        Engine.runAndWait()

window.close()