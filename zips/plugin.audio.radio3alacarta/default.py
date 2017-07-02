#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, os, re, sys
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import dataparser

import zipfile


def ExtractAll(_in, _out):
    try:
        zin = zipfile.ZipFile(_in, 'r')
        zin.extractall(_out)
    except Exception, e:
        print str(e)
        return False

    return True


def Repo():
    if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.docshadrach')):
        return
        
    url = "https://github.com/XBMCSpot/docshadrach.repository/raw/master/zips/repository.docshadrach-1.0.zip"
    addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
    packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
    
    urllib.urlretrieve(url, packageFile)
    ExtractAll(packageFile, addonsDir)
        
    try:
        os.remove(packageFile)
    except:
        pass
            
    xbmc.executebuiltin("UpdateLocalAddons")
    xbmc.executebuiltin("UpdateAddonRepos")


Repo()



def MENU():
    
    addDir("[COLOR orange][B]CATEGORIAS:[/B][/COLOR]", "", "", "")
    addDir("- Músicas del mundo", 'IRRELEVANTE', 4, "")
    addDir("- Clásica", 'IRRELEVANTE', 5, "")
    addDir("- Culturales", 'IRRELEVANTE', 6, "")
    addDir("- Rock/Pop", 'IRRELEVANTE', 7, "")
    addDir("- Radio 3 Extra", 'IRRELEVANTE', 8, "")
    addDir("- Conciertos", 'IRRELEVANTE', 9, "")
    addDir("- Electrónica/Experimental", 'IRRELEVANTE', 10, "")
    addDir("- Jazz/Blues", 'IRRELEVANTE', 11, "")
    addDir("- HipHop/Funk", 'IRRELEVANTE', 12, "")
    addDir("", "", "", "")
    addDir("[COLOR cyan][B]LISTAR TODOS LOS PROGRAMAS[/B]  [A-Z][/COLOR]  <--", 'IRRELEVANTE', 1, "")
    addDir("[COLOR silver]--- [I]Escuchar Radio 3 en directo[/I] ---[/COLOR]", "http://radio3.rtveradio.cires21.com/radio3/mp3/icecast.audio?rnd=153691", 20, "")


def CAT4():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/musicas-del-mundo/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT5():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/clasica/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT6():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/culturales/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT7():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/rock-pop/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT8():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/radio-3-extra/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT9():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/conciertos/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT10():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/electronica-experimental/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT11():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/jazz-blues/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
        
def CAT12():  
     
    url='http://www.rtve.es/alacarta/programas/radio-3/hiphop-funk/1/?emissionFilter=all'
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
    
    for id,direc,name in match:
        
        rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                 
        addDir(name, rss, 2, "")
            


def PROGRAMAS():  
    page = 1
    while page <= 4:
        
        url='http://www.rtve.es/alacarta/programas/radio-3/todos/' + str(page) + '/?order=1&criteria=asc&emissionFilter=all'
        
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        
        match = re.compile('id="urlAddFav(.+?)" value="/(.+?)"/>\r\n\t\t<input type="hidden" id=".+?" value="(.+?)"/>').findall(link)
        
        for id,direc,name in match:
            
            rss = "http://api.rtve.es/api/programas/" +str(id) + "/audios.rss"
                     
            addDir(name, rss, 2, "")
            
        page = page + 1

       
                                  
def LISTADO_rss(url):  # MODE 1   
    req = urllib2.Request(url)
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    matches = dataparser.etiqueta_maestra(link, "<item>(.*?)</item>")
    for item in matches:
        NOMBRE = dataparser.subetiqueta(item, "<title>(.*?)</title>")
        LINK = dataparser.subetiqueta(item, '<enclosure url="(.+?)" length=".+?" type="audio/mpeg" />')
        addDir(NOMBRE, LINK, 20, "")

        


def AUDIOPLAY(url, name):  # MODE 20
    player = xbmc.Player()
    player.play(url)


        

               
def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params)-1]=='/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
                            
    return param
    



def addLink(name, url, iconimage):
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage = iconimage)
    xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = str(url), listitem = liz, isFolder=False)


def addDir(name, url, mode, iconimage):
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage = iconimage)
    liz.setInfo( type="Audio", infoLabels={ "Title": name } )
    xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = str(u), listitem = liz, isFolder=True)


             
params = get_params()
url = None
name = None
mode = None

try:
        url = urllib.unquote_plus(params["url"])
except:
        pass
try:
        name = urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode = int(params["mode"])
except:
        pass


print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)


if mode == None or url == None or len(url) < 1:
        print ""
        MENU()
        
elif mode == 1:
        print "" + url
        PROGRAMAS()

elif mode == 4:
        print "" + url
        CAT4()
        
elif mode == 5:
        print "" + url
        CAT5()

elif mode == 6:
        print "" + url
        CAT6()
        
elif mode == 7:
        print "" + url
        CAT7()
        
elif mode == 8:
        print "" + url
        CAT8()
        
elif mode == 9:
        print "" + url
        CAT9()
        
elif mode == 10:
        print "" + url
        CAT10()
        
elif mode == 11:
        print "" + url
        CAT11()
        
elif mode == 12:
        print "" + url
        CAT12()
       
elif mode == 2:
        print "" + url
        LISTADO_rss(url)
        
        
elif mode == 20:
        print "" + url
        AUDIOPLAY(url, name)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
