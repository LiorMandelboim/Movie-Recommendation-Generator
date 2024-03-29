from io import BytesIO
import tkinter as tk
import tkinter.ttk as ttk
from movie_algorithm import Movie_Recommendation as MR
from urllib.request import urlopen
from PIL import Image, ImageTk



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

class create_labeled_movie(ttk.Frame):
        def __init__(self, parent, movie_name, movie_final_score , img_url):
            ttk.Frame.__init__(self , parent)
            try:
                with urlopen(img_url) as response:
                    data = response.read()
                    img = Image.open(BytesIO(data))
                    img = img.resize((181, 267)) 
                    image = ImageTk.PhotoImage(img)
                    label = ttk.Label(self, image=image , anchor="w")
                    label.image = image  
                    label.pack(side="left")
            except:
                 pass
            title = ttk.Label(self , text=movie_name+"," , font=(15))
            title.pack(side="left")

            s = ttk.Label(self , text="Movie final score:" , font=(7))
            s.pack(side="left")
            score = ttk.Label(self , text=movie_final_score , font=(10))
            score.pack(side="left")
        


class Application:
    def __init__(self):
        self.root= tk.Tk()
        self.root.configure(background='Pink')
        self.root.title("Movie Recommendation Generator")
        self.MR = MR()
        self.create_widgets()
        self.root.mainloop()

    def execute(self):
        rating = self.rating.get_value() if self.rating.get_value() else None
        length = self.length.get_value() if self.length.get_value() else None
        director = self.director.get_value() if self.director.get_value() else None
        actor = self.actor.get_value() if self.actor.get_value() else None
        genre = self.genres.get_value() if self.genres.get_value() else None
        year = self.year.get_value() if self.year.get_value() else None
        pref = {'genres' : genre , 'director' : director , 'rating' : rating , 'year' : year ,
            'time' : length , 'actors' : actor}
        top_five_movies = self.MR.recommend(pref)
        self.winners_window(top_five_movies)

    def winners_window(self , top_five_movies):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Winners")

        self.title = ttk.Label(self.new_window, text="Movie Recommencdations" , font=("Arial Bold" , 30))
        self.title.pack(pady=15 , padx=30)
        # Create a canvas widget to contain the content
        self.canvas = tk.Canvas(self.new_window)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Create a frame inside the canvas to hold the content
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")


        for movie, rating in top_five_movies.items():
            img_url = self.MR.get_movie_url(movie)
            self.movie_line = create_labeled_movie(self.frame, movie , rating , img_url)
            self.movie_line.pack(fill="both" , expand=True)

        # Create a vertical scrollbar and link it to the canvas
        self.scrollbar = ttk.Scrollbar(self.new_window, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Bind the canvas to respond to changes in size
        self.frame.bind("<Configure>", self.on_frame_configure)



    def on_frame_configure(self, event):
        # Update the scroll region of the canvas to encompass the entire frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    
    def create_widgets(self):
        self.top_label = tk.Label(self.root , text ="Movie Recommendation Generator" , font=("Arial Bold" , 30))
        self.top_label.pack(padx=20,pady=20)
        
        style = ttk.Style()
        style.configure("Pink.TFrame", background="pink")
        self.middle_frame = ttk.Frame(self.root , style="Pink.TFrame")
        

        start_rate = 80  
        end_rate = 93    
        step_rate = 1    
        ratings= [x / 10 for x in range(start_rate, end_rate, step_rate)]
        self.rating = create_labeled_combobox(self.middle_frame, "Rating:", ratings)
        self.rating.pack(side="left" , pady=20)

        genres = self.MR.get_values('genres')
        self.genres = create_labeled_combobox(self.middle_frame, "Genre:", genres)
        self.genres.pack(side="left" , pady=20)
    
        length = ['60-90' , '90-120' , '120-150' , '150-180' , '180+']
        self.length = create_labeled_combobox(self.middle_frame , "Duration(min):" , length)
        self.length.pack(side="left", pady=20)
        self.middle_frame.pack()

        self.year = create_labeled_entry(self.root ,"From Year:" )
        self.year.pack(pady=10)

        self.director = create_labeled_entry(self.root ,"Director:" )
        self.director.pack(pady=10)

        self.actor = create_labeled_entry(self.root ,"Actor:" )
        self.actor.pack(pady=10)

        self.button= ttk.Button(self.root, text = "Submit" , command=self.execute)
        self.button.pack(side="right" , pady=20)
    



Application()


