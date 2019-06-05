class Solution:
    def hIndexBinSrch(self, l , r):
        if l > r:
            return 0 
        if l == r and self.n - l <= self.citations[l]:
            return self.n - l
        m = (l+r)//2
        if self.n - m <= self.citations[m]:
            return self.hIndexBinSrch(l, m)
        else:
            return self.hIndexBinSrch(m+1, r)
        
    def hIndex(self, citations: List[int]) -> int:
        self.citations = citations
        self.n = len(citations)
        return self.hIndexBinSrch(0, self.n-1)
        
