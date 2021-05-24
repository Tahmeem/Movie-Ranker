
from imdb import IMDb,IMDbError
ia = IMDb()

def inputMovies():
    NumberOfEntries = input("How many movies would you like to add ")
    MovieNames = []
    for i in range(int(NumberOfEntries)):
        MovieNames.append(input("Enter the movie name: "))

def storeData(MovieNames):
    ratings = []
    movieDict = {}
    for i in MovieNames:
        movie = ia.search_movie(i)
        movie = movie[0].movieID
        curr_movie = ia.get_movie(movie)
        movieDict[i] = curr_movie.data['rating']
        ratings.append(curr_movie.data['rating'])
    return ratings,movieDict

def printOrder(ratings, movieDict):
    ratings.reverse()
    sortRanking(ratings, 0, len(ratings)-1)
    newMovieDict = {}
    for rating in ratings:
        for movieName in movieDict:
            if movieDict[movieName] == rating:
                newMovieDict[movieName] = rating
    return newMovieDict

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

#Using quicksort
def sortRanking(arr,left,right):
    if left > right:
        return
    p = partition(arr,left,right)
    sortRanking(arr, left, p-1)
    sortRanking(arr, p+1, right)

if __name__ == "__main__":
    inputMovies()
