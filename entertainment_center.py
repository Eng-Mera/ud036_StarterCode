# import media module that we created
import media
# import fresh_tomatoes module that
# takes list of movies and render the HTML file
import fresh_tomatoes

# Toy Story Movie Instance
toy_story = media.Movie("Toy Story",    # Movie Name
                        # Toy Story Storyline
                        "A story of a boy and his toys that come to life",
                        # Toy Story Poster
                        "https://lumiere-a.akamaihd.net/v1/images/c3c2b4a3323c4a71929cd5fc76bcda4df7157175.jpeg",  # noqa
                        # Toy Story Movie Trailer
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )

# Avatar Movie Instance
avatar = media.Movie("Avatar",  # Movie Name
                     # Avatar Storyline
                     "A marine on an alien planet",
                     # Avatar Poster
                     "http://www.joblo.com/posters/images/full/avatar-quad-1.jpg",  # noqa
                     # Avatar Movie Trailer
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# Inside out Movie Instance
inside_out = media.Movie("Inside Out",  # Movie Name
                         # Inside out Storyline
                         "A little girl and her emotions",
                         # Inside out Poster
                         "https://lumiere-a.akamaihd.net/v1/images/insideoutfamily-normal_e46cac6d.jpeg",  # noqa
                         # Inside out Movie Trailer
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")

# Ratatouille Movie Instance
ratatouille = media.Movie("Ratatouille",    # Movie Name
                          # Ratatouille Storyline
                          "Remy , The rat which love cooking",
                          # Ratatouille Poster
                          "https://www.gstatic.com/tv/thumb/movieposters/165058/p165058_p_v8_aj.jpg",  # noqa
                          # Ratatouille Movie Trailer
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

# Iron Man Movie Instance
iron_man = media.Movie("Iron Man",  # Movie Name
                       # Iron Man Storyline
                       "It is about Tony Stark",
                       # Iron Man Poster
                       "https://3.bp.blogspot.com/-NCBBGvzLUwo/UIZMyT0VSHI/AAAAAAAAAGc/BGWqK-56Q2U/s1600/IRON-MAN-3-Movie.jpg",  # noqa
                       # Iron Man Movie Trailer
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

# The Avengers Movie Instance
the_avengers = media.Movie("The Avengers",  # Movie Name
                           # The Avengers Storyline
                           "Superheros to make the world safer",
                           # The Avengers Poster
                           "https://a.ltrbxd.com/resized/sm/upload/8w/a1/14/qk/the-avengers-2012-1200-1200-675-675-crop-000000.jpg",  # noqa
                           # The Avengers Movie Trailer
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

# Big Hero Movie Instance
big_hero = media.Movie("Big Hero",  # Movie Name
                       # Big Hero Storyline
                       "Hamada, who team up with friends"
                       " to form a band of high-tech heroes",
                       # Big Hero Poster
                       "https://cdn.empireonline.com/jpg/80/0/0/1000/563/0/north/0/0/0/0/0/t/films/177572/images/2BXd0t9JdVqCp9sKf6kzMkr7QjB.jpg",  # noqa
                       # Big Hero Movie Trailer
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")

# Our Movies list
movies = [toy_story, avatar,
          inside_out, ratatouille,
          iron_man, the_avengers, big_hero]
"""
    Call open_movies_page method that takes list of movies
    and render the website HTML page
"""
fresh_tomatoes.open_movies_page(movies)
