# Can we assume a unsorted portion of length 1, is considered
# a succesful insertion?
# By relative order, do we mean we want a stable sort method?
# Using the Pair class, we can grab the key by using .key
# Are we limited to a certain time complexity?


#ex1: pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
#ex1: Output:
#[[(5, "apple"), (2, "banana"), (9, "cherry")], 
# [(2, "banana"), (5, "apple"), (9, "cherry")], 
# [(2, "banana"), (5, "apple"), (9, "cherry")]]

# Match: insertion with soft copies of a list

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
    
        #ex1: pairs = [(2, "banana"),(5, "apple"), (9, "cherry")]
        #ex1 test
        #[
        # [(5, "apple"), (2, "banana"), (9, "cherry")],
        # [(2, "banana"),(5, "apple"), (9, "cherry")],
        # [(2, "banana"),(5, "apple"), (9, "cherry")]
        #]
        
        
        # create a list for the list of pairs that is empty (aka storage)
        storage = []

        # S: O(N^2)
        # T: O(N^2)

        # iterate through the list of pairs from left, to right, starting at index 0
        for i in range(0, len(pairs)):
            # create inner index temp variable to outer index
            inner = i
            # while inner index - 1 >= 0 and key of pair at inner index is less than key of pair at inner index -1
            while inner - 1 >= 0 and pairs[inner].key < pairs[inner-1].key:
                # swap pairs between pair at inner inder index and inner index -1
                temp = pairs[inner]
                pairs[inner] = pairs[inner-1]
                pairs[inner-1] = temp
                # decrement the inner index
                inner -= 1
            # soft copy the pair onto the list storage
            storage.append(pairs[:])

        # return the storage
        return storage

            