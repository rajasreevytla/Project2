class Media:
    def __init__(self, ID, title, average_rating):
        #create a function and initialize the media ID, title, and average rating
        self._ID = ID
        self._title = title
        self._average_rating = average_rating

    def get_ID(self):
        #access method
        return self._ID
    #return the id of media

    def get_title(self):
        return self._title
    #return the title of media

    def get_average_rating(self):
        return self._average_rating
    #return the average rating of media

    def set_title(self, title):
        self._title = title
        #update the title

    def set_average_rating(self, average_rating):
        self._average_rating = average_rating
        #update the average rate

    def __str__(self):
        return f"Media[ID={self._ID},Title={self._title},AverageRating={self._average_rating}]"


