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

    item1 = rss.add_item('a', 'http://google.com/a', 'you got a', 'http://google.com/c', t1)
    item1.add('author', 'admin@abc.com')
    item1.add('category', a='fruit', b='apple')

    item2 = rss.add_item('b', 'http://google.com/b', 'you got b', 'http://google.com/c', t2)
    item2_1 = item2.add_item(item_name='image')
    item2_1.add('logo', url='logo.jpg')
    item2_1.add('content', 'a001.jpg', author='tom@abc.com')

    item3 = rss.add_item('c', 'http://google.com/c', 'you got c', 'c', t3, isPermaLink=False)
    item3_1 = item3.add_item('c1', _from='c')
    item3_1_1 = item3_1.add_item('c1-1', _from='c1')
    item3_1_2 = item3_1.add_item('c1-2', _from='c1')
    item3_2 = item3.add_item('c2', _from='c')
    item3_2_1 = item3_2.add_item('c2-1', _from='c2')
    item3_2_2 = item3_2.add_item('c2-2', _from='c2')
    
    return Response(str(rss), mimetype='text/xml')
   
app.run()