# Calculate loops


dkey = 10441485
value = 1
for loop1 in range(1, 20201227):
	value = (value * 7) % 20201227
	if value == dkey: break

# Calculate encryption key
ckey = 1004920
ekey = 1
for loop2 in range(0, loop1):
	ekey = (ekey * ckey) % 20201227

print('Encryption key:', ekey)