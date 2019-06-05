class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cits = sorted(citations, reverse=True)
        h_index = 0
        for ind, cit in enumerate(cits):
            if cit > ind:
                h_index = ind+1
            else:
                break
        return h_index
