def scrape_soi(filename):
	"""
	scrapes an soi file into a list of (possibly partial) rankings

	Args:
	filename- name of soi file to scrape
	"""
	L = []
	jj = 0		
	with open(filename,'r') as f:
		N = int(next(f))
		#print(N)
		if N<2:
			return [],0
		#sometimes the first candidate is labeled '1', sometimes '0'
		offset = int(next(f)[0])
		for _ in range(N):
			next(f)
			
		for line in f:
			l = line[:-1].split(',')
			count = int(l[0])
			sig = map(lambda x: int(x)-offset, l[1:])
			#print(len(list(sig)))
			#jj = jj+1
			#print(list(sig))
			print(l[0])
			
			for _ in range(count):
				#some election data had repeated "write-in" markers
				L.append(list(sig))

	return L,N



L,N = scrape_soi('sushi.soi')

print(N)
print(len(L))
print(str(L)[0:200])

