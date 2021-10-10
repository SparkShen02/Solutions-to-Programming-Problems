class Solution:
    """
    @param n: a number
    @param d: digit needed to be rorated
    @return: a number
    """
    def leftRotate(self, n, d):
        num=bin(n)[2:]
        while len(num)< 32:
            num='0'+num
        num=num[d:]+num[:d]
        return (int(num,2))