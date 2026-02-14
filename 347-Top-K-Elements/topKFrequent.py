class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make count of seen nums
        #2d array/list ie {1,2; 2,4; etc}
        #index doesn't matter
        #after filling 2d sort descending take top two
        #Need freq dictionary
        freq = {}
        #Makes list of freq
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        freq_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in freq_sorted[:k]]
