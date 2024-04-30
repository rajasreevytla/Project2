import tkinter as tk
from tkinter import ttk, messagebox
from Recommender import Recommender

class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()

        self.root = tk.Tk()
        self.root.title("Media Recommender")
        self.root.geometry("1200x720")

        self.notebook = ttk.Notebook(self.root)  # 创建一个标签页容器
        self.notebook.pack(expand=True, fill="both")  # 将标签页容器添加到主窗口

        self.create_movie_tab()  # 创建电影标签页
        self.create_tv_show_tab()  # 创建电视节目标签页
        self.create_book_tab()  # 创建书籍标签页
        self.create_search_tab()  # 创建搜索标签页
        self.create_recommendation_tab()  # 创建推荐标签页

        self.create_buttons()  # 创建底部的按钮

    def create_movie_tab(self):
        movie_tab = ttk.Frame(self.notebook)  # 创建一个框架用于电影标签页
        self.notebook.add(movie_tab, text="Movies")  # 添加电影标签页到标签页容器

        self.movie_text = tk.Text(movie_tab)  # 创建一个文本框显示电影列表
        self.movie_text.pack(expand=True, fill="both")  # 添加文本框到电影标签页

        self.movie_stats_text = tk.Text(movie_tab)  # 创建一个文本框显示电影统计信息
        self.movie_stats_text.pack(expand=True, fill="both")  # 添加文本框到电影标签页


    def create_tv_show_tab(self):
        tv_show_tab = ttk.Frame(self.notebook)  # 创建一个框架用于电视节目标签页
        self.notebook.add(tv_show_tab, text="TV Shows")  # 添加电视节目标签页到标签页容器

        self.tv_show_text = tk.Text(tv_show_tab)  # 创建一个文本框显示电视节目列表
        self.tv_show_text.pack(expand=True, fill="both")  # 添加文本框到电视节目标签页

        self.tv_show_stats_text = tk.Text(tv_show_tab)  # 创建一个文本框显示电视节目统计信息
        self.tv_show_stats_text.pack(expand=True, fill="both")  # 添加文本框到电视节目标签页

    def create_book_tab(self):
        book_tab = ttk.Frame(self.notebook)  # 创建一个框架用于书籍标签页
        self.notebook.add(book_tab, text="Books")  # 添加书籍标签页到标签页容器

        self.book_text = tk.Text(book_tab)  # 创建一个文本框显示书籍列表
        self.book_text.pack(expand=True, fill="both")  # 添加文本框到书籍标签页

        self.book_stats_text = tk.Text(book_tab)  # 创建一个文本框显示书籍统计信息
        self.book_stats_text.pack(expand=True, fill="both")  # 添加文本框到书籍标签页

    def create_search_tab(self):
        search_tab = ttk.Frame(self.notebook)  # 创建一个框架用于搜索标签页
        self.notebook.add(search_tab, text="Search")  # 添加搜索标签页到标签页容器
        
        search_tab.grid_columnconfigure(0, weight=1)  # Labels column
        search_tab.grid_columnconfigure(1, weight=3)  # Entries column, minimal weight

        self.search_type_label = tk.Label(search_tab, text="Type:")  # 创建标签“类型”
        self.search_type_label.grid(row=0, column=0, sticky="w")  # 添加标签到搜索标签页
        self.search_type_combobox = ttk.Combobox(search_tab, values=["Movie", "TV Show"])  # 创建下拉菜单选择电影或电视节目
        self.search_type_combobox.grid(row=0, column=1, sticky="w")  # 添加下拉菜单到搜索标签页

        self.search_title_label = tk.Label(search_tab, text="Title:")  # 创建标签“标题”
        self.search_title_label.grid(row=1, column=0, sticky="w")  # 添加标签到搜索标签页
        self.search_title_entry = tk.Entry(search_tab)  # 创建输入框输入标题
        self.search_title_entry.grid(row=1, column=1, sticky="w")  # 添加输入框到搜索标签页

        self.search_director_label = tk.Label(search_tab, text="Director:")  # 创建标签“导演”
        self.search_director_label.grid(row=2, column=0, sticky="w")  # 添加标签到搜索标签页
        self.search_director_entry = tk.Entry(search_tab)  # 创建输入框输入导演姓名
        self.search_director_entry.grid(row=2, column=1, sticky="w")  # 添加输入框到搜索标签页

        self.search_actor_label = tk.Label(search_tab, text="Actor:")  # 创建标签“演员”
        self.search_actor_label.grid(row=3, column=0, sticky="w")  # 添加标签到搜索标签页
        self.search_actor_entry = tk.Entry(search_tab)  # 创建输入框输入演员姓名
        self.search_actor_entry.grid(row=3, column=1, sticky="w")  # 添加输入框到搜索标签页

        self.search_genre_label = tk.Label(search_tab, text="Genre:")  # 创建标签“类型”
        self.search_genre_label.grid(row=4, column=0, sticky="w")  # 添加标签到搜索标签页
        self.search_genre_entry = tk.Entry(search_tab)  # 创建输入框输入影片类型
        self.search_genre_entry.grid(row=4, column=1, sticky="w")  # 添加输入框到搜索标签页

        self.search_button = tk.Button(search_tab, text="Search", command=self.search_media)  # 创建搜索按钮
        self.search_button.grid(row=5, column=0, columnspan=2, sticky="w")  # 添加搜索按钮到搜索标签页

        # search_tab.grid_columnconfigure(0, weight=1)
        self.search_results_text = tk.Text(search_tab)  # 创建文本框显示搜索结果
        self.search_results_text.grid(row=6, column=0, columnspan=2, sticky="nsew")
        # search_tab.grid_rowconfigure(6, weight=1)
        # self.search_results_text.grid(row=6, column=0, columnspan=2)  # 添加文本框到搜索标签页

    def create_recommendation_tab(self):
        recommendation_tab = ttk.Frame(self.notebook)  # 创建一个框架用于推荐标签页
        self.notebook.add(recommendation_tab, text="Recommendations")  # 添加推荐标签页到标签页容器

        self.recommendation_type_label = tk.Label(recommendation_tab, text="Type:")  # 创建标签“类型”
        self.recommendation_type_label.grid(row=0, column=0)  # 添加标签到推荐标签页
        self.recommendation_type_combobox = ttk.Combobox(recommendation_tab, values=["Movie", "TV Show", "Book"])  # 创建下拉菜单选择电影、电视节目或书籍
        self.recommendation_type_combobox.grid(row=0, column=1)  # 添加下拉菜单到推荐标签页

        self.recommendation_title_label = tk.Label(recommendation_tab, text="Title:")  # 创建标签“标题”
        self.recommendation_title_label.grid(row=1, column=0)  # 添加标签到推荐标签页
        self.recommendation_title_entry = tk.Entry(recommendation_tab)  # 创建输入框输入标题
        self.recommendation_title_entry.grid(row=1, column=1)  # 添加输入框到推荐标签页

        self.recommendation_button = tk.Button(recommendation_tab, text="Get Recommendations", command=self.get_recommendations)  # 创建获取推荐按钮
        self.recommendation_button.grid(row=2, column=0, columnspan=2)  # 添加按钮到推荐标签页

        self.recommendation_results_text = tk.Text(recommendation_tab)  # 创建文本框显示推荐结果
        self.recommendation_results_text.grid(row=3, column=0, columnspan=2)  # 添加文本框到推荐标签页


    def create_buttons(self):
        button_frame = tk.Frame(self.root)  # Create a frame for the bottom buttons
        button_frame.pack(side='bottom', fill='x', padx=10, pady=10)  # Ensure it is at the bottom and visible

        load_shows_button = tk.Button(button_frame, text="Load Shows", command=self.load_shows)
        load_shows_button.pack(side="left", padx=5, pady=5)

        load_books_button = tk.Button(button_frame, text="Load Books", command=self.load_books)
        load_books_button.pack(side="left", padx=5, pady=5)

        load_associations_button = tk.Button(button_frame, text="Load Associations", command=self.load_associations)
        load_associations_button.pack(side="left", padx=5, pady=5)

        credit_info_button = tk.Button(button_frame, text="Credit Info", command=self.credit_info_box)
        credit_info_button.pack(side="left", padx=5, pady=5)

        quit_button = tk.Button(button_frame, text="Quit", command=self.root.destroy)
        quit_button.pack(side="left", padx=5, pady=5)

    def load_shows(self):
        self.recommender.loadShows()  # 调用推荐器加载节目数据
        movie_list, movie_stats = self.recommender.getMovieList(), self.recommender.getMovieStats()  # 获取电影列表和统计数据
        tv_show_list, tv_show_stats = self.recommender.getTVList(), self.recommender.getTVStats()  # 获取电视节目列表和统计数据

        self.movie_text.delete(1.0, tk.END)  # 清空电影文本框
        self.movie_text.insert(tk.END, movie_list)  # 插入电影列表到文本框
        self.movie_stats_text.delete(1.0, tk.END)  # 清空电影统计文本框
        self.movie_stats_text.insert(tk.END, movie_stats)  # 插入电影统计数据到文本框

        self.tv_show_text.delete(1.0, tk.END)  # 清空电视节目文本框
        self.tv_show_text.insert(tk.END, tv_show_list)  # 插入电视节目列表到文本框
        self.tv_show_stats_text.delete(1.0, tk.END)  # 清空电视节目统计文本框
        self.tv_show_stats_text.insert(tk.END, tv_show_stats)  # 插入电视节目统计数据到文本框

    def load_books(self):
        self.recommender.loadBooks()  # 调用推荐器加载书籍数据
        book_list, book_stats = self.recommender.getBookList(), self.recommender.getBookStats()  # 获取书籍列表和统计数据
        self.book_text.delete(1.0, tk.END)  # 清空书籍文本框
        self.book_text.insert(tk.END, book_list)  # 插入书籍列表到文本框
        self.book_stats_text.delete(1.0, tk.END)  # 清空书籍统计文本框
        self.book_stats_text.insert(tk.END, book_stats)  # 插入书籍统计数据到文本框

    def load_associations(self):
        self.recommender.loadAssociations()  # 调用推荐器加载关联数据

    def credit_info_box(self):
        messagebox.showinfo("Credit Info", "This program was created by [Your Team Members' Names] on [Completion Date]")  # 显示信用信息对话框

    def search_media(self):
        search_type = self.search_type_combobox.get()  # 获取选择的媒体类型
        title = self.search_title_entry.get()  # 获取输入的标题
        director = self.search_director_entry.get()  # 获取输入的导演
        actor = self.search_actor_entry.get()  # 获取输入的演员
        genre = self.search_genre_entry.get()  # 获取输入的类型

        if search_type == "Movie":  # 如果选择的是电影
            result = self.recommender.searchTVMovies("Movie", title, director, actor, genre)  # 调用推荐器搜索电影
        elif search_type == "TV Show":  # 如果选择的是电视节目
            result = self.recommender.searchTVMovies("TV Show", title, director, actor, genre)  # 调用推荐器搜索电视节目
        else:
            result = "Please select Movie or TV Show from Type first."  # 如果没有选择类型，则显示提示

        self.search_results_text.delete(1.0, tk.END)  # 清空搜索结果文本框
        self.search_results_text.insert(tk.END, result)  # 插入搜索结果到文本框

    def get_recommendations(self):
        recommendation_type = self.recommendation_type_combobox.get()  # 获取选择的推荐类型
        title = self.recommendation_title_entry.get()  # 获取输入的标题

        result = self.recommender.getRecommendations(recommendation_type, title)  # 调用推荐器获取推荐

        self.recommendation_results_text.delete(1.0, tk.END)  # 清空推荐结果文本框
        self.recommendation_results_text.insert(tk.END, result)  # 插入推荐结果到文本框

def main():
    app = RecommenderGUI()  # 创建推荐器GUI应用
    app.root.mainloop()  # 运行应用的主循环

if __name__ == "__main__":
    main()  # 如果是主程序，则运行main函数



