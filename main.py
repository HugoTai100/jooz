from flask import Flask, request
import search
import jsonthings
app = Flask(__name__)
test = '''<li>
        <ul class="item colum4">
<li class="num nohl">29</li>
        <li class="album"><a class="album" u="/albumDetail?id=3836049">Take You Back</a></li>
        <li class="singer">
            <a u="/singer?id=1556314">
                Cale Dodds
            </a>
        </li>
        <li class="song"><a class="name" u="/single?id=L9CCT7cdepiTrGZvc1vQGQ==">Like We Do</a><div class="mini"><div class="mini-ctl"></span><span class="icons fav"></span></div></div></li>
    <li class="duration nohl">03:09</li></ul></li>'''
test1 = '''adsfa''' + '''adfadfasdfasdf'''

def hello_world():
    title = "其實我牽掛"
    return jsonthings.songlist_html(search.search(title, 1))
    #return search.search("songers", 1)
home_page = '''<form action="/search">
  Search for song:<br>
  <input type="text" name="name" value="">
  <br>
  <input type="submit" value="Submit">
</form>
'''
@app.route('/')
def home():
    return home_page
@app.route('/test')
def test():
    return search.search("adf",1)



@app.route('/search', methods=["GET","POST"])
def result():
    song_name = request.args.get('name')
    return "<h1>You have searched for</h1><br><h2>\"" + song_name + "\"</h2><br>"+ home_page + jsonthings.songlist_html(search.search(song_name, 1))

if __name__ == '__main__':

    app.run()
    #app.run(debug=True)
