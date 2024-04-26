from Media import Media

class Show(Media):
    def __init__(self, media_id, title, average_rating, show_type, directors, actors, country_code, date_added, release_year, rating, duration, genres, description):
        super().__init__(media_id, title, average_rating)
        self._show_type = show_type
        self._directors = directors
        self._actors = actors
        self._country_code = country_code
        self._date_added = date_added
        self._release_year = release_year
        self._rating = rating
        self._duration = duration
        self._genres = genres
        self._description = description
    def get_show_type(self):
        return self._show_type

    def get_directors(self):
        return self._directors

    def get_actors(self):
        return self._actors

    def get_country_code(self):
        return self._country_code

    def get_date_added(self):
        return self._date_added

    def get_release_year(self):
        return self._release_year

    def get_rating(self):
        return self._rating

    def get_duration(self):
        return self._duration

    def get_genres(self):
        return self._genres

    def get_description(self):
        return self._description

    # Mutator methods
    def set_show_type(self, show_type):
        self._show_type = show_type

    def set_directors(self, directors):
        self._directors = directors

    def set_actors(self, actors):
        self._actors = actors

    def set_country_code(self, country_code):
        self._country_code = country_code

    def set_date_added(self, date_added):
        self._date_added = date_added

    def set_release_year(self, release_year):
        self._release_year = release_year

    def set_rating(self, rating):
        self._rating = rating

    def set_duration(self, duration):
        self._duration = duration

    def set_genres(self, genres):
        self._genres = genres

    def set_description(self, description):
        self._description = description
