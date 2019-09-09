#
# we have an array,
# Find all the combinations of N digits from the array that gives a sum of S
#

def all_combinations(arr, subarr, S, N):
    if S == 0 and len(subarr) == N:
        print(subarr)
        return 1
    if S < 0:
        return 0
    if not arr:
        return 0

    total = all_combinations(arr[1:], subarr, S, N) + all_combinations(arr[1:], subarr+[arr[0]], S-arr[0], N)
    return total

arr = [1,2,3,4,5,6,7,8,9,10]
print(all_combinations(arr,[], 15, 3))
