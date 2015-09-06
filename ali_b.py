def sortString(x='abc', n=2):
	step = n%len(x)
	return x[step:]+x[:step]

if __name__=="__main__":

	print sortString('abcdefg', 13)
