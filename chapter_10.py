import math

# Ratings by users for each movie
movies = {
    "Movie1": [5, 4, 5, 0, 1],
    "Movie2": [4, 5, 3, 0, 1],
    "Movie3": [1, 1, 3, 5, 5],
    "Movie4": [4, 0, 2, 3, 4],
    "Movie5": [4, 3, 5, 4, 4],
}


def cosine_similarity(movie1, movie2):
    # Get the ratings for each movie
    ratings1 = movies[movie1]
    ratings2 = movies[movie2]

    # Calculate the dot product
    dot_product = sum([ratings1[i] * ratings2[i] for i in range(len(ratings1))])

    # Calculate the magnitude of each vector
    magnitude1 = math.sqrt(sum([rating**2 for rating in ratings1]))
    magnitude2 = math.sqrt(sum([rating**2 for rating in ratings2]))

    # Calculate the cosine similarity
    result = dot_product / (magnitude1 * magnitude2)

    # Return the result
    return round(result, 2)


def recommend_movies(target_movie, movies, k=3):
    # Create a dictionary to store the similarity scores
    similarities = {}

    # Calculate the similarity score for each movie
    for movie in movies:
        if movie != target_movie:
            similarities[movie] = cosine_similarity(target_movie, movie)

    # Sort the movies by their similarity score
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)

    # Return the top k recommendations
    return sorted_similarities[:k]


print(recommend_movies("Movie1", movies))
# -> [('Movie5', 0.97), ('Movie3', 0.96), ('Movie2', 0.92)]
print(recommend_movies("Movie3", movies))
# -> [('Movie5', 0.97), ('Movie1', 0.96), ('Movie2', 0.92)]
print(recommend_movies("Movie5", movies))
# -> [('Movie1', 0.97), ('Movie3', 0.97), ('Movie2', 0.94)]
