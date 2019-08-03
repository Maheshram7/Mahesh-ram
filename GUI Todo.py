import PySimpleGUI as sg
import file

list=[]
complete=[]

list=file.readFile()
complete=file.readcomplete()

layout = [[sg.Text("To Do list")],
          [sg.Text('Enter a event'),sg.InputText("", key='event')],
          [sg.Listbox(values=list,size=(30,6),key='list',enable_events='true'),sg.Listbox(values=complete,size=(30,6),key='complete',enable_events='true')],
          [sg.CalendarButton('Choose date',key='date',target='datee'),sg.InputText("",disabled='true',key='datee',do_not_clear=False)],
          [sg.Slider(range=(1,5,1),default_value=1,orientation="horizontal",key="priority")],
          [sg.Button('Add'),sg.Button('Complete'),sg.Button("Delete Todo"),sg.Button("Delete Completed"),sg.Button("Prioritise"),sg.Button('Exit')],
          [sg.InputText("",key='error',disabled=True ,do_not_clear=False)]
         ]

window = sg.Window('ToDo App', layout)
while True:
    event, values = window.Read()
    if event == "Add":
        if(values['datee']==""):
            window.FindElement('error').Update("Choose a date")
            continue
        elif(values['event']==""):
            window.FindElement('error').Update("Enter a event")
            continue
        x=values['event']+" "+str(values['datee'])+" "+str(int(values['priority']))
        list.append(x)
        window.FindElement('list').Update(list)
        window.FindElement('event').Update("")
        file.writefile(list)
    elif event == "Delete Todo":
        list.remove(''.join(values['list']))
        window.FindElement('list').Update(list)
        file.writefile(list)
    elif event == "Delete Completed":
        complete.remove(''.join(values['complete']))
        window.FindElement('complete').Update(complete)
        file.writecomplete(complete)
    elif event == "Complete":
        complete.append(''.join(values['list']))
        list.remove(''.join(values['list']))
        window.FindElement('complete').Update(complete)
        window.FindElement('list').Update(list)
        file.writefile(list)
        file.writecomplete(complete)
    elif event == None or event == 'Exit':
        break
    elif event == 'Prioritise':
        for i in range(len(list)):
            min = i
            for j in range(i + 1, len(list)):
                if (list[min][-1] > list[j][-1]):
                    min = j
            list[i], list[min] = list[min], list[i]
        window.FindElement("list").Update(list)
        file.writefile(list)

window.Close()
