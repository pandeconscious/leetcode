class Solution(object):
    def max_product_no_zero(self, nums, neg_count, n):
	"""
	this function assumes there are no zeros in the array
	"""
        if nums:
            #if neg_count is even take the product
            if neg_count % 2 == 0:
		#if even number of negative elements are present just take the product of all the elements 
                return reduce(lambda x,y: x*y, nums, 1)
            else:
		#if odd number of negative elements are present then one of the negative number removal fromt he extermities is enough to get the largest product
                if n == 1:
                    return nums[0]#a corner case handling single negative element
                i, j = 0, n-1
                while nums[i] > 0:
                    i += 1
                while nums[j] > 0:
                    j -= 1
                return max(reduce(lambda x,y: x*y, nums[i+1:], 1), reduce(lambda x,y: x*y, nums[0:j], 1)) #this is the key point either the left most negative or rightmost negative has to go out
        else:
            return 0
        
    
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums:
            maxx = -(2**31 -1)

            prev = -1
            neg_count = 0
            total_count = 0

            for i, el in enumerate(nums):
                total_count += 1
                if el == 0:
                    maxx = 0 if 0 > maxx else maxx
                    curr_max = self.max_product_no_zero(nums[prev+1:i], neg_count, i-prev-1)
                    maxx = curr_max if curr_max > maxx else maxx
                    prev = i
                    neg_count = 0
                elif el < 0 :
                    neg_count += 1
                    
            #handle the pending last elements
            curr_max = self.max_product_no_zero(nums[prev+1:], neg_count, total_count-prev-1)
            maxx = curr_max if curr_max > maxx else maxx
            return maxx
        else:
            return 0
