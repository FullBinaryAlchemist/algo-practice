import unittest
###PROBLEM STATEMENT###
#Users on longer flights like to start a second movie right when their first one ends, but they complain that the plane usually lands before they can see the ending.
# So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

#Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and 
#returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

#When building your function:

#Assume your users will watch exactly two movies
#Don't make your users watch the same movie twice
#Optimize for runtime over memory

###Solution###
#space: O(n)
#time: O(n)
def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    dict_movie_lengths={}
    
    for movie_length in movie_lengths:
        if movie_length in dict_movie_lengths:
            dict_movie_lengths[movie_length]+=1
        else:
            dict_movie_lengths[movie_length]=1
    
    exists=False
    
    for movie_length in dict_movie_lengths:
        remaining= flight_length-movie_length
        try:
            if remaining != movie_length:
                exists= dict_movie_lengths[remaining]>0
            else:
                exists= (dict_movie_lengths[remaining]-1)>0
        except :
            pass
        
        if exists:
            break
            

    return exists

#TODO:
# What if we wanted the movie lengths to sum to something close to the flight length 
#(say, within 20 minutes)?
# What if we wanted to fill the flight length as nicely as possible with any number of movies 
#(not just 2)?
# What if we knew that movie_lengths was sorted? Could we save some space and/or time?

# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)