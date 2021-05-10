# sock_sorter.py
import random 

sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = {}
for i in range(100):
	sock = random.choice(sock_types)
	count = socks.get(sock, 0)
	socks[sock] = count + 1
	# # equivalent to above
	# if sock in socks:
	# 	socks[sock] += 1 
	# else:
	# 	socks[sock] = 1

print(socks)
for sock in sock_types:
	pairs = socks[sock] // 2
	loners = socks[sock] % 2
	print(f"{sock} has {pairs} pairs and {loners} loner(s).")


