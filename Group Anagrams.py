# Anagrams - Anagrams are words that are formed by similar elements but the orders in which these characters occur differ.
# Sometimes, we may encounter a problem in which we need to group the anagrams

# Method #1 : Using defaultdict() + sorted() + values()
# The combination of the above functions can be used to get the solution to the above problem.
# In this, we first get the anagrams grouped using defaultdict and use the sorted function to get each anagram root value to group anagrams.  

from collections import defaultdict
test_lists = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anagram = defaultdict(list)
result = []

for ele in test_lists:
    anagram[str(sorted(ele))].append(ele)
result = list(anagram.values())
print("The grouped anagrams: " + str(result))