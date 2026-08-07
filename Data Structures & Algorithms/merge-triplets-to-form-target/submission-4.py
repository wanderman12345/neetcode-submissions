class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
      # if any triplet has a value in any element that is greater don;t look at i.
      I = False
      J = False 
      K = False
      for eachTriplet in triplets:
        if eachTriplet[0] > target[0] or eachTriplet[1] > target[1] or eachTriplet[2] > target[2]:
          continue

        if eachTriplet[0] == target[0]:
          I = True
        if eachTriplet[1] == target[1]:
          J = True
        if eachTriplet[2] == target[2]:
          K = True

      return I and J and K
      
        

    