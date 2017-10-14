from email.utils import formatdate


class RssData:
    def __init__(self, _id, *_content, **_attributes):
        self._id = _id
        self.content = list(_content)
        self.attributes = _attributes

    def __repr__(self):
        data = ['<', self._id]
        for key, value in self.attributes.items():
            data.extend([' ', key, '="', str(value), '"'])
        data.append('>')
        if len(self.content) > 0:
            for content in self.content:
                if type(content) == str:
                    if '<' in content or '&' in content:
                        data.extend(['<![CDATA[', content, ']]>'])
                    else:
                        data.append(content)
                else:
                    data.append(str(content))
        if len(self.content) > 0 or len(self.attributes) > 0:
            data.extend(['</', self._id, '>'])
        return ''.join(data)

    def add(self, _content):
        self.content.append(_content)
        return _content


class RssModule:
    def __init__(self, _id, title=None, link=None, description=None, guid=None, pubDate=None, **_attributes):
        guid_isPermaLink = 'true' if _attributes.get('isPermaLink', True) else 'false'
        if 'isPermaLink' in _attributes: del _attributes['isPermaLink']

        self.root = RssData(_id, **_attributes)
        if title        is not None: self.root.add(RssData('title', title))
        if link         is not None: self.root.add(RssData('link', link))
        if description  is not None: self.root.add(RssData('description', description))
        if guid         is not None: self.root.add(RssData('guid', guid, isPermaLink=guid_isPermaLink))
        if pubDate      is not None: self.root.add(RssData('pubDate', formatdate(pubDate, localtime=True)))

    def __repr__(self):
        return str(self.root)

    def add(self, _id, *_content, **_rssdatas):
        if type(_id) == RssModule:
            return self.root.add(_id)
        return self.root.add(RssData(_id, *_content, **_rssdatas))

    def add_item(self, *_content, **_attributes):
        item_name = _attributes.get('item_name', 'item')
        _content = list(_content)
        _content.insert(0, item_name)
        return self.root.add(RssModule(*_content, **_attributes))
        

class Rss:
    def __init__(self, title, link, description):
        self.xml = '<?xml version="1.0" encoding="utf-8" ?>'
        self.root = RssModule('rss', version='2.0')
        self.channel = self.root.add(RssModule('channel', title, link, description))
    
    def __repr__(self):
        return self.xml + str(self.root)

    def add(self, _id, *_content, **_attributes):
        return self.channel.add(_id, *_content, **_attributes)

    def add_item(self, *_content, **_attributes):
        return self.channel.add_item(*_content, **_attributes)
