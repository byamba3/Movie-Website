import media
import fresh_tomatoes
import urllib
import json
import ssl

# Pre-defined Movie objects for non API option

logan = media.Movie("Logan",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vgl"
                    "rh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",
                    "https://www.youtube.com/watch?v=f7kIl-Q1yrA")

wonder_woman = media.Movie("Wonder Woman",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCA"
                           "Omt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",
                           "https://www.youtube.com/watch?v=F0lZgaz0CIE")

kubo = media.Movie("Kubo and the Two Strings",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcRQeUx8alN89H9"
                   "qOSbfZY9sKwIOECZSYcz2LA3auB3bldJI-hmE",
                   "https://www.youtube.com/watch?v=ykD2W8U6wH4")

your_name = media.Movie("Your Name",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcR7gFSo85"
                        "szXEdjrPsBO992eUhkX0qwALaQWdCj-BOfcaU0kpH-",
                        "https://www.youtube.com/watch?v=7jJAOYsZQx8")

finding_dory = media.Movie("Finding Dory",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcTPxyox"
                           "zLf33_chM3uqooaT3tiyEBbQmqJb0Ndbvpt6qfQ4ybIk",
                           "https://www.youtube.com/watch?v=y19fAZrwJ88")

zootopia = media.Movie("Zootopia",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcQj1fU0-Idu"
                       "jcrs_MB2xEWbVEygeCkcjYUp4Z-hSIPqgu0vFbQi",
                       "https://www.youtube.com/watch?v=1ZOHlq6Qcz0")

moana = media.Movie("Moana",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewV"
                    "qmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS",
                    "https://www.youtube.com/watch?v=FG5K0_i9ZFA")

ex_machina = media.Movie("Ex Machina",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PT"
                         "MlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",
                         "https://www.youtube.com/watch?v=3hAlv0xLJJ4")

the_martian = media.Movie("The Martian",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EI"
                          "OafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
                          "https://www.youtube.com/watch?v=XQnYm5MG1x0")

mad_max = media.Movie("Mad Max: Fury Road",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcQuK41mExh1Qv"
                      "3kbXoxohWYGlcstOQ6zEnnNdSI2BGIKywQwgRI",
                      "https://www.youtube.com/watch?v=5wHRFvJNCW4")

gotg = media.Movie("Guardians of the Galaxy",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1P"
                   "ZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                   "https://www.youtube.com/watch?v=yM7VVKxjeag")

inside_out = media.Movie("Inside Out",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQ"
                         "xfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",
                         "https://www.youtube.com/watch?v=YEk_5aT5Gng")
# Add your pre-defined movies here:
predefined_movies = [logan, wonder_woman, kubo, your_name, finding_dory,
                     zootopia, moana, ex_machina, the_martian,
                     mad_max, gotg, inside_out]

# Returns a JSON data from a URL


def get_json_from_url(url):
    context = ssl._create_unverified_context()
    response = urllib.urlopen(url, context=context)
    data = json.load(response)
    return data

# Takes in a link and the API, then returns a movie array from the JSON


def get_movies_from_json(link, api):
    url = link + api
    json_movie_collection = get_json_from_url(url)

    movies = []

    for movie in json_movie_collection['results']:
        poster_url = "http://image.tmdb.org/t/p/w500//" + movie['poster_path']

        # Gets an additional JSON just for the trailer
        url_video = "http://api.themoviedb.org/3/movie/" + \
            str(movie['id']) + "/videos?api_key=" + api
        movie_video = get_json_from_url(url_video)
        trailer_url = "https://www.youtube.com/watch?v=" + \
            movie_video['results'][0]['key']

        temp_movie = media.Movie(
            movie['title'], poster_url, trailer_url)
        movies.append(temp_movie)

    return movies


# Main
print("Movie Website - Byamba3")
is_valid = False
api_base_url = "https://api.themoviedb.org/3/movie/popular?api_key="
api_key = "8e0615057ed71d85a782edf61f3a1a13"

all_movies = []

while is_valid is False:
    input_value = raw_input(
        'Do you want to use the API version? Enter Y or N: ')
    if str.lower(input_value) == 'y' or str.lower(input_value) == 'yes':
        print("Fetching live from MovieDB...")
        all_movies = get_movies_from_json(api_base_url, api_key)
        is_valid = True
    elif str.lower(input_value) == 'n' or str.lower(input_value) == 'no':
        # Adds pre-defined Movie objects here!
        all_movies = predefined_movies
        is_valid = True

fresh_tomatoes.open_movies_page(all_movies)
