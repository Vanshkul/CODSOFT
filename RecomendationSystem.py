import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")

cv = CountVectorizer()
matrix = cv.fit_transform(movies["genre"])

similarity = cosine_similarity(matrix)

def recommend(movie_name):

    if movie_name not in movies["title"].values:
        print("Movie not found!")
        return

    movie_index = movies[movies["title"] == movie_name].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nRecommended Movies:\n")

    for movie in movie_list:
        print(movies.iloc[movie[0]].title)

movie_name = input("Enter movie name: ")

recommend(movie_name)