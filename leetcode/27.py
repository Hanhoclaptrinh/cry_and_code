class Solution:
    def removeElement(nums, val):
        # cho 2 con tro
        # 1 con tro tim phan tu can xoa
        # 1 con luu gia tri khong phai xoa
        
        # con tro luu gia tri khong phai xoa
        k=0
        
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k