class Solution:
    def inversionCount(self, arr):
        def mergesort(arr):
            if len(arr) <= 1:
                return arr,0
            
            mid = len(arr) // 2
            
            left , count1 = mergesort(arr[:mid])
            right , count2 = mergesort(arr[mid:])
            
            merged = []
            i = j = 0
            count = count1 + count2
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += len(left) - i
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged,count
        return mergesort(arr)[1]