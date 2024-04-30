import tkinter as tk
from tkinter import filedialog, messagebox
from typing import Self
from Book import Book
from Show import Show
import csv


class Recommender:
    def __init__(self):
        self.books = {}
        self.shows = {}
        self.associations = {}
    
    def loadBooks(self):
        while True:
            file_path = filedialog.askopenfilename(title="Select a book file",
                                                filetypes=[("Tab-delimited files", "*.csv")])
            if not file_path:
                return  # User cancelled the dialog
            try:
                with open(file_path, "r", newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    self.books = {}  # Assuming self.books is a dictionary
                    for row in reader:
                        try:
                            book = Book(
                                row['bookID'], 
                                row['title'], 
                                row['authors'], 
                                row['average_rating'], 
                                row['isbn'],
                                row['isbn13'],
                                row['language_code'], 
                                int(row['num_pages']), 
                                int(row['ratings_count']), 
                                row['publication_date'],
                                row['publisher']
                            )
                            self.books[row['bookID']] = book  # Assuming 'bookID' is the key to store in the dictionary
                        except ValueError as e:
                            print(f"Error converting book data: {e}")
                        except KeyError as e:
                            print(f"Missing expected column in data: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file: {e}")
                continue  # Allow the user to try again or cancel
            break  # Successfully loaded the data


    def loadShows(self):
        while True:

            file_path = filedialog.askopenfilename(title="Select a show file",
                                                   filetypes=[("Tab-delimited files", "*.csv")])
            if not file_path:
                return
            try:
                with open(file_path, "r", newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print("CSV Headers:", reader.fieldnames)
                    for row in reader:
                        try:
                            show = Show(row['show_id'], row['type'], row['title'], row['director'], row['cast'],
                                        row['average_rating'],
                                        row['country'], row['date_added'], row['release_year'], row['rating'],
                                        row['duration'],
                                        row['listed_in'], row['description'])
                            self.shows[row['show_id']] = show
                        except ValueError as e:
                            print(f"Error converting book data: {e}")
                        except KeyError as e:
                            print(f"Missing expected column in data: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file: {e}")
                continue
            break

    def loadAssociations(self):
        while True:
            file_path = filedialog.askopenfilename(title="Select an association file",
                                                   filetypes=[("Tab-delimited files", "*.csv")])
            if not file_path:
                return
            with open(file_path, "r", newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    id1, id2 = row
                    if id1 not in self.associations:
                        self.associations[id1] = {}
                    if id2 not in self.associations[id1]:
                        self.associations[id1][id2] = 0
                    self.associations[id1][id2] += 1

                    if id2 not in self.associations:
                        self.associations[id2] = {}
                    if id1 not in self.associations[id2]:
                        self.associations[id2][id1] = 0
                    self.associations[id2][id1] += 1
            break

    def getMovieList(self):
        if not any(show for show in self.shows.values() if show._show_type == 'Movie'): return "No movies found."
        max_title_length = max(len(show._title) for show in self.shows.values() if show._show_type == 'Movie')
        max_runtime_length = max(len(show._duration) for show in self.shows.values() if show._show_type == 'Movie')
        header = f"{'Title'.ljust(max_title_length + 2)}{'Runtime'.ljust(max_runtime_length + 2)}"
        movie_list = [header]
        for show in self.shows.values():
            if show._show_type == 'Movie':
                title = show._title.ljust(max_title_length + 2)
                runtime = show._duration.ljust(max_runtime_length + 2)
                movie_list.append(f"{title}{runtime}")
        return '\n'.join(movie_list)

    def getBookList(self):
        if not self.books:
            return "No books found."
        max_title_length = max(len(book._title) for book in self.books.values())
        max_authors_length = max(len(book._authors) for book in self.books.values())
        header = f"{'Title'.ljust(max_title_length + 2)}{'Author(s)'.ljust(max_authors_length + 2)}"
        book_list = [header]
        for book in self.books.values():
            title = book._title.ljust(max_title_length + 2)
            authors = book._authors.ljust(max_authors_length + 2)
            book_list.append(f"{title}{authors}")
        return '\n'.join(book_list)

    def getTVList(self):
        if not any(show for show in self.shows.values() if show._show_type == 'TV Show'):
            return "No TV shows found."
        max_title_length = max(len(show._title) for show in self.shows.values() if show._show_type == 'TV Show')
        max_seasons_length = max(len(show._duration) for show in self.shows.values() if
                                 show._show_type == 'TV Show')  # Assuming duration field holds seasons
        header = f"{'Title'.ljust(max_title_length + 2)}{'Seasons'.ljust(max_seasons_length + 2)}"
        tv_list = [header]
        for show in self.shows.values():
            if show._show_type == 'TV Show':
                title = show._title.ljust(max_title_length + 2)
                seasons = show._duration.ljust(max_seasons_length + 2)
                tv_list.append(f"{title}{seasons}")
        return '\n'.join(tv_list)

    def getMovieStats(self):
        from collections import Counter
        movies = [show for show in self.shows.values() if show._show_type == 'Movie']
        if not movies:
            return "No movies found."
        total_movies = len(movies)
        rating_counts = Counter(movie._rating for movie in movies)
        rating_percentages = {rating: f"{(count / total_movies) * 100:.2f}%" for rating, count in rating_counts.items()}
        # total_duration = sum(int(movie._duration) for movie in movies)
        total_duration = sum(int(movie._duration.replace('min', '').strip()) for movie in movies)
        average_duration = f"{total_duration / total_movies:.2f}"
        directors = Counter(movie._directors for movie in movies)
        most_common_director, most_director_count = directors.most_common(1)[0]
        actor_list = []
        for movie in movies:
            if movie._actors:
                actors = movie._actors.replace("\\", ",").split(',')
                actor_list.extend(actor.strip() for actor in actors)
        actors = Counter(actor_list)
        most_common_actor, most_actor_count = actors.most_common(1)[0] if actors else ("None", 0)
        # actors = Counter(actor for movie in movies for actor in movie._actors.split(', '))
        # most_common_actor, most_actor_count = actors.most_common(1)[0]
        genres = Counter(genre for movie in movies for genre in movie._genres.split(', '))
        most_common_genre, most_genre_count = genres.most_common(1)[0]
        stats = (
            f"Rating Percentages: {rating_percentages}\n"
            f"Average Movie Duration: {average_duration} minutes\n"
            f"Most Common Director: {most_common_director} ({most_director_count} movies)\n"
            f"Most Common Actor: {most_common_actor} ({most_actor_count} movies)\n"
            f"Most Frequent Genre: {most_common_genre} ({most_genre_count} occurrences)"
        )
        return stats

    def getTVStats(self):
        from collections import Counter
        tv_shows = [show for show in self.shows.values() if show._show_type == 'TV Show']
        if not tv_shows:
            return "No TV shows found."
        total_tv_shows = len(tv_shows)
        rating_counts = Counter(tv._rating for tv in tv_shows)
        rating_percentages = {rating: f"{(count / total_tv_shows) * 100:.2f}%" for rating, count in
                              rating_counts.items()}
        total_seasons = sum(int(tv._duration.split(' ')[0]) for tv in tv_shows)
        average_seasons = f"{total_seasons / total_tv_shows:.2f}"
        actor_list = []
        for tv_show in self.shows.values():
            if tv_show._actors:
                actors = tv_show._actors.replace("\\", ",").split(',')
                actor_list.extend(actor.strip() for actor in actors)
        actors = Counter(actor_list)
        most_common_actor, most_actor_count = actors.most_common(1)[0] if actors else ("None", 0)
        # actors = Counter(actor for tv in tv_shows for actor in tv._actors.split(', '))
        # most_common_actor, most_actor_count = actors.most_common(1)[0]
        genres = Counter(genre for tv in tv_shows for genre in tv._genres.split(', '))
        most_common_genre, most_genre_count = genres.most_common(1)[0]
        stats = (
            f"Rating Percentages: {rating_percentages}\n"
            f"Average Number of Seasons: {average_seasons}\n"
            f"Most Common Actor: {most_common_actor} ({most_actor_count} shows)\n"
            f"Most Frequent Genre: {most_common_genre} ({most_genre_count} occurrences)"
        )

        return stats

    def getBookStats(self):
        from collections import Counter
        if not self.books:
            return "No books found."

        total_pages = sum(int(book._num_pages) for book in self.books.values())
        total_books = len(self.books)
        average_pages = f"{total_pages / total_books:.2f}"
        # authors = Counter(author for book in self.books.values() for author in book._authors.split(', '))

        # most_common_author, most_author_books = authors.most_common(1)[0]
        # publishers = Counter(book._publisher for book in self.books.values())
        # most_common_publisher, most_publisher_books = publishers.most_common(1)[0]
        # stats = (
        #     f"Average Page Count: {average_pages}\n"
        #     f"Most Prolific Author: {most_common_author} ({most_author_books} books)\n"
        #     f"Most Prolific Publisher: {most_common_publisher} ({most_publisher_books} books)"
        # )
        # return stats
        author_list = []
        for book in self.books.values():
            authors = book._authors.replace("\\", ",").split(',')
            author_list.extend(author.strip() for author in authors)
        authors = Counter(author_list)
        most_common_author, most_author_books = authors.most_common(1)[0] if authors else ("None", 0)

        publishers = Counter(book._publisher for book in self.books.values())
        most_common_publisher, most_publisher_books = publishers.most_common(1)[0] if publishers else ("None", 0)

        stats = (
            f"Average Page Count: {average_pages}\n"
            f"Most Prolific Author: {most_common_author} ({most_author_books} books)\n"
            f"Most Prolific Publisher: {most_common_publisher} ({most_publisher_books} books)"
        )
        return stats

    def searchTVMovies(self, type, title, director, actor, genre):
        if type not in ['Movie', 'TV Show']:
            messagebox.showerror("Error", "Please select 'Movie' or 'TV Show' from Type first.")
            return "No Results"
        if not any([title, director, actor, genre]):
            messagebox.showerror("Error",
                                 "Please enter information for the Title, Director, Actor, and/or Genre first.")
            return "No Results"
        filtered_shows = [
            show for show in self.shows.values() if
            show._show_type == type and
            (title.lower() in show._title.lower() if title else True) and
            (director.lower() in show._directors.lower() if director else True) and
            (actor.lower() in show._actors.lower() if actor else True) and
            (genre.lower() in show._genres.lower() if genre else True)
        ]

        if not filtered_shows:
            return "No Results found."
        max_title_length = max(len(show._title) for show in filtered_shows)
        max_director_length = max(len(show._directors) for show in filtered_shows)
        max_actor_length = max(len(show._actors) for show in filtered_shows)
        max_genre_length = max(len(show._genres) for show in filtered_shows)
        header = f"{'Title'.ljust(max_title_length + 2)}{'Director'.ljust(max_director_length + 2)}" \
                 f"{'Actors'.ljust(max_actor_length + 2)}{'Genre'.ljust(max_genre_length + 2)}"
        result_lines = [header]
        for show in filtered_shows:
            title = show._title.ljust(max_title_length + 2)
            director = show._directors.ljust(max_director_length + 2)
            actors = show._actors.ljust(max_actor_length + 2)
            genre = show._genres.ljust(max_genre_length + 2)
            result_lines.append(f"{title}{director}{actors}{genre}")
        return '\n'.join(result_lines)

    def searchBooks(self, title, author, publisher):
        if not title and not author and not publisher:
            messagebox.showerror("Error", "Please enter information for the Title, Author, and/or Publisher first.")
            return "No Results"
        filtered_books = [
            book for book in self.books.values() if
            (title.lower() in book._title.lower() if title else True) and
            (author.lower() in book._authors.lower() if author else True) and
            (publisher.lower() in book._publisher.lower() if publisher else True)
        ]
        if not filtered_books:
            return "No Results found."
        max_title_length = max(len(book._title) for book in filtered_books)
        max_authors_length = max(len(book._authors) for book in filtered_books)
        max_publisher_length = max(len(book._publisher) for book in filtered_books)
        header = f"{'Title'.ljust(max_title_length + 2)}{'Author(s)'.ljust(max_authors_length + 2)}{'Publisher'.ljust(max_publisher_length + 2)}"
        result_lines = [header]
        for book in filtered_books:
            title_formatted = book._title.ljust(max_title_length + 2)
            authors_formatted = book._authors.ljust(max_authors_length + 2)
            publisher_formatted = book._publisher.ljust(max_publisher_length + 2)
            result_lines.append(f"{title_formatted}{authors_formatted}{publisher_formatted}")
        return '\n'.join(result_lines)

    def getRecommendations(self, media_type, title):
        if media_type in ['Movie', 'TV Show']:
            found_id = None
            for show_id, show in self.shows.items():
                if show.title == title and show.show_type == media_type:
                    found_id = show_id
                    break

            if not found_id:
                messagebox.showwarning("Warning", "No recommendations found for the given title.")
                return "No results"
            associated_books = self.associations.get(found_id, {})
            if not associated_books:
                return "No recommendations available."

            results = []
            for book_id in associated_books:
                book = self.books.get(book_id)
                if book:
                    results.append(f"Book Title: {book.title}, Author: {book.authors}, Publisher: {book.publisher}")
            return "\n".join(results) if results else "No results"

        elif media_type == 'Book':
            found_id = None
            for book_id, book in self.books.items():
                if book.title == title:
                    found_id = book_id
                    break

            if not found_id:
                messagebox.showwarning("Warning", "No recommendations found for the given title.")
                return "No results"
            associated_shows = self.associations.get(found_id, {})
            if not associated_shows:
                return "No recommendations available."

            results = []
            for show_id in associated_shows:
                show = self.shows.get(show_id)
                if show:
                    results.append(f"Show Title: {show.title}, Type: {show.show_type}, Directors: {show.directors}")
            return "\n".join(results) if results else "No results"

        else:
            messagebox.showwarning("Warning", "Invalid media type specified. Choose 'Movie', 'TV Show', or 'Book'.")
            return "Invalid media type"






