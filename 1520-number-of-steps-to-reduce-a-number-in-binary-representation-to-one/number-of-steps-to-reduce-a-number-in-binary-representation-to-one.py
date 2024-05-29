class Solution:
    def numSteps(self, s: str) -> int:
        l = len(s) - 1
        carry = 0
        count = 0
        while (l > 0):
            ##even number with carry = 0, result even
            if int(s[l]) + carry == 0:
                carry = 0
                count += 1
            ##odd number with carry = 1, result even
            elif int(s[l]) + carry == 2:
                carry = 1
                count += 1
            ##even number with carry = 1, result odd
            ##odd number with carry = 0, result odd
            else:
                carry = 1
                count += 2
            l -= 1
        #last digit 1 needs to add a carried over digit 1, which gives 10.
        #So need one more divide to make it 1 (one more step)
        if carry == 1:
            count += 1
        return count