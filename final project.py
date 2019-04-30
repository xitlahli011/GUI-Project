import tkinter
calc = tkinter.Tk()
calc.geometry('342x545')
calc.title('Calculator')



txtDisplay = tkinter.Label(calc, width = 12, borderwidth = 35, bg = 'light blue', font = ('arial', 30))
txtDisplay.grid(row = 0, column = 0, columnspan = 4)

funcStrStore = '' 
numStoreStr = ''
firstNum = 0
secNum = 0

def equalBtn():
    global funcStrStore
    global numStoreStr
    global firstNum
    global secNum
    secNum = int(numStoreStr)
    if funcStrStore == '+' :
        answer = firstNum + secNum
    if funcStrStore == '-' :
        answer = firstNum - secNum
    if funcStrStore == 'x' :
        answer = firstNum * secNum
    if funcStrStore == '÷' :
        answer = firstNum / secNum
    txtDisplay.configure(text = str(answer))
    

#############################################################

def btnClick7():
    global numStoreStr
    numStoreStr += '7'
    txtDisplay.configure(text = numStoreStr)

def btnClick8():
    global numStoreStr
    numStoreStr += '8'
    txtDisplay.configure(text = numStoreStr)

def btnClick9():
    global numStoreStr
    numStoreStr += '9'
    txtDisplay.configure(text = numStoreStr)

def plusBtn():
    global funcStrStore
    global numStoreStr
    global firstNum
    funcStrStore = '+'
    firstNum = int(numStoreStr)
    numStoreStr = ''
    txtDisplay.configure(text = numStoreStr)
    
#############################################################

def btnClick4():
    global numStoreStr
    numStoreStr += '4'
    txtDisplay.configure(text = numStoreStr)

def btnClick5():
    global numStoreStr
    numStoreStr += '5'
    txtDisplay.configure(text = numStoreStr)

def btnClick6():
    global numStoreStr
    numStoreStr += '6'
    txtDisplay.configure(text = numStoreStr)

def minusBtn():
    global funcStrStore
    global numStoreStr
    global firstNum
    funcStrStore = '-'
    firstNum = int(numStoreStr)
    numStoreStr = ''
    txtDisplay.configure(text = numStoreStr)

#############################################################

def btnClick1():
    global numStoreStr
    numStoreStr += '1'
    txtDisplay.configure(text = numStoreStr)

def btnClick2():
    global numStoreStr
    numStoreStr += '2'
    txtDisplay.configure(text = numStoreStr)

def btnClick3():
    global numStoreStr
    numStoreStr += '3'
    txtDisplay.configure(text = numStoreStr)

def multiplyBtn():
    global funcStrStore
    global numStoreStr
    global firstNum
    funcStrStore = 'x'
    firstNum = int(numStoreStr)
    numStoreStr = ''
    txtDisplay.configure(text = numStoreStr)

#############################################################

def btnClick0():
    global numStoreStr
    numStoreStr += '0'
    txtDisplay.configure(text = numStoreStr)

def divideBtn():
    global funcStrStore
    global numStoreStr
    global firstNum
    funcStrStore = '÷'
    firstNum = int(numStoreStr)
    numStoreStr = ''
    txtDisplay.configure(text = numStoreStr)

def clearBtn():
    global funcStrStore
    global numStoreStr
    global firstNum 
    funcStrStore = '' 
    numStoreStr = ''
    firstNum = 0
    txtDisplay.configure(text = numStoreStr)

#############################################################
    
button7 = tkinter.Button(calc, text = '7', command = btnClick7, borderwidth = 15, font = ('arial', 30, 'bold')) 
button7.grid(row = 1, column = 0)
button8 = tkinter.Button(calc, text = '8', command = btnClick8, borderwidth = 15, font = ('arial', 30, 'bold'))
button8.grid(row = 1, column = 1)
button9 = tkinter.Button(calc, text = '9', command = btnClick9, borderwidth = 15, font = ('arial', 30, 'bold'))
button9.grid(row = 1, column = 2)
addittionButton = tkinter.Button(calc, text = '+', command = plusBtn, borderwidth = 15, font = ('arial', 30, 'bold'))
addittionButton.grid(row = 1, column = 3)

button4 = tkinter.Button(calc, text = '4', command = btnClick4, borderwidth = 15, font = ('arial', 30, 'bold'))
button4.grid(row = 2, column = 0)
button5 = tkinter.Button(calc, text = '5', command = btnClick5, borderwidth = 15, font = ('arial', 30, 'bold'))
button5.grid(row = 2, column = 1)
button6 = tkinter.Button(calc, text = '6', command = btnClick6, borderwidth = 15, font = ('arial', 30, 'bold'))
button6.grid(row = 2, column = 2)
subtractionButton = tkinter.Button(calc, text = '-', command = minusBtn, borderwidth = 15, font = ('arial', 30, 'bold'))
subtractionButton.grid(row = 2, column = 3)

button1 = tkinter.Button(calc, text = '1', command = btnClick1, borderwidth = 15, font = ('arial', 30, 'bold'))
button1.grid(row = 3, column = 0)
button2 = tkinter.Button(calc, text = '2', command = btnClick2, borderwidth = 15, font = ('arial', 30, 'bold'))
button2.grid(row = 3, column = 1)
button3 = tkinter.Button(calc, text = '3', command = btnClick3, borderwidth = 15, font = ('arial', 30, 'bold'))
button3.grid(row = 3, column = 2)
multiplicationButton = tkinter.Button(calc, text = 'x', command = multiplyBtn, borderwidth = 15, font = ('arial', 30, 'bold'))
multiplicationButton.grid(row = 3, column = 3)

button0 = tkinter.Button(calc, text = '0', command = btnClick0, borderwidth = 15, font = ('arial', 30, 'bold'))
button0.grid(row = 4, column = 0)
clearButton = tkinter.Button(calc, text = 'C', command = clearBtn, borderwidth = 15, font = ('arial', 30, 'bold'))
clearButton.grid(row = 4, column = 1)
equalButton = tkinter.Button(calc, text = '=', command = equalBtn, borderwidth = 15, font = ('arial', 30, 'bold'))
equalButton.grid(row = 4, column = 2) 
divisionButton = tkinter.Button(calc, text = '÷', command = divideBtn, borderwidth = 15, font = ('arial', 30, 'bold'))
divisionButton.grid(row = 4, column = 3)

#############################################################

