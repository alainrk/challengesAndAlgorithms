'''
L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
'''

def longestIncreasingSubsequence(arr):
	n = len(arr)
	dp = [1] * n
	pred = [None] * n
	maxi = 0

	for i in range(n):
		for j in range(i):
			if arr[j] < arr[i] and dp[j] + 1 >= dp[i]:
				dp[i] = 1 + dp[j]
				pred[i] = j
			if dp[i] >= dp[maxi]:
				maxi = i

	res = []
	curr = maxi

	while curr is not None:
		res.append(arr[curr])
		curr = pred[curr]

	return list(reversed(res))