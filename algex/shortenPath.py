def shortenPath(path):
	pieces = path.split('/')
	res = []

	if path[0] == '/':
		res.append('')

	for piece in pieces:
		print(res)
		if piece == '.' or piece == '':
			continue
		if piece == '..':
			if not len(res) or res[-1] == '..':
				res.append('..')
			elif res[-1] != '':
				res.pop()
		else:
			res.append(piece)

	path = '/'.join(res)
	if not path:
		return '/'
	return path