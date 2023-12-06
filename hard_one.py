from collections import deque

def max_Sliding_Window(nums, k):
    result = []
    window = deque()

    for i in range(len(nums)):
        # Remove elements that are out of the current window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements that are smaller than the current element from the back
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # Add the current element's index to the window
        window.append(i)

        # Add the maximum element in the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


nums = input()
l=[]
for i in nums:
    if i.isdigit():
        e=int(i)
        l.append(e)
        
k = int(input())
output = max_Sliding_Window(l, k)
print(output)