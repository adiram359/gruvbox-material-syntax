import math

"""
Optimal O(nlogn) Solution:
"""

def numRescueBoats(people, limit):
        people.sort()
        num_boats = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            num_boats += 1
            right -= 1

        return num_boats
class Solution:

    def numRescueBoats(self, people, limit):
        """
        N = len(people)
        Runtime: O(NlogN)



        >>> Solution().numRescueBoats([1,2],3)
        1
        >>> Solution().numRescueBoats([3,2,2,1], 3)
        3
        >>> Solution().numRescueBoats([3, 5, 3,4], 5)
        4
        >>> Solution().numRescueBoats([3, 5, 3,4], 5)
        4
        """

        solo = people.count(limit)
        total = 0
        for person in people:
            if person < limit:
                total += 1
        return math.ceil(total/limit) + solo
        """
        people.sort()
        count = 0
        while people:
            fattest = people.pop()
            complement = limit - fattest
            i = self.findPartner(people, complement)
            if i != -1:
                people.pop(i)
            count += 1

        return count
        """


    def findPartner(self, people, target):
        l = 0
        r = len(people) - 1
        i = -1
        while l <= r:
            mid = (l + r)//2
            if people[mid] == target:
                return mid
            elif people[mid] < target:
                i = mid
                l = mid + 1
            else:
                r = mid - 1
        return i



if __name__ == "__main__":
    import doctest
    doctest.testmod()







    
