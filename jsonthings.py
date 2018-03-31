import json
import time
import search
import base64
dummy = '''<li>
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
def songlist(raw_data):
    jsoned = json.loads(raw_data)
    x=1
    for i in jsoned['itemlist']:
        print(x)
        x += 1
        print(base64.b64decode(i['info1']).decode('UTF-8'))
        print(base64.b64decode(i['info2']).decode('UTF-8'))
        print(base64.b64decode(i['info3']).decode('UTF-8'))
        print(i['songid'])
    print("total:", jsoned['sum'])
def song_link_gen(url, title):
    return '''<a href=''' + url + '>' + title +'</a>'

def songlist_html(raw_data):
    jsoned = json.loads(raw_data)
    x=1
    text = ''''''
    for i in jsoned['itemlist']:
        song_length = time.strftime("%M:%S", time.gmtime(i['playtime']))
        song_link_320 = search.search_song(i['songid'], 320)
        song_link_192 = search.search_song(i['songid'], 192)
        text = text + '''<li>
        <ul class="item colum4">
<li class="num nohl">''' + str(x) + '''</li>
        <li class="album"><a class="album" u="/albumDetail?id=3836049">'''+ base64.b64decode(i['info3']).decode('UTF-8') +'''Take You Back</a></li>
        <li class="singer">
            <a u="/singer?id=1556314">'''+ base64.b64decode(i['info2']).decode('UTF-8') + '''
            </a>
        </li>
        <li class="song"><a class="name" u="/single?id='''+ i['songid'] + '''">'''+base64.b64decode(i['info1']).decode('UTF-8')+'''</a><div class="mini"><div class="mini-ctl"></span><span class="icons fav"></span></div></div></li>
    <li class="duration nohl">''' + song_length + '''</li><li><a href=http://www.joox.com/#/single?id=''' + i['songid'] + '''>Go to Joox</a></li><li> Download link : ''' + song_link_gen(song_link_192, "Download192bit") +"<br>" +song_link_gen(song_link_320, "Download320bit") +'''</li></ul></li>'''

   #    print(x)
        x += 1
   #    print(base64.b64decode(i['info1']).decode('UTF-8'))
   #    print(base64.b64decode(i['info2']).decode('UTF-8'))
   #    print(base64.b64decode(i['info3']).decode('UTF-8'))
   #    print(i['songid'])
   #print("total:", jsoned['sum'])
    return text
#AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz{}()[]!@#$%^&*--_=+/\'":,.
#'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz{}()[]!@#$%^&*--_=+/\'":,.'
def get192(raw_data):
    #print(raw_data)
    cleaned = ''.join( c for c in raw_data if c not in '\n')
    jsoned = json.loads(cleaned)
    return jsoned['r192Url']

def get320(raw_data):
    #print(raw_data)
    jsoned = json.loads(raw_data)
    return jsoned['r320Url']



if __name__ == '__main__':
    a = open('a.json', 'r')
    raw_data = a.read()
    #print(raw_data)
    jsoned = json.loads(raw_data)
#    print(jsoned['r192Url'])
#    print(jsoned['itemlist'][0]['info1'])
    songlist(raw_data)
#http://hk.stream.music.joox.com/C60000180jcm1YosQz.m4a?vkey=F81E509608905F542088238B54E7E9BB9DE30856F330C42763BEFA9655A26793&fromtag=8&guid=JO0X@WEB_OPENUDID
