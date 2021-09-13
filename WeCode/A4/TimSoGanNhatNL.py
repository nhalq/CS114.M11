import bisect

input()
arr = list(map(int, input().split()))
n = len(arr)

while True:
  try:
    k, value = map(int, input().split())
    right = min(n - 1, bisect.bisect_left(arr, value))

    left = max(0, right - k + 1)
    right = left + k - 1

    while (right + 1 < n) and (value - arr[left] > arr[right + 1] - value):
      left, right = left + 1, right + 1
    print(arr[left], arr[right])
  except: break
