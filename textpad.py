from tkinter import *
from tkinter import filedialog

class Text_Pad:

    # current File
    current_open_file = ""
    #open File File menu submneu item:
    def open_file(self):
        open_return = filedialog.askopenfile(initialdir="/",title="Select file to open", filetypes=(("text files","*.txt"),("all file","*.*")))
        if(open_return != None):
            self.text_area.delete(1.0,END)
            for line in open_return:
                self.text_area.insert(END,line)
            self.current_open_file= open_return.name
            open_return.close()

    def save_as_file(self):
        f = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
        if f is None:
            return
       
        save_text= self.text_area.get(1.0,END)
        self.current_open_file = f.name
        f.write(save_text)
        f.close()

    def save_file(self):
        if self.current_open_file == "":
            self.save_as_file()
        else:
            f = open(self.current_open_file,"w+")
            f.write(self.text_area.get(1.0,END))
            f.close()
    
    def new_file(self):
        self.text_area.delete(1.0, END)
        self.current_open_file == ""
        

    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())


    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sil.last")

    def past_text(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())
        
    

    def __init__(self,master):
        self.master = master

        master.title("Text Pad")
        self.text_area = Text(self.master,undo=True)
        self.text_area.pack(fill=BOTH,expand=1)
        
        # manu Config
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)

        #creating File Menu 
        self.file_menu = Menu(self.main_menu,tearoff= FALSE)
        self.main_menu.add_cascade(label = "File",menu = self.file_menu)
   
            # Creating Some Submenu in File menu
        self.file_menu.add_command(label ="New",command=self.new_file)
        self.file_menu.add_command(label ="Open",command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label ="Save",command=self.save_file)
        self.file_menu.add_command(label ="Save As",command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label ="Exit",command=master.quit)



        # Creating Edit menu
        self.edit_menu = Menu(self.main_menu,tearoff= FALSE)
        self.main_menu.add_cascade(label = "Edit", menu = self.edit_menu)

            # Creating Some Submenu in Edit menu
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)

        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy",command=self.copy_text)
        self.edit_menu.add_command(label="Cut",command=self.cut_text)
        self.edit_menu.add_command(label="Past",command=self.past_text)



root = Tk()
root.geometry("800x500+100+100")
text_editor = Text_Pad(root)
root.mainloop()