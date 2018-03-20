import webbrowser

class Movie():
    """
    Movie's class, create the data structure with title, poster image URL and trailer Youtube URL
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Class constructor

        :param title, poster_image_url, trailer_youtube_url
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
