# Python3 program to find the maximum stolen value

# calculate the maximum stolen value
path_index = []
def maximize_loot(hval, n):
	if n == 0:
		return 0, path_index
	if n == 1:
		# path_index.append(n)
		return hval[0], path_index
	if n == 2:
		if hval[0] >= hval[1]:
			# path_index.append(0)
			return hval[0], path_index
		else:
			# path_index.append(1)
			return hval[1], path_index

	# dp[i] represent the maximum value stolen so
	# for after reaching house i.
	dp = [0]*n

	# Initialize the dp[0] and dp[1]
	dp[0] = hval[0]

	dp[1] = max(hval[0], hval[1])
	
	# Fill remaining positions
	for i in range(2, n):
		if hval[i]+dp[i-2] > dp[i-1]:
			dp[i] = hval[i] + dp[i - 2]
			path_index.append(i-2)
			# path_index.append(i)
		else:
			dp[i] = dp[i-1]
			path_index.append(i-1)

	return dp[-1], path_index

# Value of houses
hval = [6, 7, 1, 3, 8, 2, 4]

# number of houses
n = len(hval)
max, path = maximize_loot(hval, n)
print("Maximum loot value: ", max)
print("Index path: ", path)

