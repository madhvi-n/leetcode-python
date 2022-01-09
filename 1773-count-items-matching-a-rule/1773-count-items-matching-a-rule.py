class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        value = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        count = 0
        for index, item in enumerate(items):
            if item[value[ruleKey]] == ruleValue:
                count += 1
            
        return count