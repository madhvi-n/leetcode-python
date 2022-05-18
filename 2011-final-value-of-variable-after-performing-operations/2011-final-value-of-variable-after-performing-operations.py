class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
#         counter = collections.Counter(operations)
#         print(counter)
        
#         for operation, count in counter.items():
#             if operation == "X++" or operation == "++X":
#                 x += (1 * counter.get(operation))
#             else:
#                 x -= (1 * counter.get(operation))
#         return x

        for operation in operations:
            if operation == "X++" or operation == "++X":
                x += 1
            else:
                x -= 1
        return x