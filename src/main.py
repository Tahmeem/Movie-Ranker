"""
from flask import Flask
from imdb import IMDb,IMDbError
ia = IMDb()

NumberOfEntries = input("How many movies would you like to add ")
MovieNames = []
for i in range(int(NumberOfEntries)):
    MovieNames.append(input("Enter the movie name: "))

ratings = []
for i in MovieNames:
    movie = ia.search_movie(i)
    movie = movie[0].movieID
    curr_movie = ia.get_movie(movie)
    ratings.append(curr_movie.data['rating'])


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
def sort(arr,left,right):
    if left > right:
        return
    p = partition(arr,left,right)
    sort(arr, left, p-1)
    sort(arr, p+1, right)



#if __name__ == '__main__':
    sort(ratings, 0, len(ratings)-1)
    print(ratings)
"""

