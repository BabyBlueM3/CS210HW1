# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO AUTOLAB

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(filename):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    movieRatingDict = {}

    with open(filename, 'r') as f:
        for line in f:
            if line.strip():

                movie, rating, rater = line.split('|')  
                # If movie is not in dictionary, add it with an empty list
                rating = float(rating.strip())
            if movie not in movieRatingDict:
                movieRatingDict[movie] = []
            
            # Append rating to the movie's list
            movieRatingDict[movie].append(rating)

    #print(movieRatingDict)
    return(movieRatingDict) 
    
    

# 1.2
def read_movie_genre(filename):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    movieGenreDict = {}

    with open(filename, 'r') as f:
        for line in f:
            if line.strip():

                genre, id, movie = line.split('|')  
        
            # Append results to the movie's list
            movieGenreDict[movie.strip()] = genre.strip()
    
    # print(movieGenreDict) 
    
    return(movieGenreDict)


# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW


    genreDict = {}

    for movie,genre in d.items():
        if genre not in genreDict:
            genreDict[genre] = []
        genreDict[genre].append(movie)

    #print(genreDict)
    return(genreDict)

    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    ratingDict = {}

    for movie, rating in d.items():
        if rating:
            avgRating = sum(rating) / len(rating)
        ratingDict[movie] = avgRating

    #print(ratingDict)
    return(ratingDict)
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    topNMovies={}

    sortedMovies = sorted(d.items(), key=lambda x: x[1], reverse= True)

    for movie, rating in d.items():
        topNMovies = dict(sortedMovies[:n])
        

    #print(topNMovies)

    return(topNMovies)
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    filteredMovies = {}

    for movie, rating in d.items():
        if rating >= thres_rating:
            filteredMovies[movie] = rating

    #print(filteredMovies)
    return(filteredMovies)
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    newRatingDict = {}

    moviesInGenre = genre_to_movies.get(genre, [])

    movieRatings = [(movie, movie_to_average_rating[movie]) for movie in moviesInGenre if movie in movie_to_average_rating]

    sortedMovies = sorted(movieRatings, key=lambda x: x[1], reverse= True)

    newRatingDict = dict(sortedMovies[:n])

    #print(newRatingDict)
    return(newRatingDict)
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    genreRatingDict = {}
    count = 0
    newRating = 0

    moviesInGenre = genre_to_movies.get(genre, [])
    movieRatings = [(movie, movie_to_average_rating[movie]) for movie in moviesInGenre if movie in movie_to_average_rating]
    #print(movieRatings) 
    for movie, rating in movieRatings:
        newRating += rating
        count += 1
        #print(rating)

    #print(newRating)
    avgRating = newRating / count
    #print(avgRating)
    return(avgRating)


    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    genrePopDict = {}
    avgRating = 0
    
    for genre, movieInGenre in genre_to_movies.items():
        newRating = 0
        count = 0
        movieRatings = [(movie, movie_to_average_rating[movie]) for movie in movieInGenre if movie in movie_to_average_rating]
       #print(movieRatings)

        for movie, rating in movieRatings:
            newRating += rating
            count += 1
            if count > 0:
                    avgRating = newRating / count
            else:
                    avgRating = 0
        
        genrePopDict[genre] = avgRating
    
    genreRatingsort = sorted(genrePopDict.items(), key =lambda x:x[1], reverse = True)

    print(genreRatingsort)
    return(genreRatingsort)

    






# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    pass
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    pass
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    pass

# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading
    print("fuck")

    filename = "samplerating.txt"
    read_ratings_data(filename)

    averageRatingDict = read_ratings_data(filename)
    avgRating = calculate_average_rating(averageRatingDict)

    filter = get_popular_movies(avgRating)
    filter_movies(filter)



    filename = "samplemovies.txt"
    processingDict = read_movie_genre(filename)

    genreDict = create_genre_dict(processingDict)

    #get_popular_in_genre('Action', genreDict, avgRating)
    get_genre_rating('Action', genreDict, avgRating)

    genre_popularity(genreDict,avgRating)



    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()

    