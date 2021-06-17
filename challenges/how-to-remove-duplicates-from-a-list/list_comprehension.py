def is_dupe(item, counts):
	if item not in counts:
		counts[num] = 1
		return False
	else:
		return True
    
dupes = [1, 3, 8, 3, 5]
counts = dict()
dupes[:] = [item for item in dupes if not is_dupe(item, counts)]
