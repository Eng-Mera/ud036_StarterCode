# import media module that we created
import media
# import fresh_tomatoes module that take list of movies and render HTML file
import fresh_tomatoes

# Toy Story Movie Instance
toy_story = media.Movie("Toy Story",    # Movie Name
                        "A story of a boy and his toys that come to life",  # Toy Story Storyline
                        "https://lumiere-a.akamaihd.net/v1/images/c3c2b4a3323c4a71929cd5fc76bcda4df7157175.jpeg?region=0%2C0%2C1024%2C320",  # Toy Story Poster
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"   # Toy Story Movie Trailer
                        )

# Avatar Movie Instance
avatar = media.Movie("Avatar",  # Movie Name
                     "A marine on an alien planet",  # Avatar Storyline
                     "http://www.joblo.com/posters/images/full/avatar-quad-1.jpg",  # Avatar Poster
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")     # Avatar Movie Trailer

# Inside out Movie Instance
inside_out = media.Movie("Inside Out",  # Movie Name
                         "A little girl and her emotions",  # Inside out Storyline
                         "https://lumiere-a.akamaihd.net/v1/images/insideoutfamily-normal_e46cac6d.jpeg",  # Inside out Poster
                         "https://www.youtube.com/watch?v=yRUAzGQ3nSY")     # Inside out Movie Trailer

# Ratatouille Movie Instance
ratatouille = media.Movie("Ratatouille",    # Movie Name
                          "Remy , The rat which love cooking",  # Ratatouille Storyline
                          "https://www.gstatic.com/tv/thumb/movieposters/165058/p165058_p_v8_aj.jpg",  # Ratatouille Poster
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")    # Ratatouille Movie Trailer

# Iron Man Movie Instance
iron_man = media.Movie("Iron Man",  # Movie Name
                       "It is about Tony Stark",  # Iron Man Storyline
                       "https://3.bp.blogspot.com/-NCBBGvzLUwo/UIZMyT0VSHI/AAAAAAAAAGc/BGWqK-56Q2U/s1600/IRON-MAN-3-Movie.jpg",  # Iron Man Poster
                       "https://www.youtube.com/watch?v=8hYlB38asDY")   # Iron Man Movie Trailer

# The Avengers Movie Instance
the_avengers = media.Movie("The Avengers",  # Movie Name
                           "Superheros to make the world safer",  # The Avengers Storyline
                           "https://a.ltrbxd.com/resized/sm/upload/8w/a1/14/qk/the-avengers-2012-1200-1200-675-675-crop-000000.jpg?k=3dc082c0fa",  # The Avengers Poster
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")   # The Avengers Movie Trailer

# Big Hero Movie Instance
big_hero = media.Movie("Big Hero",  # Movie Name
                       "Hamada, who team up with friends to form a band of high-tech heroes",  # Big Hero Storyline
                       "https://cdn.empireonline.com/jpg/80/0/0/1000/563/0/north/0/0/0/0/0/t/films/177572/images/2BXd0t9JdVqCp9sKf6kzMkr7QjB.jpg",  # Big Hero Poster
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")   # Big Hero Movie Trailer

# Our Movies list
movies = [toy_story, avatar,
          inside_out, ratatouille,
          iron_man, the_avengers, big_hero]
""" 
    Call open_movies_page method that takes list of movies 
    and render HTML page 
"""
fresh_tomatoes.open_movies_page(movies)
