import urllib
import urllib2
import requests
import os
import json
import smtplib
import email.MIMEMultipart
import email.MIMEText

print "Hello World!"

url = "https://leetcode.com/problemset/algorithms/"
url2 = "https://leetcode.com/api/problems/algorithms/"

response = urllib2.urlopen(url2)
data = json.load(response)
print data
print data['category_slug']
# print json.dumps(data, sort_keys=True, indent=4)
total = data['num_total']
print 'num_total is: ', total

Leetcode_count_file = "/tmp/leetcode_cnt.txt"

f = open(Leetcode_count_file, 'r')
previous_count = f.readline()
previous_count = int(previous_count)
print "previous_count is: "
print previous_count

if previous_count != total:
	print "previous_count != total"
	os.remove(Leetcode_count_file)
	print "old file removed"
	
	f = open(Leetcode_count_file, 'w')
	f.write(str(total))

	fromaddr = XXXX
	fromaddrPassword = YYYY
	toaddr = ZZZZ

	# server = smtplib.SMTP('smtp.gmail.com', 587)
	server = smtplib.SMTP_SSL('smtp.gmail.com:465')
	# server.ehlo()#this line is not needed! If uncommented, it'll throw exception!
	# server.starttls()#this line is not needed! If uncommented, it'll throw exception!
	# server.login("steve.j.sun@gmail.com", "Betrieber304")
	server.login(fromaddr, fromaddrPassword)#I've enabled less secure apps for this account, so it might now work on other accounts

	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Leetcode has new questions!"

	body = "Previous/Now: "
	body += str(previous_count)
	body += '/'
	body += str(total)
	msg.attach(MIMEText(body, 'plain'))
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()



print "It reached the end!"



