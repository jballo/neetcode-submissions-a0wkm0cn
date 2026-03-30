# Can we assume we maintain relative orders of the key for a stable sort?
# Is there a range for the keys for the pairs list?
# Can we assume we will have a large data set for pairs?
# Can we assume we will have at least 1 pair? 0 pairs?
# what do we wish to return if we have a pair list length of 0?
# Input:
#pairs = [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]

#Output:
#[(1, "date"), (2, "banana"), (5, "apple"), (9, "cherry"), (9, "elderberry")]



# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # use a helper function that will be the recursive mergeSort
        # return the pairs list call
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)


    # define and declare mergeSortHelper with parameters as self, pairs, start, end
    def mergeSortHelper(self, pairs, start, end):
        # check if the size of the array is 1 or 0 -> return pairs if true
        if end - start <= 0:  # [], [1]
            return pairs
        # calculate the index for the midpoint of the array
        midpoint = int( (start + end) / 2) #use int because we are using this as index
        # sort the array from the midpoint value to the start
        # aka sort left side
        self.mergeSortHelper(pairs, start, midpoint)
        # sort the right side of the array from the the value after the  to the end
        self.mergeSortHelper(pairs, midpoint+1, end)
        # merge the two sorted arrays using a function merge
        self.merge(pairs, start, end, midpoint)
        # return pairs
        return pairs


    # define and declare the function merge w/ parameters as self, pairs, start, end, midpoint
    def merge(self, pairs, start, end, midpoint):
        # define and declare array of left side of subarray (start to midpoint)
        left = pairs[start:midpoint+1]
        # define and eclare array of left side of subarray (midpoint + 1 to end)
        right = pairs[midpoint+1:end+1]

        # define pointers for...
        # pairs index, set to the start
        pairIndex = start
        # left array index, set to 0
        leftIndex = 0
        # right array index, set to 0
        rightIndex = 0

        # loop through the values of the left and right array until either left array index hits its length
        # or the right array index hits its length
        while leftIndex < len(left) and rightIndex < len(right):
            # in the loop, if the left array value's key is less than or equal to the right array's value key for their respective index
            if left[leftIndex].key <= right[rightIndex].key:
                # -> set the current position for pair to the left array value pair
                pairs[pairIndex] = left[leftIndex]
                # ->increment the left array index
                leftIndex += 1
            else:
                # if the condition failed 
                # -> set the current position for pair to the right array value pair 
                pairs[pairIndex] = right[rightIndex]
                # ->increment the right array index
                rightIndex += 1
            # increment the pairs index counter either way, increases after every override to pairs
            pairIndex += 1


        # loop through left array until its index hits left array's length
        while leftIndex < len(left):
            # set the current position for pair to the left array value pair
            pairs[pairIndex] = left[leftIndex]
            # increment left array index
            leftIndex += 1
            # increment the pair index
            pairIndex += 1
        
        # loop through right array until its index hits right array's length
        while rightIndex < len(right):
            # set the current position for pair to the right array value pair
            pairs[pairIndex] = right[rightIndex]
            # increment right array index
            rightIndex += 1
            # increment the pair index
            pairIndex += 1

