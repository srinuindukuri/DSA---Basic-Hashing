# Hash Maps also knows as Dictionaries in Python..
# A Hash map is a dictionary that stores information as values and pairs them with a unique identifier called keys.

# ------------------------------------------------------------------------------------------------------------------

# Example: University GPA Database...

#      KEY    :      Value
#     19823   :      83%
#     23272   :      74%
#     72372   :      97%

# Example: Capital City Database...

#      KEY    :      Value
#    France   :     Paris
#    India    :     New Delhi
#    Japan    :     Tokyo

# ------------------------------------------------------------------------------------------------------------------

# Benefits of Hashmaps...
# 1) Custom keys are easier for software engineers to work with..
# 2) HashMaps allow for search in O(1), 
#    Whereas arrays/ linked lists are O(n)

# ------------------------------------------------------------------------------------------------------------------

# The common issue comes up with HashMaps is Collision
# Collision - It occurs when an hash function tries to assign a piece of data to an already used index.

# ------------------------------------------------------------------------------------------------------------------

# Main Thing About HashMaps Functions
# 1) Once they map data to a keys they cant change the key. This means any key in a HashMap always be immutable.
# 2) If you try to assign a immutable type key such as array.. it throws TypeError
#     To fix this simply try to convert this data type to an immutable type.. like "Tuple", which makes it immutable.

# ------------------------------------------------------------------------------------------------------------------

# In array if u want to find an city, it would have to search every index until it reaches the correct city.
# But in HashMap, the program just has to receive country name.
# Hash Function
#   France = index 0 
#   India  = index 1
#   Japan  = index 2
# database["Japan"] == ?? -> (2)

# ------------------------------------------------------------------------------------------------------------------

# Dictionary - All keys need to be initialized
# DefaultDict - All keys are already initialized --> This can be done from importing..
#                                                         from collections import defaultdict

# ------------------------------------------------------------------------------------------------------------------

# HashMaps: Retrieving Data
#        hashmap.keys() --> It returns all the keys from dictionary in the from of list 
#        hashmap.values() --> It returns all the values from dictionary in the list
#        hashmap.items() --> It returns lists of the all of the key value pairs as tuples

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

# Problem - Group Anagrams