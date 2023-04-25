import tkinter as tk
from tkinter import * 
# create root window
root = tk.Tk()

y = 0
# root window title and dimension
root.title("Welcome to TkapDx mini")
# Set geometry(widthxheight)
root.geometry('350x350')
 
# adding a label to the root window
lbl = Label(root, text = "C - Transmission Dashboard")
lbl.grid()
 
# function to display text when
# button is clicked
def clicked():
    import pandas as pd
    import plotly.express as px



    df = pd.read_excel(io='D:\server-mahanadi\A400 Data for Dashboard testing.xlsx',
                   sheet_name='Sheet1',
                   skiprows=4)

    l1=[]
    l1.append(df)
    if df in l1:

    #while True:

        #print(df)   

#fig = px.line(df, x = 'Tool Details', y = 'BOLT - 1', title='c transmission dashboard')

        fig = px.line(df, x='Date & Time', y='RH Input Bore S1', title='RH Input Bore S1')
        fig.add_hline(y=62.019,line_color = "red",line_width = 2)
        fig.add_hline(y=62,line_color = "red")
        fig.update_traces(line_color="blue")
#fig.add_vline(x="12/19/2022  7:54:28 AM")
#fig.add_hrect(y0=0.9, y1=2.6, line_width=0, fillcolor="red", opacity=0.2)

    fig.update_layout(
    autosize=False,
    width=1600,
    height=900,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
)

    fig.show() 

btn = tk.Button(root, text = "Click to view" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)
 
#plotting second graph

lb2 = Label(root, text = "RH Counter Bore S1")
lb2.grid()
 
# function to display text when
# button is clicked
def clicked1():
    import pandas as pd
    
    import plotly.express as px



    df = pd.read_excel(io='D:\server-mahanadi\A400 Data for Dashboard testing.xlsx',
                   sheet_name='Sheet1',
                   skiprows=4)

    l1=[]
    l1.append(df)
    if df in l1:

    #while True:

        #print(df)   

#fig = px.line(df, x = 'Tool Details', y = 'BOLT - 1', title='BOLT - 1')

        fig2 = px.line(df, x='Date & Time', y='RH Counter Bore S1', title='RH Counter Bore S1')
        fig2.add_hline(y=38.039,line_color = "red",line_width = 2)
        fig2.add_hline(y=38,line_color = "red")
        fig2.update_traces(line_color="blue")
#fig.add_vline(x="12/19/2022  7:54:28 AM")
#fig.add_hrect(y0=0.9, y1=2.6, line_width=0, fillcolor="red", opacity=0.2)

    fig2.update_layout(
    autosize=False,
    width=1600,
    height=900,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
)

    fig2.show() 

btn1 = tk.Button(root, text = "Click to view" ,
             fg = "black", command=clicked)
# set Button grid
btn1.grid(column=1, row=1)
 


#plotiing 3rd graph
lb3 = Label(root, text = "RH Counter Bore S1")
lb3.grid()
 
# function to display text when
# button is clicked
def clicked3():
    import pandas as pd
    import plotly.express as px



    df = pd.read_excel(io='D:\server-mahanadi\A400 Data for Dashboard testing.xlsx',
                   sheet_name='Sheet1',
                   skiprows=4)

    l1=[]
    l1.append(df)
    if df in l1:

    #while True:

        #print(df)   

#fig = px.line(df, x = 'Tool Details', y = 'BOLT - 1', title='BOLT - 1')

        fig3 = px.line(df, x='Date & Time', y='RH Counter Bore S1', title='RH Counter Bore S1')
        fig3.add_hline(y=38.039,line_color = "red",line_width = 2)
        fig3.add_hline(y=38,line_color = "red")
        fig3.update_traces(line_color="blue")
#fig.add_vline(x="12/19/2022  7:54:28 AM")
#fig.add_hrect(y0=0.9, y1=2.6, line_width=0, fillcolor="red", opacity=0.2)

    fig3.update_layout(
    autosize=False,
    width=1600,
    height=900,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor="LightSteelBlue",
)

    fig3.show() 

btn3 = tk.Button(root, text = "Click to view" ,
             fg = "black", command=clicked)
# set Button grid
btn3.grid(column=1, row=2)


# Execute Tkinter
root.mainloop()
