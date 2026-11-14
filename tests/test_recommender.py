import unittest
from src.recommender import cosine_similarity, exclude_rated_movies


class TestCosineSimilarity(unittest.TestCase):
    def test_identical_vectors(self):
        self.assertAlmostEqual(cosine_similarity([1, 2, 3], [1, 2, 3]), 1.0)

    def test_orthogonal_vectors(self):
        self.assertAlmostEqual(cosine_similarity([1, 0], [0, 1]), 0.0)

    def test_zero_vector(self):
        self.assertEqual(cosine_similarity([0, 0], [1, 2]), 0.0)

    def test_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            cosine_similarity([1, 2], [1])


class TestExcludeRatedMovies(unittest.TestCase):
    def test_excludes_rated_movies(self):
        candidates = [{"movie_id": 1}, {"movie_id": 2}, {"movie_id": 3}]
        self.assertEqual(exclude_rated_movies(candidates, [1, 3]), [{"movie_id": 2}])

    def test_empty_candidates(self):
        self.assertEqual(exclude_rated_movies([], [1]), [])


if __name__ == "__main__":
    unittest.main()
