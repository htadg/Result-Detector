import requests
from lxml import etree
from io import StringIO
import time
import sys

import gi

gi.require_version('Notify', '0.7')

from gi.repository import Notify

Notify.init("CBSE Class 10 Result Checker")

summary = "Got link"
body = ""
notification = None

def displayNotification(s):
	global summary
	global body
	if not s:
		try:
			notification.close()
		except:
			pass
	else:
		notification = Notify.Notification.new(summary, body)
		notification.show()
		time.sleep(10)
		sys.exit()


def check(url):
	global body
	res = requests.request('GET', url).text
	parser = etree.HTMLParser()
	tree = etree.parse(StringIO(res), parser)
	link = tree.xpath('/html/body/table[3]/tbody/tr/td[2]/table[2]/tbody/tr[1]/td/a/@href')[0]
	sys.stdout.flush()
	sys.stdout.write('.')
	if link != "#":
		print "Link Found: ", link
		body = link
		displayNotification(True)
	time.sleep(3)

print "Checking CBSE Class 10 Result..."

sys.stdout.write("[")
sys.stdout.flush()

while True:
	check('http://cbseresults.nic.in')
