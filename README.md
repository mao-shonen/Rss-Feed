# -RSS-Feed
搜尋不到使用簡單直覺的  
只好自己做一個 自己用的 功能很簡單
# 使用方法
輸出沒有格式化  
下面都是我從網頁取得的

## 基本
```python
from Rss import Rss, RssModule, RssData

rss = Rss('my rss web', 'http://google.com', '.....')
str(rss)
```
output:
```xml
<rss version="2.0">
  <channel>
    <title>my rss web</title>
    <link>http://google.com</link>
    <description>.....</description>
  </channel>
</rss>
```

## 增加幾個項目
```python
from Rss import Rss, RssModule, RssData
from time import time, mktime
from datetime import datetime

rss = Rss('my rss web', 'http://google.com', '.....')
t1 = mktime(datetime(1999, 12, 31, 23, 59, 59, 999999).timetuple()) #timestamp
t2 = mktime(datetime(2009, 12, 31, 23, 59, 59, 999999).timetuple()) #timestamp
t3 = time()

rss.add_item('a', 'http://google.com/a', 'you got a', t1)
rss.add_item('b', 'http://google.com/b', 'you got b', t2)
rss.add_item('c', 'http://google.com/c', 'you got c', 'c', t3, isPermaLink=False)
str(rss)
```
output:
```xml
<rss version="2.0">
    <channel>
        <title>my rss web</title>
        <link>http://google.com</link>
        <description>.....</description>
        <item>
            <title>a</title>
            <link>http://google.com/a</link>
            <description>you got a</description>
            <guid isPermaLink="true">http://google.com/a</guid>
            <pubDate>Fri, 31 Dec 1999 23:59:59 +0800</pubDate>
        </item>
        <item>
            <title>b</title>
            <link>http://google.com/b</link>
            <description>you got b</description>
            <guid isPermaLink="true">http://google.com/b</guid>
            <pubDate>Thu, 31 Dec 2009 23:59:59 +0800</pubDate>
        </item>
        <item>
            <title>c</title>
            <link>http://google.com/c</link>
            <description>you got c</description>
            <guid isPermaLink="false">http://google.com/c</guid>
            <pubDate>Sun, 15 Oct 2017 01:40:25 +0800</pubDate>
        </item>
    </channel>
</rss>
```

## 增加其他屬性
```python
from Rss import Rss, RssModule, RssData
from time import time, mktime
from datetime import datetime

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
str(rss)
```
output:
```xml
<rss version="2.0">
    <channel>
        <title>my rss web</title>
        <link>http://google.com</link>
        <description>.....</description>
        <item>
            <title>a</title>
            <link>http://google.com/a</link>
            <description>you got a</description>
            <guid isPermaLink="true">http://google.com/c</guid>
            <pubDate>Fri, 31 Dec 1999 23:59:59 +0800</pubDate>
            <author>admin@abc.com</author>
            <category a="fruit" b="apple"/>
        </item>
        <item>
            <title>b</title>
            <link>http://google.com/b</link>
            <description>you got b</description>
            <guid isPermaLink="true">http://google.com/c</guid>
            <pubDate>Thu, 31 Dec 2009 23:59:59 +0800</pubDate>
            <image item_name="image">
                <logo url="logo.jpg"/>
                <content author="tom@abc.com">a001.jpg</content>
            </image>
        </item>
        <item>
            <title>c</title>
            <link>http://google.com/c</link>
            <description>you got c</description>
            <guid isPermaLink="false">c</guid>
            <pubDate>Sun, 15 Oct 2017 01:44:45 +0800</pubDate>
            <item _from="c">
                <title>c1</title>
                <item _from="c1">
                    <title>c1-1</title>
                </item>
                <item _from="c1">
                    <title>c1-2</title>
                </item>
            </item>
            <item _from="c">
                <title>c2</title>
                <item _from="c2">
                    <title>c2-1</title>
                </item>
                <item _from="c2">
                    <title>c2-2</title>
                </item>
            </item>
        </item>
    </channel>
</rss>
```
