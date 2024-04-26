from Media import Media

class Book(Media):
    def __init__(self, media_id, title, average_rating, authors, isbn, isbn13, language_code, num_pages, ratings_count, pub_date, publisher):
        super().__init__(media_id, title, average_rating)
        #call the function and initialize
        self._isbn = isbn
        self._isbn13 = isbn13
        self._authors = authors
        self._num_pages = num_pages
        self._language_code = language_code
        self._publisher = publisher
        self._pub_date = pub_date
        self._ratings_count = ratings_count

    def get_authors(self):
        return self._authors

    def get_isbn(self):
        return self._isbn

    def get_isbn13(self):
        return self._isbn13

    def get_language_code(self):
        return self._language_code

    def get_num_pages(self):
        return self._num_pages

    def get_ratings_count(self):
        return self._ratings_count

    def get_pub_date(self):
        return self._pub_date

    def get_publisher(self):
        return self._publisher

    def set_authors(self, authors):
        self._authors = authors

    def set_isbn(self, isbn):
        self._isbn = isbn

    def set_isbn13(self, isbn13):
        self._isbn13 = isbn13

    def set_language_code(self, language_code):
        self._language_code = language_code

    def set_num_pages(self, num_pages):
        self._num_pages = num_pages

    def set_ratings_count(self, ratings_count):
        self._ratings_count = ratings_count

    def set_pub_date(self, pub_date):
        self._pub_date = pub_date

    def set_publisher(self, publisher):
        self._publisher = publisher

