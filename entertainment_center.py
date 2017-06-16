import media
import fresh_tomatoes
import urllib
import json
import ssl

#Pre-defined Movie objects for non API option

logan = media.Movie("Logan",
                    "In the near future, a weary Logan (Hugh Jackman) cares for an ailing Professor X (Patrick Stewart) at a remote outpost on the Mexican border. His plan to hide from the outside world gets upended when he meets a young mutant (Dafne Keen) who is very much like him. Logan must now protect the girl and battle the dark forces that want to capture her.",
                    "http://t1.gstatic.com/images?q=tbn:ANd9GcRPoMqL1vglrh7OF_69pT8gYMYnYaq1r7WfPMcD587V9uOR_hW2",
                    "https://www.youtube.com/watch?v=f7kIl-Q1yrA")

wonder_woman = media.Movie("Wonder Woman",
                           "Before she was Wonder Woman (Gal Gadot), she was Diana, princess of the Amazons, trained to be an unconquerable warrior. Raised on a sheltered island paradise, Diana meets an American pilot (Chris Pine) who tells her about the massive conflict that's raging in the outside world. Convinced that she can stop the threat, Diana leaves her home for the first time. Fighting alongside men in a war to end all wars, she finally discovers her full powers and true destiny.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAOmt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",
                           "https://www.youtube.com/watch?v=F0lZgaz0CIE")

kubo = media.Movie("Kubo and the Two Strings",
                   "Young Kubo's (Art Parkinson) peaceful existence comes crashing down when he accidentally summons a vengeful spirit from the past. Now on the run, Kubo joins forces with Monkey (Charlize Theron) and Beetle (Matthew McConaughey) to unlock a secret legacy. Armed with a magical instrument, Kubo must battle the Moon King (Ralph Fiennes) and other gods and monsters to save his family and solve the mystery of his fallen father, the greatest samurai warrior the world has ever known.",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcRQeUx8alN89H9qOSbfZY9sKwIOECZSYcz2LA3auB3bldJI-hmE",
                   "https://www.youtube.com/watch?v=ykD2W8U6wH4")

your_name = media.Movie("Your Name",
                        "A teenage boy and girl embark on a quest to meet each other for the first time after they magically swap bodies.",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcR7gFSo85szXEdjrPsBO992eUhkX0qwALaQWdCj-BOfcaU0kpH-",
                        "https://www.youtube.com/watch?v=7jJAOYsZQx8")

finding_dory = media.Movie("Finding Dory",
                           "Dory (Ellen DeGeneres) is a wide-eyed, blue tang fish who suffers from memory loss every 10 seconds or so. The one thing she can remember is that she somehow became separated from her parents as a child. With help from her friends Nemo and Marlin, Dory embarks on an epic adventure to find them. Her journey brings her to the Marine Life Institute, a conservatory that houses diverse ocean species. Dory now knows that her family reunion will only happen if she can save mom and dad from captivity.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcTPxyoxzLf33_chM3uqooaT3tiyEBbQmqJb0Ndbvpt6qfQ4ybIk",
                           "https://www.youtube.com/watch?v=y19fAZrwJ88")

zootopia = media.Movie("Zootopia",
                       "From the largest elephant to the smallest shrew, the city of Zootopia is a mammal metropolis where various animals live and thrive. When Judy Hopps (Ginnifer Goodwin) becomes the first rabbit to join the police force, she quickly learns how tough it is to enforce the law. Determined to prove herself, Judy jumps at the opportunity to solve a mysterious case. Unfortunately, that means working with Nick Wilde (Jason Bateman), a wily fox who makes her job even harder.",
                       "http://t2.gstatic.com/images?q=tbn:ANd9GcQj1fU0-Idujcrs_MB2xEWbVEygeCkcjYUp4Z-hSIPqgu0vFbQi",
                       "https://www.youtube.com/watch?v=1ZOHlq6Qcz0")

moana = media.Movie("Moana",
                    "An adventurous teenager sails out on a daring mission to save her people. During her journey, Moana meets the once-mighty demigod Maui, who guides her in her quest to become a master way-finder. Together they sail across the open ocean on an action-packed voyage, encountering enormous monsters and impossible odds. Along the way, Moana fulfills the ancient quest of her ancestors and discovers the one thing she always sought: her own identity.",
                    "http://t3.gstatic.com/images?q=tbn:ANd9GcTJOaSVrzlgewVqmUgUz4W5ty2KUeHH6s-aYSIr_Qw8v2EBrtCS",
                    "https://www.youtube.com/watch?v=FG5K0_i9ZFA")

ex_machina = media.Movie("Ex Machina",
                         "Caleb Smith (Domhnall Gleeson) a programmer at a huge Internet company, wins a contest that enables him to spend a week at the private estate of Nathan Bateman (Oscar Isaac), his firm's brilliant CEO. When he arrives, Caleb learns that he has been chosen to be the human component in a Turing test to determine the capabilities and consciousness of Ava (Alicia Vikander), a beautiful robot. However, it soon becomes evident that Ava is far more self-aware and deceptive than either man imagined.",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",
                         "https://www.youtube.com/watch?v=3hAlv0xLJJ4")
                        
the_martian = media.Movie("The Martian",
                          "When astronauts blast off from the planet Mars, they leave behind Mark Watney (Matt Damon), presumed dead after a fierce storm. With only a meager amount of supplies, the stranded visitor must utilize his wits and spirit to find a way to survive on the hostile planet. Meanwhile, back on Earth, members of NASA and a team of international scientists work tirelessly to bring him home, while his crew mates hatch their own plan for a daring rescue mission.",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ",
                          "https://www.youtube.com/watch?v=XQnYm5MG1x0")

mad_max = media.Movie("Mad Max: Fury Road",
                      "Years after the collapse of civilization, the tyrannical Immortan Joe enslaves apocalypse survivors inside the desert fortress the Citadel. When the warrior Imperator Furiosa (Charlize Theron) leads the despot's five wives in a daring escape, she forges an alliance with Max Rockatansky (Tom Hardy), a loner and former captive. Fortified in the massive, armored truck the War Rig, they try to outrun the ruthless warlord and his henchmen in a deadly high-speed chase through the Wasteland.",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcQuK41mExh1Qv3kbXoxohWYGlcstOQ6zEnnNdSI2BGIKywQwgRI",
                      "https://www.youtube.com/watch?v=5wHRFvJNCW4")

gotg = media.Movie("Guardians of the Galaxy",
                   "Brash space adventurer Peter Quill (Chris Pratt) finds himself the quarry of relentless bounty hunters after he steals an orb coveted by Ronan, a powerful villain. To evade Ronan, Quill is forced into an uneasy truce with four disparate misfits: gun-toting Rocket Raccoon, treelike-humanoid Groot, enigmatic Gamora, and vengeance-driven Drax the Destroyer. But when he discovers the orb's true power and the cosmic threat it poses, Quill must rally his ragtag group to save the universe.",
                   "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                   "https://www.youtube.com/watch?v=yM7VVKxjeag")

inside_out = media.Movie("Inside Out",
                         "Riley (Kaitlyn Dias) is a happy, hockey-loving 11-year-old Midwestern girl, but her world turns upside-down when she and her parents move to San Francisco. Riley's emotions -- led by Joy (Amy Poehler) -- try to guide her through this difficult, life-changing event. However, the stress of the move brings Sadness (Phyllis Smith) to the forefront. When Joy and Sadness are inadvertently swept into the far reaches of Riley's mind, the only emotions left in Headquarters are Anger, Fear and Disgust.",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",
                         "https://www.youtube.com/watch?v=YEk_5aT5Gng")
# Add your pre-defined movies here: 
predefined_movies = [logan, wonder_woman, kubo, your_name, finding_dory, zootopia, moana, ex_machina, the_martian, mad_max, gotg, inside_out]

# Returns a json data from a URL
def get_json_from_url(url):
    context = ssl._create_unverified_context()
    response = urllib.urlopen(url, context=context)
    data = json.load(response)
    return data

# Takes in a link and the api, then returns a movie array from the json
def get_movies_from_json(link, api):
    url = link + api
    json_movie_collection = get_json_from_url(url)
    
    movies = []
    
    for movie in json_movie_collection['results']:
        poster_url = "http://image.tmdb.org/t/p/w500//" + movie['poster_path']

        # Gets an additional JSON just for the trailer
        url_video = "http://api.themoviedb.org/3/movie/" + str(movie['id']) + "/videos?api_key=" + api
        movie_video = get_json_from_url(url_video)
        trailer_url = "https://www.youtube.com/watch?v=" + movie_video['results'][0]['key']
    
        temp_movie = media.Movie(movie['title'], movie['overview'], poster_url, trailer_url)
        movies.append(temp_movie)

    return movies

#Main
print("Movie Website - Byamba3")
is_valid = False
api_base_url= "https://api.themoviedb.org/3/movie/popular?api_key="
api_key = "8e0615057ed71d85a782edf61f3a1a13"

all_movies = []

while is_valid == False:
    input_value = raw_input('Do you want to use the API version? Enter Y or N: ')
    if str.lower(input_value) == 'y' or str.lower(input_value) == 'yes':
        print("Fetching live from MovieDB...")
        all_movies = get_movies_from_json(api_base_url, api_key)
        is_valid = True
    elif str.lower(input_value) == 'n' or str.lower(input_value) == 'no':
        # Adds pre-defined Movie objects here!
        all_movies = predefined_movies
        is_valid = True

fresh_tomatoes.open_movies_page(all_movies)




