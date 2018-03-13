import os
from bot import FilterBot
if os.path.isdir("data/") == False:
	print("Creating data directory")
	os.mkdir("data/")

try:
	f = open("data/token.data", "r")
	f.close()

except:
	f = open("data/token.data", "w+")
	token = input("No token found, please input token:\n")
	f.write(token)
	f.close()
	print("Token saved")
	time.sleep(1)

try:
	f = open("data/shard_count.data", "r")
	f.close()

except:
	print("No shard count detected")
	f= open("data/shard_count.data", "w+")
	shard_count = input("No shard count found, input shard count (not 0 based)\n")
	f.write(shard_count)

print("Booting...")

b = FilterBot()
b.run()
