class Solution:
    '''
    Sort people from tall to short, and for the same height, from less people in front to more people in front. In this way, people[:i] contians all non-shorter people that could possibly be in front of people[i]. 
    Then, traverse people and insert each person into the appropriate position. 
    Time complexity: O(n^2), Space complexity: O(log(n)). 
    '''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1])) # time complexity: O(nlog(n)), space complexity O(log(n))
        for i in range(0, len(people)):
            person = people[i]
            people.insert(person[1], person)
            people.pop(i+1)
        return people