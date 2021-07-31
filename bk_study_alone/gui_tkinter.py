import tkinter

root = tkinter.Tk()
label = tkinter.Label(root, text='GUI 프로그램')
label.pack()

def func():
    print('Click')
    label.config(text='눌러봐')
    
button = tkinter.Button(root, text="클릭", command=func)
button.pack()

root.mainloop()
