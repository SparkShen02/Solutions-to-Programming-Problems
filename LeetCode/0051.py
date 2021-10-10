class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.states = [None for i in range(n)]
        self.n = n
        self.count_sol = []

        def is_solution(index):
            return index == self.n

        def process_solution(index):
            sol = []
            for num in self.states:
                sol.append(num*"."+"Q"+(n-num-1)*".") 
            self.count_sol.append(sol)

        def construct_candidates(index):
            possibles = [True for i in range(n)]
            for i in range(0, index):
                possibles[self.states[i]]= False

                up = self.states[i]-(index-i)
                down = self.states[i]+(index-i)
                if up >= 0: possibles[up] = False
                if down < self.n: possibles[down] = False

            result = []
            for i in range(self.n):
                if possibles[i]:
                    result.append(i)
            return result

        def backtrack(index):
            if is_solution(index):
                process_solution(index)
            else:
                candidates = construct_candidates(index)
                for candidate in candidates:
                    self.states[index] = candidate
                    backtrack(index+1)

        backtrack(0)
        return self.count_sol