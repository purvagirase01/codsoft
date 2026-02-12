import tkinter as tk
root=tk. Tk() # creates main frame
root.geometry("600x400") #frame size set
root.title("✨ To Do List ✨") #title of frame
#add function
def add_command():
    task=ent.get()
    lbox.insert(tk.END,task)
    ent.delete(0,tk.END)
    print(f"{task} is added to list")

#mark function
def mark_command():
    pos=lbox.curselection() [0]
    text=lbox.get(pos)
    lbox.delete(pos)
    lbox.insert(tk.END,f"{text} \u2713") #\u2713- it used to generate tick_mark(✅) sign
    print(f"{text} is completed")

#delete function    
def del_command():
    pos=lbox.curselection() [0]
    lbox.delete(pos)
    

#label_1 
lb_1=tk.Label(root,text="Enter Task:",font=('calibri',15))
lb_1.place(x=10,y=15)

#input box
ent=tk.Entry(root,width=50)
ent.place(x=120,y=20)

#task list box
lbox=tk.Listbox(root,width=50,height=10)
lbox.place(x=120,y=70)

#BUTTON NO.1 ("ADD TASK")
btn1=tk.Button(root,text="ADD", font=('calibri',15),width=12,command=add_command )#add_command function
btn1.place(x=50,y=250)

#BUTTON NO.2 ("mark as a completed TASK")
btn2=tk.Button(root,text="Mark", font=('calibri',15),width=12,command=mark_command )#mark_command function
btn2.place(x=230,y=250)

#BUTTON NO.3 ("REMOVE TASK")
btn3=tk.Button(root,text="Remove", font=('calibri',15),width=12,command=del_command )#del_command function)
btn3.place(x=400,y=250)




root.mainloop()


