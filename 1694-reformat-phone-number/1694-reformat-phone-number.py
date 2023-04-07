class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", " ").replace(" ", "")
        i = 0
        output = []
        length = len(number)
        
        while i < length:
            if i+4 == length:
                output.append(number[i:i+2])
                i = i+2
            elif i+3 <= length:
                output.append(number[i:i+3])
                i = i+3
            else:
                output.append(number[i:i+2])
                i = i+2
                
        if len(output) > 1:
            return "-".join(output)
        
        return output[0]