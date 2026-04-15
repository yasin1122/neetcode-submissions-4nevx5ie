class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        find the greatest element and replace all element before it with it
        find the greatest of the remaining elements,
            replace down to the greatest elements indicie the elements with it
            keep doing that till last element
        replace last element with -1
        return the array
        """
        # max_element = max(arr)
        # for i, num in enumerate(arr):
        #     if num != max_element:
        #         arr[i] = max_element
        #     else:
        #         max_element = max(arr[i+1:]) if i+1 < len(arr) else -1
        #         arr[i] = max_element
         
        # return arr

        rightMax = -1

        for i in reversed(range(len(arr))):
            arr[i], rightMax = rightMax, max(rightMax, arr[i])

        return arr