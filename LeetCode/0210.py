class Solution:
    '''
    Topological sort. 
    First, build a graph for the courses such that every course is pointed by its pre-requisites. 
    Then, apply Kahn's algorithm to sort the courses. 
    Last, check whether there is any edge in the graph. If so, the original graph must have at least one cycle, and thus a topological order cannot be formed. 
    Time complexity: O(V+E), Space complexity: O(V+E). 
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build graph
        nodeToChildren = [[] for course in range(numCourses)]
        numInEdges = [0 for course in range(numCourses)]
        for course, prereq in prerequisites:
            nodeToChildren[prereq].append(course)
            numInEdges[course] += 1
        
        # Kahn's algorithm
        order = []
        s = []
        for course in range(numCourses):
            if numInEdges[course] == 0:
                s.append(course)
        while s:
            course = s.pop()
            order.append(course)
            for nextCourse in nodeToChildren[course]:
                numInEdges[nextCourse] -= 1
                if numInEdges[nextCourse] == 0:
                    s.append(nextCourse)
        
        # Check for cycle
        for num in numInEdges:
            if num != 0:
                return []

        return order