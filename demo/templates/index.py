from ast import keyword
from crypt import methods
from xml.dom.expatbuilder import ParseEscape
from flask import Flask
from flask import render_template
from flask import request
from spider import getBdMsg
#Flask(__name__).run()
app = Flask(__name__)


@app.route('/')
def index() :
    return render_template('index.html')



@app.route('/juran')
def demo() :
    return 'hello world'

@app.route('/s')
def search():
    #return'搜索结果-一人之下'
    keyword = str(request.args.get('wd'))
    page = str(request.args.get('pn'))
    html = getBdMsg(keyword, page)
    return html



if __name__ == '__main__':

    app.run(debug=True,port=5500)