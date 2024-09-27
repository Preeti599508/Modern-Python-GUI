import customtkinter as ctk

def add_Todo():
    todo=entry.get()
    label=ctk.CTkLabel(scrollabel_frame,text=todo)
    label.pack()
    entry.delete(0,ctk.END)

root=ctk.CTk(fg_color="grey")
root.geometry("750x450")
root.title("Todo App")

title_label=ctk.CTkLabel(root,text="Daily Tasks",font=ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx=10,pady=20)

scrollabel_frame=ctk.CTkScrollableFrame(root,width=500,height=200)
scrollabel_frame.pack()

entry=ctk.CTkEntry(scrollabel_frame,placeholder_text="Add Todo")
entry.pack(fill='x')

add_button=ctk.CTkButton(root,text="Add",width=500,command=add_Todo)
add_button.pack(pady=20)


root.mainloop()