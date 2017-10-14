from flask import Flask, Response
from Rss import Rss, RssModule, RssData


app = Flask(__name__)

@app.route('/')
def main():
    rss = Rss('my rss web', 'http://google.com', '.....')

    return Response(str(rss), mimetype='text/xml')
   
app.run()