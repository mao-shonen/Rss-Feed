from flask import Flask, Response
from Rss import Rss, RssModule, RssData
from time import time, mktime
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def main():
    rss = Rss('my rss web', 'http://google.com', '.....')
    t1 = mktime(datetime(1999, 12, 31, 23, 59, 59, 999999).timetuple()) #timestamp
    t2 = mktime(datetime(2009, 12, 31, 23, 59, 59, 999999).timetuple()) #timestamp
    t3 = time()

    rss.add_item('a', 'http://google.com/a', 'you got a', t1)
    rss.add_item('b', 'http://google.com/b', 'you got b', t2)
    rss.add_item('c', 'http://google.com/c', 'you got c', 'c', t3, isPermaLink=False)
    
    return Response(str(rss), mimetype='text/xml')
   
app.run()