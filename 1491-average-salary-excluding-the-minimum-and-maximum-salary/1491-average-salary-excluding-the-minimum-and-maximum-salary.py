class Solution:
    def average(self, salary: List[int]) -> float:
        max_index = salary.index(max(salary))
        salary.pop(max_index)
        
        min_index = salary.index(min(salary))
        salary.pop(min_index)
        
        return sum(salary) / len(salary) if len(salary) > 1 else salary[0]
        