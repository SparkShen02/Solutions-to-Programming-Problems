class Solution:
    """
    @param arr: The release order
    @param n: The cooldown
    @return: Return the time
    """
    def askForCoolingTime(self, arr, n):
        def minus():
            for a in count:
                if count[a]!=0:
                    count[a]-=1
        def move():
            order.append(arr[i])
            minus()
            count[num]=n
        order=[]
        count={}
        for i in range(len(arr)):
            num=str(arr[i])
            if num not in count:
                move()
            else:
                while count[num]!=0:
                    order.append('_')
                    minus()
                move()
        print(order)
        return len(order)