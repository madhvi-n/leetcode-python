class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = defaultdict(int)

        def dfs(curr):
            # Base case
            if curr >= n:
                return 0
            
            points, brainpower = questions[curr][0], questions[curr][1]

            if curr in memo:
                return memo[curr]

            # Recurrence relation: to solve or to skip the current question?
            # Skip: move on to the next question
            
            skip = dfs(curr + 1)
            
            # Solve: collect the points from solving the current question, move on to the next question from brainpower
            solve = dfs(curr + brainpower + 1) + points
            
            # What is the best decision though?
            memo[curr] = max(skip, solve)

            return memo[curr]

        return dfs(0)