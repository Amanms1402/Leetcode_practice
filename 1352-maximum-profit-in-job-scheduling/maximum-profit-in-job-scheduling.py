class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        tbl = []
        for x, y, z in zip(startTime, endTime, profit):
            
            tbl.append([y, x, z])
        tbl.sort()
        endTime.sort()  
        @cache
        def dp(idx):
            if idx < 0:
                return 0 
            ans1 = dp(idx-1)
 
            nxt = bisect_left(endTime, tbl[idx][1])
            if tbl[nxt][0] > tbl[idx][1]:
                nxt -= 1
            elif tbl[nxt][0] == tbl[idx][1]:
                nxt = bisect_right(endTime, tbl[idx][1]) - 1
            ans2 = dp(nxt) + tbl[idx][2]
            return max(ans1, ans2)
        
        return dp(len(tbl)-1)