import jsonthings
import urllib.request
import urllib.parse
#http://api.joox.com/web-fcgi-bin//web_search?callback=jQuery110002187161929213639_1521547409166&lang=zh_TW&country=hk&type=0&search_input=songers&pn=1&sin=0&ein=29&_=1521547409167
def search(title, page):
    #this will return a json
    post_params = {
            'callback':'jQuery110002187161929213639_1521549409166',
            'lang':'zh_TW',
            'country':'hk',
            'type':0,
            'search_input':title,
            'pn':page,
            'sin':(page - 1) * 30,
            'ein':page * 30 - 1,
            '_':1521547409167
            }
    post_args = urllib.parse.urlencode(post_params)
    #raw = urllib.request.urlopen("http://api.joox.com/web-fcgi-bin//web_search?callback=jQuery110002187161929213639_1521547409166&lang=zh_TW&country=hk&type=0&search_input=songers&pn=1&sin=0&ein=29&_=1521547409167").read()
    raw = urllib.request.urlopen("http://api.joox.com/web-fcgi-bin//web_search?" + post_args).read()
    raw = raw.decode("utf-8")[42:-1]
    return raw
#orginial http://api.joox.com/web-fcgi-bin/web_get_songinfo?songid=8WxxfPdTbux5uWjGAsPDwA==&lang=zh_TW&country=hk&from_type=-1&channel_id=-1&_=1521548142238
def search_song(song_id, bitrate):
    #this will return a json
    post_params = {
            'songid': song_id,
            'lang':'zh_TW',
            'country':'hk',
            'form_type': -1,
            'channel_id': -1,
            '_':1521547409167
            }
    post_args = urllib.parse.urlencode(post_params)
    #raw = urllib.request.urlopen("http://api.joox.com/web-fcgi-bin//web_search?callback=jQuery110002187161929213639_1521547409166&lang=zh_TW&country=hk&type=0&search_input=songers&pn=1&sin=0&ein=29&_=1521547409167").read()
    raw = urllib.request.urlopen("http://api.joox.com/web-fcgi-bin/web_get_songinfo?" + post_args).read()
    #return raw.decode("utf-8").split('(')[1][:-1]
#MusicInfoCallback(
    not_so_raw = raw.decode("utf-8")[18:-1]
    #print(not_so_raw)
    if bitrate == 192:
        return jsonthings.get192(not_so_raw)
    elif bitrate == 320:
        return jsonthings.get320(not_so_raw)

def getWholeSongList(title):
    jsonthings.songlist(search(title, 1))

if __name__ == '__main__':

    getWholeSongList('songers')
    pass
