# pip install mrjob
from mrjob.job import MRJob

class MovieRecommendation(MRJob):
    # Mapper: Extract movie_id for high ratings (>= 4)
    def mapper(self, _, line):
        # Skip the header row
        if line.startswith("user_id"):
            return
        
        # Split the line into fields
        user_id, movie_id, rating = line.split(',')
        
        # Only consider high ratings (>= 4)
        if int(rating) >= 4:
            yield movie_id, 1

    # Reducer: Count the number of high ratings for each movie
    def reducer(self, movie_id, counts):
        yield movie_id, sum(counts)

if __name__ == '__main__':
    MovieRecommendation.run()


# ratings.csv
user_id,movie_id,rating
1,101,4
2,102,3
3,101,5
4,103,2
5,101,4

# python prog14.py ratings.csv