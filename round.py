def round_up_to(son, l=0):
	son = str(son)
	drobi = son.split('.')
	if l == 0:
		if int(drobi[1][0]) >= 5:
			return int(drobi[0])+1
		return int(drobi[0])
	drob = drobi[1][:l]
	if len(drobi[1]) <= l:
		obj = "a string" 
		assert not isinstance(obj, str), ('Length of number is less than required.')
	if int(drobi[1][l+1]) <= 5:
		return float(drobi[0] + "." + str(int(drob)+1))
	vse = drobi[0] + "." + drob
	return float(vse)

print(round_up_to(2.1928374651123, 3))