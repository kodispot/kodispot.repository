#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib,urllib2,os,re,sys,zipfile
import urlresolver,xbmc,xbmcaddon,xbmcgui,xbmcplugin


Config = xbmcaddon.Addon()

dialog = xbmcgui.Dialog()


path = os.path.join(xbmcaddon.Addon().getAddonInfo('path'))

info = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.shareit', 'info.txt'))


# logpath = str(path).split('addons')

logpath = xbmc.translatePath(os.path.join("special://logpath/", "kodi.log"))

if logpath is file:
    xbmclog = logpath
else:
    logpath = xbmc.translatePath(os.path.join("special://logpath/", "xbmc.log"))
    xbmclog = logpath

print "path ----> " + xbmclog


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


def TextBoxes(heading,anounce):
    class TextBox():
        """Thanks to BSTRDMKR for this code:)"""
            # constants
        WINDOW = 10147
        CONTROL_LABEL = 1
        CONTROL_TEXTBOX = 5

        def __init__( self, *args, **kwargs):
            # activate the text viewer window
            xbmc.executebuiltin( "ActivateWindow(%d)" % ( self.WINDOW, ) )
            # get window
            self.win = xbmcgui.Window( self.WINDOW )
            # give window time to initialize
            xbmc.sleep( 500 )
            self.setControls()

        def setControls( self ):
            # set heading
            self.win.getControl( self.CONTROL_LABEL ).setLabel(heading)
            try:
                f = open(anounce)
                text = f.read()
            except: text=anounce
            self.win.getControl( self.CONTROL_TEXTBOX ).setText(text)
            return
    TextBox()


def Notify():
    dir = os.path.join(xbmcaddon.Addon().getAddonInfo('path'))
    info = os.path.join(dir, 'info.txt')
    TextBoxes("[B][COLOR red]SHARE IT[/B][/COLOR]",info)



def getInfo(id):
    
    url = "https://www.themoviedb.org/search?query=" + id
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read()
    response.close()
    
    try:
        match = re.compile('<div class="poster">\n          <a href=".+?" title=".+?"><img class=".+?" src="(.+?)" width=".+?"></a>\n        </div>\n        <div class=".+?">\n          <h3><a href=".+?" title=".+?">(.+?)</a><span>(.+?)</span></h3>').findall(link)
    
        for thb,nam1,nam2 in match:
            img = thb.split('/')
            thumb = "https://"+img[2]+"/"+img[3]+"/"+img[4]+"/original/"+img[6]
            name = nam1+nam2
    
        return name,thumb
    
    except:
        dialog.ok('ERROR', 'Could not find the movie info. Check IMDb id.')
        name = ""
        thumb = ""
        return name,thumb


def lastDVD():
    
    DVD_list = []
    
    name = ""
    thumb = ""
    
    """
    with open(xbmclog) as f:
        for line in f:
            if "http://" in line:
                 print line
    """

    opciones = open(xbmclog, "r+")
    contenido = opciones.read()
    
    DVD = re.compile('NOTICE: DVDPlayer: Opening: (.*)').findall(contenido)
    
    if DVD == []:
        dialog.ok('ERROR', 'You have to run a movie first.')
        sys.exit()
    
    else:
    
        for link in DVD:
            
            print "LINE " + link
            DVD_list.append(link)
            
        
        last = DVD_list[int(len(DVD_list))-1]
                 
        print "LAST " + DVD_list[int(len(DVD_list))-1]
        
        
        ret = dialog.select('Choose an option', ['-- [B]XML[/B] format', '-- [B]PLX[/B] format', '-- [B]M3U[/B] format', '[I]Just the LINK[/I]'])
        
        if ret == 0:
            # XML
            kb = xbmc.Keyboard('',"Add 'Movie Name' or 'IMDb id'",False)
            kb.setDefault()
            kb.doModal()
            if (kb.isConfirmed()):
                name = kb.getText()
                isornot = re.search("tt[0-9][0-9][0-9][0-9][0-9][0-9][0-9]", name)
                if isornot == None:
                    pass
                else:
                    name, thumb = getInfo(isornot.group(0))
            else:
                name = ""
                pass
        
            tags = "<item><title>"+name+"</title><link>"+last+"</link><thumbnail>"+thumb+"</thumbnail></item>"
            
            kb = xbmc.Keyboard('','Use Yatse to copy your tags easily',False)
            kb.setDefault(tags)
            kb.doModal()
            if (kb.isConfirmed()):
                sys.exit()
            else: sys.exit()
        
        
        elif ret == 1:
            # PLX
            kb = xbmc.Keyboard('',"Add 'Movie Name' or 'IMDb id'",False)
            kb.setDefault()
            kb.doModal()
            if (kb.isConfirmed()):
                name = kb.getText()
                isornot = re.search("tt[0-9][0-9][0-9][0-9][0-9][0-9][0-9]", name)
                if isornot == None:
                    pass
                else:
                    name, thumb = getInfo(isornot.group(0))
            else:
                name = ""
                pass
        
            tags = "type=video name="+name+" thumb="+thumb+" URL="+last
            
            
            kb = xbmc.Keyboard('','Use Yatse to copy your tags easily',False)
            kb.setDefault(tags)
            kb.doModal()
            if (kb.isConfirmed()):
                sys.exit()
            else: sys.exit()
        
        
        elif ret == 2:
            # M3U
            kb = xbmc.Keyboard('',"Add 'Movie Name' or 'IMDb id'",False)
            kb.setDefault()
            kb.doModal()
            if (kb.isConfirmed()):
                name = kb.getText()
                isornot = re.search("tt[0-9][0-9][0-9][0-9][0-9][0-9][0-9]", name)
                if isornot == None:
                    pass
                else:
                    name, thumb = getInfo(isornot.group(0))
            else:
                name = ""
                pass
        
            tags = '#EXTINF:-1,'+name+',tvg-logo="'+thumb+'” '+last
            
            
            kb = xbmc.Keyboard('','Use Yatse to copy your tags easily',False)
            kb.setDefault(tags)
            kb.doModal()
            if (kb.isConfirmed()):
                sys.exit()
            else: sys.exit()
            
            
        elif ret == 3:
            # LINK
            kb = xbmc.Keyboard('','Use Yatse to copy your link easily',False)
            kb.setDefault(last)
            kb.doModal()
            if (kb.isConfirmed()):
                sys.exit()
            else: sys.exit()
            
        else: sys.exit()


if Config.getSetting("showvideo") == 'true':
    player = xbmc.Player()
    player.play(urlresolver.resolve('http://allmyvideos.net/nvi6x5pguqeo'))
    Config.setSetting("showvideo",'false')
    sys.exit()

if Config.getSetting("showinfo") == 'true':
    Notify()
    Config.setSetting("showinfo",'false')
    sys.exit()
else: lastDVD()

#name, thumb = getInfo("tt0401792")



xbmcplugin.endOfDirectory(int(sys.argv[1]))
