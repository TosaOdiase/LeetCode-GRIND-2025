class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new_start, new_end = newInterval 
        added = False 
        for start, end in intervals:
            if end < new_start:
                result.append([start,end])
            elif start > new_end:
                if not added:
                    result.append([new_start, new_end])
                    added = True
                result.append([start, end])
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        if not added:
            result.append([new_start, new_end])
        return result
        
            