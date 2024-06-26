import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Recommender import Recommender

class RecommenderGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Media Recommender")
        self.root.geometry("1200x800")
        # set the window information
        self.recommender = Recommender()
        self.notebook = ttk.Notebook(self.root)
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        # create notebook as container
        self.create_movie_tab()
        self.create_tv_show_tab()
        self.create_book_tab()
        self.create_tv_movie_search_tab()
        self.create_book_search_tab()
        self.create_recommendation_tab()
        self.create_ratings_tab()
        # creating tabs
        self.create_buttons()
        # creating buttons
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)  # Ensure the button frame doesn't expand vertically
        self.root.grid_columnconfigure(0, weight=1)

    def create_movie_tab(self):
        movie_tab = ttk.Frame(self.notebook)
        self.notebook.add(movie_tab, text="Movies")

        self.movie_text = tk.Text(movie_tab, height=10)
        self.movie_text.pack(expand=True, fill="both")

        self.movie_stats_text = tk.Text(movie_tab, height=5)
        self.movie_stats_text.pack(expand=True, fill="both")

    def create_tv_show_tab(self):
        tv_show_tab = ttk.Frame(self.notebook)
        self.notebook.add(tv_show_tab, text="TV Shows")
        # add it into notebook

        self.tv_show_text = tk.Text(tv_show_tab, height=10)
        self.tv_show_text.pack(expand=True, fill="both")
        # fill the entire tab

        self.tv_show_stats_text = tk.Text(tv_show_tab, height=5)
        self.tv_show_stats_text.pack(expand=True, fill="both")

    def create_book_tab(self):
        book_tab = ttk.Frame(self.notebook)
        self.notebook.add(book_tab, text="Books")

        self.book_text = tk.Text(book_tab, height=10)
        self.book_text.pack(expand=True, fill="both")

        self.book_stats_text = tk.Text(book_tab, height=5)
        self.book_stats_text.pack(expand=True, fill="both")

    def create_tv_movie_search_tab(self):
        search_tab = ttk.Frame(self.notebook)
        self.notebook.add(search_tab, text="SearchMovies/TV")
        ttk.Label(search_tab, text="Type:").grid(row=0, column=0, padx=10, pady=5)
        self.search_type_combobox = ttk.Combobox(search_tab, values=["Movie", "TV Show"])
        self.search_type_combobox.grid(row=0, column=1, padx=10, pady=5)
        ttk.Label(search_tab, text="Title:").grid(row=1, column=0, padx=10, pady=5)
        self.search_title_entry = tk.Entry(search_tab, width=50)
        self.search_title_entry.grid(row=1, column=1, padx=10, pady=5)
        search_button = ttk.Button(search_tab, text="Search", command=self.search_media)
        search_button.grid(row=2, column=0, columnspan=2, pady=10)
        self.search_results_text = tk.Text(search_tab, height=15)
        self.search_results_text.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10)
    def create_book_search_tab(self):
        book_search_tab = ttk.Frame(self.notebook)
        self.notebook.add(book_search_tab, text="Search Books")

        ttk.Label(book_search_tab, text="Title:").grid(row=0, column=0, padx=10, pady=5)
        self.book_search_title_entry = tk.Entry(book_search_tab, width=50)
        self.book_search_title_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(book_search_tab, text="Author:").grid(row=1, column=0, padx=10, pady=5)
        self.book_search_author_entry = tk.Entry(book_search_tab, width=50)
        self.book_search_author_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(book_search_tab, text="Publisher:").grid(row=2, column=0, padx=10, pady=5)
        self.book_search_publisher_entry = tk.Entry(book_search_tab, width=50)
        self.book_search_publisher_entry.grid(row=2, column=1, padx=10, pady=5)

        search_button = ttk.Button(book_search_tab, text="Search", command=self.search_books)
        search_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.book_search_results_text = tk.Text(book_search_tab, height=15)
        self.book_search_results_text.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=10)

        self.book_search_results_text.insert(tk.END, "Please enter data to perform a search.")

    def create_recommendation_tab(self):
        recommendation_tab = ttk.Frame(self.notebook)
        self.notebook.add(recommendation_tab, text="Recommendation")

        ttk.Label(recommendation_tab, text="Type:").grid(row=0, column=0, padx=10, pady=5)
        self.recommendation_type_combobox = ttk.Combobox(recommendation_tab, values=["Movie", "TV Show", "Book"])
        self.recommendation_type_combobox.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(recommendation_tab, text="Title:").grid(row=1, column=0, padx=10, pady=5)
        self.recommendation_title_entry = tk.Entry(recommendation_tab, width=50)
        self.recommendation_title_entry.grid(row=1, column=1, padx=10, pady=5)

        search_button = ttk.Button(recommendation_tab, text="Search", command=self.get_recommendations)
        search_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.recommendation_results_text = tk.Text(recommendation_tab, height=15)
        self.recommendation_results_text.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10)

        self.recommendation_results_text.insert(tk.END, "Please enter a title to receive a recommendation.")
        # set default text

    def create_ratings_tab(self):
        ratings_tab = ttk.Frame(self.notebook)
        self.notebook.add(ratings_tab, text="Ratings")

        # Fetch the data for movie ratings and TV show ratings
        movie_ratings_data = self.recommender.get_movie_ratings()
        tv_show_ratings_data = self.recommender.get_tv_show_ratings()

        # Create the pie chart for Movie Ratings
        movie_fig, movie_ax = plt.subplots()
        movie_ax.pie(movie_ratings_data.values(), labels=movie_ratings_data.keys(), autopct='%1.2f%%', startangle=90)
        movie_ax.set_title('Movie Ratings Distribution')

        # Create the pie chart for TV Show Ratings
        tv_show_fig, tv_show_ax = plt.subplots()
        tv_show_ax.pie(tv_show_ratings_data.values(), labels=tv_show_ratings_data.keys(), autopct='%1.2f%%',
                       startangle=90)
        tv_show_ax.set_title('TV Show Ratings Distribution')

        # Create canvas widgets to embed the figures in the tkinter frame
        movie_canvas = FigureCanvasTkAgg(movie_fig, master=ratings_tab)  # Embed the figure in the tkinter window
        movie_canvas.draw()
        movie_canvas_widget = movie_canvas.get_tk_widget()
        movie_canvas_widget.grid(row=0, column=0, padx=10, pady=10)

        tv_show_canvas = FigureCanvasTkAgg(tv_show_fig, master=ratings_tab)
        tv_show_canvas.draw()
        tv_show_canvas_widget = tv_show_canvas.get_tk_widget()
        tv_show_canvas_widget.grid(row=0, column=1, padx=10, pady=10)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=0, sticky="ew")  # Ensure it expands only horizontally
        button_frame.config(bg='red')

        # Configure the buttons with uniform expansion
        buttons = ["Load Shows", "Load Books", "Load Associations", "Credit Info", "Quit"]
        commands = [self.loadShows, self.loadBooks, self.loadAssociations, self.credit_info_box, self.root.destroy]
        for i, (text, cmd) in enumerate(zip(buttons, commands)):
            btn = tk.Button(button_frame, text=text, command=cmd)
            btn.grid(row=0, column=i, sticky="ew")
            button_frame.grid_columnconfigure(i, weight=1)

    def loadShows(self):
        self.recommender.loadShows()
        movie_list, movie_stats = self.recommender.getMovieList(), self.recommender.getMovieStats()
        tv_show_list, tv_show_stats = self.recommender.getTVList(), self.recommender.getTVStats()
        self.movie_text.delete(1.0, tk.END)
        self.movie_text.insert(tk.END, movie_list)
        self.movie_stats_text.delete(1.0, tk.END)
        self.movie_stats_text.insert(tk.END, movie_stats)

        self.tv_show_text.delete(1.0, tk.END)
        self.tv_show_text.insert(tk.END, tv_show_list)
        self.tv_show_stats_text.delete(1.0, tk.END)
        self.tv_show_stats_text.insert(tk.END, tv_show_stats)

    def loadBooks(self):
        self.recommender.loadBooks()
        book_list, book_stats = self.recommender.getBookList(), self.recommender.getBookStats()
        self.book_text.delete(1.0, tk.END)
        self.book_text.insert(tk.END, book_list)
        self.book_stats_text.delete(1.0, tk.END)
        self.book_stats_text.insert(tk.END, book_stats)

    def loadAssociations(self):
        self.recommender.loadAssociations()

    def credit_info_box(self):
        messagebox.showinfo("Credit Info", "This program was created by [Your Team Members' Names] on [Completion Date]")

    def search_media(self):
        search_type = self.search_type_combobox.get()
        title = self.search_title_entry.get()
        director = self.search_director_entry.get()
        actor = self.search_actor_entry.get()
        genre = self.search_genre_entry.get()

        if search_type == "Movie":
            result = self.recommender.searchTVMovies("Movie", title, director, actor, genre)
        elif search_type == "TV Show":
            result = self.recommender.searchTVMovies("TV Show", title, director, actor, genre)
        else:
            result = "Please select Movie or TV Show from Type first."

        self.search_results_text.delete(1.0, tk.END)
        self.search_results_text.insert(tk.END, result)

    def get_recommendations(self):
        type = self.recommendation_type_combobox.get()
        title = self.recommendation_title_entry.get()

        if type == "Movie":
            result = self.recommender.getRecommendations("Movie", title)
        elif type == "TV Show":
            result = self.recommender.getRecommendations("TV Show", title)
        elif type == "Book":
            result = self.recommender.getRecommendations("Book", title)
        else:
            result = "Please select a type from the dropdown."

        self.recommendation_results_text.delete(1.0, tk.END)
        self.recommendation_results_text.insert(tk.END, result)

    def search_books(self):
        title = self.book_search_title_entry.get()
        author = self.book_search_author_entry.get()
        publisher = self.book_search_publisher_entry.get()

        result = self.recommender.searchBooks(title, author, publisher)

        self.book_search_results_text.delete(1.0, tk.END)
        self.book_search_results_text.insert(tk.END, result)

def main():
    app = RecommenderGUI()
    app.root.mainloop()

if __name__ == "__main__":
    main()

