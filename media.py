import webbrowser

class Movie():
    
    #Constructs a Movie object with title, storyline, poster image URL, and trailer URL
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Opens the movie's trailer in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
