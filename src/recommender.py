from math import sqrt


def cosine_similarity(vector_a, vector_b):
    # Compare equally sized vectors. Compare only co-rated movies in real data.
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length")

    dot = sum(a * b for a, b in zip(vector_a, vector_b))
    mag_a = sqrt(sum(a * a for a in vector_a))
    mag_b = sqrt(sum(b * b for b in vector_b))

    if mag_a == 0 or mag_b == 0:
        return 0.0

    return dot / (mag_a * mag_b)


def exclude_rated_movies(candidates, rated_movie_ids):
    rated = set(rated_movie_ids)
    return [movie for movie in candidates if movie["movie_id"] not in rated]
