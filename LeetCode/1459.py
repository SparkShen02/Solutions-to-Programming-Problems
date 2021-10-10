class Solution:
    '''
    Covered area = area of a + area of b - intersection area of a and b
    Intersection area of a and b = the intersection length of the line from aBotLeft to aBotRight and the line from bBotLeft to bBotRight * the intersection length of the line from aBotLeft to aTopLeft and the line from bBotLeft to bTopLeft. 
    Time complexity: O(1), Space complexity: O(1). 
    '''
    def computeArea(self, aBotLeftX: int, aBotLeftY: int, aTopRightX: int, aTopRightY: int, bBotLeftX: int, bBotLeftY: int, bTopRightX: int, bTopRightY: int) -> int:
        aBotRightX, aBotRightY = aTopRightX, aBotLeftY
        aTopLeftX, aTopLeftY = aBotLeftX, aTopRightY
        bBotRightX, bBotRightY = bTopRightX, bBotLeftY
        bTopLeftX, bTopLeftY = bBotLeftX, bTopRightY

        def recArea(botLeftX, botRightX, botRightY, topRightY):
            return (botRightX - botLeftX) * (topRightY - botRightY)
        def intersectionLen(a1, a2, b1, b2):
            if a1 > b2 or b1 > a2:
                return 0
            return min(a2, b2) - max(a1, b1)

        aArea, bArea = recArea(aBotLeftX, aBotRightX, aBotRightY, aTopRightY), recArea(bBotLeftX, bBotRightX, bBotRightY, bTopRightY)
        intersectArea = intersectionLen(aBotLeftX, aBotRightX, bBotLeftX, bBotRightX) * intersectionLen(aBotLeftY, aTopLeftY, bBotLeftY, bTopLeftY)
        return aArea + bArea - intersectArea