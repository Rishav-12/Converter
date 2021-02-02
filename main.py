from tkinter import *

unit_dict = {
    "cm" : 0.01,
    "m" : 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams" : 1.0,
    "kg" : 1000.0,
    "quintals": 100000.0,
    "tonnes" : 1000000.0,
    "pounds" : 453.592
}

# Options for drop-down menu
OPTIONS = ["select units",
            "cm",
            "m",
            "km",
            "feet",
            "miles",
            "inches",
            "kg",
            "grams",
            "quintals",
            "tonnes",
            "pounds",
            "Celsius",
            "Fahrenheit"]

# Main window
root = Tk()
root.geometry("400x350")
root.title("Unit Converter")
root['bg'] = 'pink'

def ok():
    inp = float(inputentry.get())
    inp_unit = inputopt.get()
    out_unit = outputopt.get()
    
    if inp_unit == "Celsius" and out_unit == "Fahrenheit":
        outputentry.delete(0, END)
        outputentry.insert(0, (inp * 1.8) + 32)
    elif inp_unit == "Fahrenheit" and out_unit == "Celsius":
        outputentry.delete(0, END)
        outputentry.insert(0, (inp - 32) * (5/9))
    else:
        outputentry.delete(0, END)
        outputentry.insert(0, round(inp * unit_dict[inp_unit]/unit_dict[out_unit], 5))

inputopt = StringVar()
inputopt.set(OPTIONS[0])

outputopt = StringVar()
outputopt.set(OPTIONS[0])

inputlabel = Label(root, text = "Input")
inputlabel.grid(row = 0, column = 0, pady = 20)

inputentry = Entry(root, justify = "center", font = "bold")
inputentry.grid(row = 1, column = 0, padx = 35, ipady = 5)

inputmenu = OptionMenu(root, inputopt, *OPTIONS)
inputmenu.grid(row = 1, column = 1)
inputmenu.config(font = "Arial 10")

outputlabel = Label(root, text = "Output")
outputlabel.grid(row = 2, column = 0, pady = 20)

outputentry = Entry(root, justify = "center", font = "bold")
outputentry.grid(row = 3, column = 0, padx = 35, ipady = 5)

outputmenu = OptionMenu(root, outputopt, *OPTIONS)
outputmenu.grid(row = 3, column = 1)
outputmenu.config(font = "Arial 10")

okbtn = Button(root, text = "OK", command = ok, padx = 80, pady = 2)
okbtn.grid(row = 4, column = 0, columnspan = 2, pady = 50)

root.mainloop()
