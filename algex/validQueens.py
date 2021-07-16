def nonAttackingQueens(n):
	nvalid = 0
	rows = [None] * n
	for i in range(n):
		rows[0] = i
		count = [0]
		backtrack(rows, 0, n, count)
		nvalid += count[0]
	return nvalid

def isValidPlacement(rows, rowIdx, n):
	colVal = rows[rowIdx]
	# curr = [rowIdx, colVal]
	for r in range(rowIdx):
		c = rows[r]
		if c == colVal:
			return False
		# \ diagonal
		cd1 = colVal - (rowIdx - r)
		if 0 <= cd1 < n and cd1 == c:
			return False
		# / diagonal
		cd2 = colVal + (rowIdx - r)
		if 0 <= cd2 < n and cd2 == c:
			return False
	return True

def isSolution(rows, n):
	return rows[-1] is not None

def printSolution(rows, n):
	for r in range(n):
		row = [1 if rows[r] == c else 0 for c in range(n)]
		print(row)
	print('-' * 2 * (n+1))

def backtrack(rows, row, n, count):
	if isSolution(rows, n):
		printSolution(rows, n)
		count[0] += 1
		return True

	# row is last PLACED row
	if row >= n:
		return False

	currRow = row + 1
	for colVal in range(n):
		rows[currRow] = colVal
		if isValidPlacement(rows, currRow, n):
			backtrack(rows, currRow, n, count)
		rows[currRow] = None
