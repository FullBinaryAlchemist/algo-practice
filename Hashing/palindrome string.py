import unittest


#Space(IMP):O(1) see note below for explanation
#Time: O(n) [n:legnth of string] since we are traversing through the string once 
def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    dict_chars={}
    
    for char in the_string:
        if char in dict_chars:
            dict_chars[char]+=1
        else:
            dict_chars[char]=1
    
    odds=0
    
    for char in dict_chars:
        if dict_chars[char]%2!=0:
            odds+=1
        if odds>1:
            return False
        

    return True

##Issues with Solution#1
#Possible issues with this solution in non-pythonic languages:
#Integer overflow if the count is too large

##Solution
#We only need to track the characters which appears odd number of times rather than their count
#So we use a set and add a character if it not there else remove a character if it is present(as even pairs)
#then check the length of set . If it is greater than 1 then return False

def has_palindrome_permutation2(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1


###Space Complexity:
#SInce we are maintaining a dictiorary character wise and there are at most 26 characters in english
#the length of our dictionary will be at most 26 i.e. O(k) = > O(1)

# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)