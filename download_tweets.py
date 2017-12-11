#!/usr/bin/python

import sys
import urllib
import re
import json
import csv

from bs4 import BeautifulSoup

import socket
socket.setdefaulttimeout(10)

cache = {}
ratings = {"negative" : 0.0, "neutral" : 0.33, "objective" : 0.66, "positive" : 1.0}
reg = re.compile('[^a-zA-Z ]')
try:
	with open("pr1.csv", "w") as file:
		writer = csv.writer(file)
		num_lines = sum(1 for line in open(sys.argv[1]))
		i = 1
		for line in open(sys.argv[1]):
			if i < 22144:
				i= i + 1
				continue
			fields = line.rstrip('\n').split('\t')
			sid = fields[0]
			uid = fields[1]
			start = int(fields[2])
			end = int(fields[3])
			rating = fields[4]
			tweet = None
			text = "Not Available"
			if cache.has_key(sid):
				text = cache[sid]
			else:
		                try:
		                        f = urllib.urlopen("http://twitter.com/%s/status/%s" % (uid, sid))
		                        #Thanks to Arturo!
		                        html = f.read().replace("</html>", "") + "</html>"
		                        soup = BeautifulSoup(html)
		
					jstt   = soup.find_all("p", "js-tweet-text")
					tweets = list(set([x.get_text() for x in jstt]))
					#print len(tweets)
					#print tweets
					if(len(tweets)) > 1:
						continue
		
					text = tweets[0]
					cache[sid] = tweets[0]
		
		                        for j in soup.find_all("input", "json-data", id="init-data"):
		                                js = json.loads(j['value'])
		                                if(js.has_key("embedData")):
		                                        tweet = js["embedData"]["status"]
		                                        text  = js["embedData"]["status"]["text"]
		                                        cache[sid] = text
		                                        break
		                except Exception:
		                        continue
		
		        if(tweet != None and tweet["id_str"] != sid):
	                    text = "Not Available"
	                    cache[sid] = "Not Available"
		        else:
	                    text = text.replace('\n', ' ',)
	                    text = re.sub(r'\s+', ' ', text)
	                    #print json.dumps(tweet, indent=2)
	                    #print "\t".join(fields + [text]).encode('utf-8')
                        wordList = re.sub("[^\w]", " ",  text).split()
                        subject = wordList[start : end + 1]
                        #word = " ".join(raw[start : end])
                        writer.writerow([" ".join(wordList).encode('utf-8'), " ".join(subject).encode('utf-8'), ratings[rating], start,end])
                        print "".join(str(i) + "/" + str(num_lines))
                        i = i + 1
	            
except KeyboardInterrupt:
    pass
         

            
            
            
            
            
            
