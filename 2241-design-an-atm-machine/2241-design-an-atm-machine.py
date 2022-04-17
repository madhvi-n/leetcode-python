class ATM:
    
    def __init__(self):
        self.arr = [0, 0, 0, 0, 0]
        self.d = {0:20, 1:50, 2: 100, 3: 200, 4: 500}
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.arr[i] += banknotesCount[i]
            
    def withdraw(self, amount: int) -> List[int]:
        length = len(self.arr)
        ans = [0 for i in range(length)]

        k = length - 1
        # We start with k = 4 as the machine prioritizes using banknotes of larger values.
        while k >= 0 and amount > 0:
            note = self.d[k]
            if amount >= note and self.arr[k]:
                x = amount // note
                num = min(self.arr[k], x)
                ans[k] = num
                amount -= (note * num)
            k -= 1

        if amount == 0:
            for i in range(length):
                self.arr[i] -= ans[i]
            return ans
        else:
            return [-1]