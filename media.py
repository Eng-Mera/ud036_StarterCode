# import webbrowser module to open browser page
import webbrowser


class Movie:    # Define Movie Class
    """
        documentation of Movie Class

        Attributes :
            title (str): Hold the name of the movie
            storyline (str): Hold summary about the movie
            poster (str): Hold the movie poster link
            trailer (str): Hold the movie trailer youtube link

        Methods :
            show_trailer : to show the movie trailer in the browser
    """
    # init method that been called once we create new instance
    # and assign the values to the instance variables
    def __init__(self,  # the instance itself
                 movie_title,   # movie_title argument
                 movie_storyline,   # movie_storyline argument
                 movie_poster,  # movie_poster argument
                 movie_trailer  # movie_trailer argument
                 ):
        """
        __init__ method
        :param movie_title (str):
        :param movie_storyline (str):
        :param movie_poster (str):
        :param movie_trailer (str):
        """
        # Assign The arguments values to instance variables
        self.title = movie_title    # Assign movie_title argument to title instance variable
        self.storyline = movie_storyline    # Assign movie_storyline argument to storyline instance variable
        self.poster = movie_poster  # Assign movie_poster argument to poster instance variable
        self.trailer = movie_trailer    # Assign movie_trailer argument to trailer instance variable

    """
        show_trailer method 
        
        Arguments :
            self : the instance itself 
        
        Return : 
            void method that don't return anything
            but it open the web browser with the movie trailer link
    """
    def show_trailer(self):
        # call open method from webbrowser module
        webbrowser.open(self.trailer)

