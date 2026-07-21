from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1  

        arr = []
        for key, value in count.items():
            arr.append([value,key]) #swap key,value"

        arr.sort() #the highest will be at the end so that we can pop"

        res = []
        while len(res) < k:
            res.append(arr.pop()[1]) #only the input number index will return
        return res




        