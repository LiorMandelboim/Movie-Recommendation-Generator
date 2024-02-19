import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

class create_labeled_combobox(ttk.Frame):
    def __init__(self, parent, label_text, combobox_values, combobox_size=10):
        ttk.Frame.__init__(self , parent)
        self.label = ttk.Label(self, text=label_text)
        self.combobox = ttk.Combobox(self, values=combobox_values , width=combobox_size)
        self.label.pack(side="left" , padx=5)
        self.combobox.pack(side="right")

    def get_value(self):
        return self.combobox.get()

class create_labeled_entry(ttk.Frame):
        def __init__(self, parent, label_text, textbox_size=30):
            ttk.Frame.__init__(self , parent)
            self.label = ttk.Label(self, text=label_text)
            text = tk.StringVar()
            self.textbox = ttk.Entry(self, textvariable=text , width=textbox_size)
            self.label.pack(side="left" , padx=5)
            self.textbox.pack(side="right")
        
        def get_value(self):
             return self.textbox.get()
        


class Application:
    def __init__(self):
        self.root= tk.Tk()
        self.root.configure(background='Pink')
        self.root.title("Movie Recomendation Generator")
        self.create_widgets()
        self.root.mainloop()

    def execute(self):
         rating = self.rating.get_value()
         length = self.length.get_value()
         director = self.director.get_value()
         print (rating+length+director)
    
    def create_widgets(self):
        self.top_label = tk.Label(self.root , text ="Movie Recomendation Generator" , font=("Arial Bold" , 30))
        self.top_label.pack(padx=20,pady=20)
        
        self.middle_frame = ttk.Frame(self.root)

        start_rate = 80  
        end_rate = 93    
        step_rate = 1    
        ratings= [x / 10 for x in range(start_rate, end_rate, step_rate)]
        self.rating = create_labeled_combobox(self.middle_frame, "Rating:", ratings)
        self.rating.pack(side="left" , pady=20)
    
        length = ['60-90' , '90-120' , '120-150' , '150-180' , '180+']
        self.length = create_labeled_combobox(self.middle_frame , "Length(min):" , length)
        self.length.pack(side="left", pady=20)
        self.middle_frame.pack()

        self.director = create_labeled_entry(self.root ,"Actor:" )
        self.director.pack(pady=20)

        self.button= ttk.Button(self.root, text = "Submit" , command=self.execute)
        self.button.pack(side="right" , pady=20)
       




        


        




Application()


"""
def on_submit():
    user_input = entry.get()
    
    messagebox.showinfo("Message", f"You entered: {user_input}")

# Create the main application window
root = tk.Tk()
root.title("Simple GUI")

# Create a label
label = tk.Label(root, text="Enter something:")
label.pack()

# Create an entry field for user input
entry = tk.Entry(root)
entry.pack()

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Run the Tkinter event loop
root.mainloop()
"""