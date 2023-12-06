def majority_elements(nums):
    if not nums:
        return []

    # Initialize candidates and their counters
    cand1, count1 = None, 0
    cand2, count2 = None, 0

    # Count occurrences of candidates and update candidates
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0, 0
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1

    # Check if candidates meet the ⌊ n/3 ⌋ threshold
    result = []
    if count1 > len(nums) // 3:
        result.append(cand1)
    if count2 > len(nums) // 3:
        result.append(cand2)

    return result


nums1 = input()
l=[]
for i in nums1:
    if i.isdigit():
        e=int(i)
        l.append(e)

result1 = majority_elements(l)

print(result1)