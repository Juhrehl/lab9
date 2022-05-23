import random

movie = {"Title":"Mad Max: Fury Road","Year":"2015","Rated":"R","Released":"15 May 2015","Runtime":"120 min","Genre":"Action, Adventure, Sci-Fi","Director":"George Miller","Writer":"George Miller, Brendan McCarthy, Nick Lathouris","Actors":"Tom Hardy, Charlize Theron, Nicholas Hoult","Plot":"In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max.","Language":"English, Russian","Country":"Australia, United States","Awards":"Won 6 Oscars. 247 wins & 233 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTdjYTA4OGUwZjMyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.1/10"},{"Source":"Rotten Tomatoes","Value":"97%"},{"Source":"Metacritic","Value":"90/100"}],"Metascore":"90","imdbRating":"8.1","imdbVotes":"966,247","imdbID":"tt1392190","Type":"movie","DVD":"01 Sep 2015","BoxOffice":"$154,109,060","Production":"N/A","Website":"N/A","Response":"True"}

def blog_generator (movie):
  blog = ""
  blog += headline_generator (movie["Title"])
  blog += first_paragraph (movie)
  return blog

def headline_generator (title):
  number = random.randint(0,2)
  if number == 0:
    title = "Is " + title + " the best action movie out there?"
  elif number == 1:
    title = "The making of " + title
  elif number == 2:
    title = "Why " + title + " should be on your watch list"
  return title+"\n\n"

def get_word():
  number = random.randint (0,2)
  if number == 0:
    return " an Australian filmmaker"
  elif number == 1:
    return " a famous"
  elif number == 2:
    return " an award winning filmmaker"

def first_paragraph (movie):
  return movie["Title"] + " was released in " + movie["Year"] + " It was directed by" + get_word() + " director, " + movie["Director"] + "." + " This movie takes place " + movie["Plot"] + " Throughout the years, this movie " + movie["Awards"] + "."
  

blog = blog_generator(movie)
print (blog)
  
  