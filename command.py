from linepy import *
from justgood import imjustgood
import os,traceback,sys,time,threading,livejson,random,re,ast,json,requests
#** Dont change or remove if you are not sure **
#** For Premium Apikey you can contact our team **
#** ID: bit.ly/ang-id /*/ ID: line://ti/p/ryc35PaVQF /*/ ID: line://ti/p/~@ivg8360z **
class justgood(threading.Thread):
    def __init__(self, uid=None, client=None):
        super(justgood, self).__init__()
        self.uid = uid
        self.client = client
        self.db = livejson.File('Data/data.json',True, False, 4)
        self.key = livejson.File('Data/key.json',True, False, 4)
        self.api = livejson.File('Data/api.json',True, False, 4)
        self.maker = self.db['maker']
        self.thumbnail = self.db["thumbnail"]
        self.media = imjustgood(self.api["apikey"])
        self.mid = self.client.getProfile().mid
        self.weAre = self.db["notMast"]
        self.weAr = self.db["justGood"]
        self.join = False
        self.read = {
            "cctv":{}
         }
        self.setting = {
            "convImg": False,
            "convUser":{}
         }

    def notified_invite_into_group(self, op):
        group = op.param1
        if self.uid in op.param3:
            if self.maker:self.client.acceptGroupInvitation(group)
            elif self.join:self.client.acceptGroupInvitation(group)
            else:self.client.acceptGroupInvitation(group);self.client.sendMessage(group,"Permission denied");self.client.leaveGroup(group)
    def notified_read_message(self,op):
        group = op.param1
        member = op.param2
        target = [mem.mid for mem in self.client.getGroup(group).members]
        if group in self.read["cctv"]:
           if member in target:
              if member not in self.read["cctv"][group]:
                  monyet =["Ngetik sini monyet"," Anjing lu"," Saya Ganteng"]
                  text = "• @!  {}".format(random.choice(monyet))            
                  self.sendMention(group,text,[member])
                  self.read["cctv"][group][member] = True

# ** This script use flex fiture, type: Allowliff if you found some command not working **
    def receive_message(self, op):
        try:
           msg = op.message
           text = msg.text
           id = msg.id
           to = msg.to
           of = msg._from
           mykey = self.key["key"]
           if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
               if msg.toType == 0:
                   if of != self.client.getProfile().mid:to = of
                   else:to = msg.to
               elif msg.toType == 1 or msg.toType == 2:
                   to = msg.to
               if msg.contentType == 0:
                   if None == msg.text:
                       return
                   key = mykey.lower()
                   txt = msg.text.lower()
                   thumbnail = self.thumbnail
                   if txt == "help" or txt == key + " help":
                       if key != "": Good = key.title() + " "
                       else:Good = ""
                       just = "• I'm Just Good\n"
                       just += "• Beta Sample\n\n"
                       just += "» Media Command:\n   Social Searching"
                       just += "\n    1. " + Good + "Ymp3: Query"
                       just += "\n    2. " + Good + "Ymp4: Query"
                       just += "\n    3. " + Good + "Youtube: Url"
                       just += "\n    4. " + Good + "Lyric: Query"
                       just += "\n    5. " + Good + "Music: Query"
                       just += "\n    6. " + Good + "Tiktok: UserID"
                       just += "\n    7. " + Good + "Smule: UserID"
                       just += "\n    8. " + Good + "Twitter: UserID"
                       just += "\n    9. " + Good + "Github: UserID"
                       just += "\n    10. " + Good + "Instagram: ID"
                       just += "\n    11. " + Good + "Instapost: URL"
                       just += "\n    12. " + Good + "Smulelink: URL"
                       just += "\n\n   Media Searching"
                       just += "\n    13. " + Good + "Bitlylink: Url"
                       just += "\n    14. " + Good + "Tinyurl: Url"
                       just += "\n    15. " + Good + "Movie: Title"
                       just += "\n    16. " + Good + "Cinema: City"
                       just += "\n    17. " + Good + "Getporn: Title"
                       just += "\n    18. " + Good + "Zodiac: Sign"
                       just += "\n    19. " + Good + "Urban: Query"
                       just += "\n    20. " + Good + "Image: Query"
                       just += "\n    21. " + Good + "Weather: City"
                       just += "\n    22. " + Good + "Playstore: App"
                       just += "\n    23. " + Good + "Televisi Program"
                       just += "\n    24. " + Good + "TV Program: Chnl"
                       just += "\n    25. " + Good + "Time adzan: City"
                       just += "\n    26. " + Good + "Wallpaper: Query"
                       just += "\n    27. " + Good + "Wikipedia: Query"
                       just += "\n    28. " + Good + "Arti nama: Name"
                       just += "\n    29. " + Good + "Arti Mimpi: Name"
                       just += "\n    30. " + Good + "Handphone: Brand"
                       just += "\n    31. " + Good + "Fancytext: Yourtext"
                       just += "\n    32. " + Good + "Birthday: dd-mm-yyyy"
                       just += "\n    33. " + Good + "Myanniv: dd-mm-yyyy"
                       just += "\n\n   Random & Info"
                       just += "\n    34. " + Good + "Convertimage"
                       just += "\n    35. " + Good + "Coronavirus"
                       just += "\n    36. " + Good + "Kamasutra"
                       just += "\n    37. " + Good + "Info Bmkg"
                       just += "\n    38. " + Good + "Topnews"
                       just += "\n    39. " + Good + "Pornstar"
                       just += "\n    40. " + Good + "Quotes"
                       just += "\n    41. " + Good + "Hentai"
                       just += "\n\n   Get & Prank"
                       just += "\n    42. " + Good + "Dick @mention"
                       just += "\n    43. " + Good + "Tits @mention"
                       just += "\n    44. " + Good + "Vagina @mention"
                       just += "\n    45. " + Good + "Meme @tag / % - %"
                       just += "\n\n   Group Utility"
                       just += "\n    46. " + Good + "Tagall"
                       just += "\n    47. " + Good + "Tagnote"
                       just += "\n    48. " + Good + "Sider on"
                       just += "\n    49. " + Good + "Sider off"
                       good_ = "\n\n» Owner Command:"
                       good_ += "\n    50. " + Good + "Upbio: %"
                       good_ += "\n    51. " + Good + "Upname: %"
                       good_ += "\n    52. " + Good + "Unsend: $"
                       good_ += "\n    53. " + Good + "Broadcast: %"
                       good_ += "\n    54. " + Good + "Updatekey: %"
                       good_ += "\n    55. " + Good + "Resetkey"
                       good_ += "\n    56. " + Good + "Allowliff"
                       good_ += "\n    57. " + Good + "Apistatus: Apikey"
                       good_ += "\n    58. " + Good + "Updateapi: Apikey"
                       footer = "\n──────────────\n"
                       footer += "$ = Num || % = Text\n"
                       footer += "https://api.imjustgood.com"
                       public = just + footer
                       master = just + good_ + footer
                       if of in self.maker:self.client.sendReplyMessage(id,to,"{}".format(master))
                       else:self.client.sendReplyMessage(id,to,"{}".format(public))

# ** Social Searching **

                   if txt.startswith("ymp3: ") or txt.startswith(key + " ymp3: "):
                       query = txt.split("ymp3: ")[1]
                       youtube = self.media.youtube(query)
                       data = youtube['result']
                       result = "    「 Youtube Audio」\n\n»Title: {}\n» Author: {}\n» Duration: {}\n» Watched: {}X".format(data['title'],data['author'],data['duration'],data['watched'])
                       self.client.sendImageWithURL(to,data['thumbnail'])
                       self.client.sendReplyMessage(id,to,result)
                       self.client.sendAudioWithURL(to,data['audioUrl'])

                   if txt.startswith("ymp4: ") or txt.startswith(key + " ymp4: "):
                       query = txt.split("ymp4: ")[1]
                       ymp4 = self.media.youtube(query)
                       data = ymp4['result']
                       result = "    「 Youtube Video」\n\n» Title: {}\n» Author: {}\n» Duration: {}\n» Watched: {}X".format(data['title'],data['author'],data['duration'],data['watched'])
                       self.client.sendImageWithURL(to,data['thumbnail'])
                       self.client.sendReplyMessage(id,to,result)
                       self.client.sendVideoWithURL(to,data['videoUrl'])

                   if txt.startswith("youtube: ") or txt.startswith(key + " youtube: "):
                       yturl = msg.text.split(": ")[1]
                       youtube = self.media.youtubedl(yturl)
                       data = youtube['result']
                       result = "    「 Youtube Result 」\n\n{}\n» Author: {}\n» Duration: {}\n» Viewers: {}".format(data["title"],data["author"],data["duration"],data["watched"])
                       self.client.sendImageWithURL(to,data["thumbnail"])
                       self.client.sendReplyMessage(id,to,result)
                       self.client.sendAudioWithURL(to,data["audioUrl"])
                       self.client.sendVideoWithURL(to,data["videoUrl"])

                   if txt.startswith("lyric: ") or txt.startswith(key + " lyric: "):
                       query = txt.split("lyric: ")[1]
                       lyric = self.media.lyric(query)
                       data = lyric['result']
                       result = "    「 Lyric Result 」\n\n» Title: {}\n» Artist: {}\n\n{}".format(data["title"],data["artist"],data["lyric"])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("music: ") or txt.startswith(key + " music: "):
                       query = txt.split("music: ")[1]
                       joox = self.media.joox(query)
                       data = joox['result']
                       result = "    「 Joox Music 」\n\n» Title: {}\n» Artist: {}\n» Duration: {}\n» File Size: {}".format(data['title'],data['singer'],data['duration'],data['size'])
                       self.client.sendImageWithURL(to,data['thumbnail'])
                       self.client.sendReplyMessage(id,to,result)
                       self.client.sendVideoWithURL(to,data['mp3Url'])

                   if txt.startswith("tiktok: ") or txt.startswith(key + " tiktok: "):
                       userid = txt.split("tiktok: ")[1]
                       tiktok = self.media.tiktok(userid)
                       data = tiktok['result']
                       if data["biography"] == "":biography = "None"
                       else:biography = data["biography"]
                       result = "    「 Tiktok Profile 」\n\n» Profile Name: {}\n» Username: {}\n» Profile Bio: {}\n» Followers: {}\n» Following: {}\n» Total Like: {}\n» Profile Url: {}".format(data['fullname'],data['username'],biography,data['followers'],data["following"],data["likes"],data["profileUrl"])        
                       self.client.sendImageWithURL(to,data['pictureUrl'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("smule: ") or txt.startswith(key + " smule: "):
                       userid = txt.split("smule: ")[1]
                       smule = self.media.smule(userid)
                       data = smule['result'];no = 1
                       result = "    「 Smule Profile 」\n\n» User Name: {}\n\n".format(data["username"])        
                       for ang in data["recording"]:
                           result += "   {}. {}\n".format(no,ang["title"])
                           no =(no+1)
                       result += "\n» Total: {}\n───────────────\nFor get recording please type:\nSmulepost: {} / No".format(len(data["recording"]),userid)
                       self.client.sendImageWithURL(to,data['avatar'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("smulepost: ") or txt.startswith(key + " smulepost: "):
                       userid = txt.split("smulepost: ")[1].split(" /")[0]
                       num = txt.split("/ ")[1]
                       postnum = int(num)
                       smule = self.media.smule(userid)
                       data = smule["result"]["recording"]
                       postlist = [ax for ax in data]
                       postdata = postlist[postnum-1]           
                       result = "    「 Smule Result 」\n\n» Title: {}\n» Singer: {}\n» Format: {}\n» Performance by: {}\n» Total likes: {} ♡\n» Listened: {} X\n» Created: {}\n» Caption: {}".format(postdata['title'],postdata['artist'],postdata["type"],postdata['performance'],postdata["loves"],postdata["listens"],postdata["created"],postdata["caption"]) 
                       self.client.sendReplyMessage(id,to,"{}".format(result))
                       if postdata["type"] == "audio":self.client.sendMessage(to,"Downloading audio..");self.client.sendAudioWithURL(to,postdata['mp3Url'])
                       elif postdata["type"] == "video":self.client.sendMessage(to,"Downloading video..");self.client.sendVideoWithURL(to,postdata['mp4Url'])

                   if txt.startswith("twitter: ") or txt.startswith(key + " twitter: "):
                       userid = txt.split("twitter: ")[1]
                       twitter = self.media.twitter(userid)
                       data = twitter['result']
                       if data["biography"] == "":biography = "None"
                       else:biography = data["biography"]
                       result = "    「 Twitter Profile 」\n\n» Profile Name: {}\n» User name: {}\n» Profile Bio: {}\n» Followers: {}\n» Following: {}\n» Total Tweet: {}\n» Cover Url: {}".format(data['fullname'],data['username'],biography,data['follower'],data["following"],data["tweet"],data["banner"])        
                       self.client.sendImageWithURL(to,data['avatar'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("github: ") or txt.startswith(key + " github: "):
                       userid = txt.split("github: ")[1]
                       github = self.media.github(userid)
                       data = github['result']
                       if data["bio"] == None:biography = "None"
                       else:biography = data["bio"]
                       if data["blog"] == None:website = "None"
                       else:website = data["blog"]
                       result = "    「 Github Profile 」\n\n» Profile Name: {}\n» User name: {}\n» Profile Bio: {}\n» Website: {}\n» Followers: {}\n» Following: {}\n» Repositories: {}\n» Page Url: {}".format(data['fullname'],data['username'],biography,website,data['followers'],data["following"],data["repositories"],data["page"])        
                       self.client.sendImageWithURL(to,data['avatar'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("instagram: ") or txt.startswith(key + " instagram: "):
                       userid = txt.split("instagram: ")[1]
                       instagram = self.media.instagram(userid)
                       data = instagram['result']
                       if data["biography"] == "":biography = "None"
                       else:biography = data["biography"]
                       if data["private"] != True:Privasi = "Disabled"
                       else:Privasi = "Enabled" 
                       result = "    「 Instagram Profile 」\n\n» Profile Name: {}\n» Username: {}\n» Profile Bio: {}\n» Followers: {}\n» Following: {}\n» Private: {}\n» Total Post: {}\n» Profile URL: {}".format(data['fullname'],data['username'],biography,data['follower'],data['following'],Privasi,data["post"],data["profile"])            
                       if data["lastpost"] !=[]:
                          no =1;result +="\n» Lastpost:\n"
                          for bacot in data["lastpost"]:
                              result +="\n  {}. Page: {} » {}".format(no,bacot["page"],bacot["created"])
                              no = (no+1)
                       self.client.sendImageWithURL(to,data['picture'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("instapost: ") or txt.startswith(key + " instapost: "):
                       posturl = text.split(": ")[1]
                       instapost = self.media.instapost(posturl)
                       data = instapost['result']
                       if data["caption"] == "":caption = "None"
                       else:caption = data["caption"]
                       result = "    「 Instagram Post  」\n\n» Profile Name: {}\n» Username: {}\n» Caption: {}\n» Created: {}".format(data['fullname'],data['username'],caption,data['created'])            
                       self.client.sendImageWithURL(to,data['picture'])
                       self.client.sendReplyMessage(id,to,result)
                       if data["slidePost"] == False:
                          if data["postData"][0]["type"] == "image":self.client.sendMessage(to,"Download image..");self.client.sendImageWithURL(to,data['postData'][0]["postUrl"])
                          elif data["postData"][0]["type"] == "video":self.client.sendMessage(to,"Download video..");self.client.sendVideoWithURL(to,data['postData'][0]["postUrl"])
                       else:
                          for ang in data["postData"]:
                              if ang["type"] == "image":
                                  self.client.sendImageWithURL(to,ang["postUrl"])
                              elif ang["type"] == "video":
                                  self.client.sendVideoWithURL(to,ang["postUrl"])

                   if txt.startswith("smulelink: ") or txt.startswith(key + " smulelink: "):
                       url = msg.text.split(": ")[1]
                       smule = self.media.smuledl(url)
                       data = smule["result"]
                       result = "    「 Smule Download 」\n\n» Title: {}\n» Caption: {}".format(data['title'],data['caption'])
                       if "thumbnail" in data:
                           self.client.sendImageWithURL(to,data['thumbnail'])
                       else:pass
                       self.client.sendReplyMessage(id,to,"{}".format(result))
                       self.client.sendAudioWithURL(to,data['mp3Url'])
                       if data["type"] == "video":self.client.sendMessage(to,"Downloading video..");self.client.sendVideoWithURL(to,data['mp4Url'])
                       else:pass

# ** Media Searching **

                   if txt.startswith("bitlylink: ") or txt.startswith(key + " bitlylink: "):
                       url = text.split(": ")[1]
                       bitly = self.media.bitly(url)
                       data = bitly['result']
                       result = "Converted to:\n{}".format(data)
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("tinyurl: ") or txt.startswith(key + " tinyurl: "):
                       url = text.split(": ")[1]
                       tiny = self.media.tinyurl(url)
                       result = "Converted to:\n{}".format(tiny["result"])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("movie: ") or txt.startswith(key + " movie: "):
                       title = txt.split("movie: ")[1]
                       movie = self.media.movie(title)
                       data = movie['result']
                       result = "    「 Movie Review 」\n\n» Title: {}\n» Actors: {}\n» Director: {}\n» Genre: {}\n» Producer: {}\n» Release: {}\n» Duration: {}\n» Awards: {}\n» Synopsis: {}".format(data['title'],data['actors'],data['director'],data['genre'],data["production"],data["release"],data["runtime"],data["awards"],data["synopsis"])            
                       self.client.sendImageWithURL(to,data['poster'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("cinema: ") or txt.startswith(key + " cinema: "):
                       city = txt.split("cinema: ")[1]
                       cinema = self.media.cinema(city)
                       data = cinema['result']
                       mmk = [];no = 1;result = "    「 CINEMA SHOWPLACE」\n\n» CITY: {}".format(data['city'].upper())            
                       for agx in data["data"]:
                          if "nowPlaying" in agx:
                              mmk.append("True")
                              result += "\n\n{}.STUDIO( {} )\n» Address: {}\n\n» Now Playing: ".format(no,agx["cinema"],agx["address"])
                              no = (no+1);num = 1
                              for nn in agx["nowPlaying"]:
                                    result += "\n\n {}. {}".format(num,nn["movie"])
                                    num = (num+1)
                              self.client.sendReplyMessage(id,to,result)                  
                              self.client.sendMessage(to,"For detail cinema playing type:\nCinema detail: {} / No Studio : No Playing\n\n*Example*\nCinema detail: {} / 1 - 1".format(city,city))
                       if mmk == []:
                          for agx in data["data"]:
                              result += "\n\n{}.{}\n» Address: {}".format(no,agx["cinema"],agx["address"])
                              no = (no+1)
                          result +="\n\n» Now Playing: PSBB BANGSAT\nIKUTI PROTOKOL KESEHATAN"
                          self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("cinema detail: ") or txt.startswith(key + " cinema detail: "):
                       city = txt.split("detail: ")[1].split(" /")[0]
                       studio = txt.split("/ ")[1].split(" -")[0]
                       playing = txt.split("- ")[1]
                       cinema = self.media.cinema(city)
                       data = cinema["result"]["data"]
                       tstudio = [ax for ax in data]
                       studionum = tstudio[int(studio)-1]       
                       tplaying = [ab for ab in studionum["nowPlaying"]]
                       player = tplaying[int(playing)-1];time = ""
                       for piye in player["showtime"]:
                           time += "\n  {} WIB".format(piye)                          
                       result = "{}. \n\n» Ticket: {}\n» Showtime: {}\n\n» Genre: {}\n\n» Duration: {}\n\n» Director: {}\n\n» Actors: {}\n\n» Synopsis: {}".format(player["movie"],player['price'],time,player['genre'],player["duration"],player["director"],player["actor"],player['synopsis'])
                       self.client.sendImageWithURL(to,player['poster'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("getporn: ") or txt.startswith(key + " getporn: "):
                       query = txt.split("getporn: ")[1]
                       porn = self.media.porn(query)
                       data = porn['result']
                       result = "    「 Porn Video 」\n\n{}\n  » Duration: {}\n  » Quality: {}\n  » Viewers: {}".format(data["title"],data["duration"],data["quality"],data["watched"])
                       self.client.sendImageWithURL(to,data["thumbnail"])
                       self.client.sendReplyMessage(id,to,result)
                       self.client.sendVideoWithURL(to,data["videoUrl"])

                   if txt.startswith("zodiac: ") or txt.startswith(key + " zodiac: "):
                       sign = txt.split("zodiac: ")[1]
                       zodiac = self.media.zodiac(sign)
                       data = zodiac['result']
                       result = "    「 Daily Zodiac 」\n\n» Zodiac: {}\n» Date: {}\n» Zodiac Match: {}\n\n» General: {}\n\n» Money: {}\n\n» Single Relation: {}\n\n» Couple Relation: {}\n\n» Hokki\n  - Number: {}\n  - Colour: {}\n  - Time: {}".format(sign,data['date'],data["couple"],data['public'],data["money"],data["love"]["single"],data["love"]["couple"],data['number'],data['color'],data["time"])            
                       self.client.sendImageWithURL(to,data['image'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("urban: ") or txt.startswith(key + " urban: "):
                       query = txt.split("urban: ")[1]
                       urban = self.media.urban(query)
                       data = urban['result']
                       result = "    「 Urban Dictionary」\n\n» Word: {}\n» Definition:\n{}\n» Example:\n{}".format(query.title(),data['definition'],data['example'])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("image: ") or txt.startswith(key + " image: "):
                       query = txt.split("image: ")[1]
                       image = self.media.image(query)
                       data = image['result']
                       jagir = random.choice(data)
                       self.sendFleximg(to,jagir)

                   if txt.startswith("weather: ") or txt.startswith(key + " weather: "):
                       city = txt.split("weather: ")[1]
                       weather = self.media.cuaca(city)
                       data = weather['result']
                       result = "    「 Weather 」\n\n▪︎City: {}\n\n» Condition🏝: {}\n» Humidity❄: {}\n» Mph Wind🌪: {}\n» Temperature🌡: {}".format(data["location"],data["description"],data["humidity"],data["wind"],data["temperature"])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("playstore: ") or txt.startswith(key + " playstore: "):
                       app = txt.split("playstore: ")[1]
                       playstore = self.media.playstore(app)
                       data = playstore['result']
                       no = 1;result = "    「 Playstore 」"
                       for ax in data:
                           result += "\n\n{}. {}\n    » Developer: {}\n    » Description: {}\n    » Download URL: {}".format(no,ax["title"],ax["developer"],ax["description"],ax["pageUrl"])
                           no = (no+1)
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "televisi program" or txt == key + " televisi program":
                       program = self.media.acaratv()
                       data = program['result']
                       channel = "    「 TV PROGRAM 」\n"
                       for anx in data:
                           for ngx in anx:
                               channel += "\n\n»» {}:\n".format(ngx)
                               for nenen in anx[ngx]:
                                   channel +="\n  {}".format(nenen)
                       self.client.sendReplyMessage(id,to,channel)

                   if txt.startswith("tv program: ") or txt.startswith(key + "tv program: "):
                       tvid = txt.split("tv program: ")[1]
                       channel = self.media.acaratv_channel(tvid)
                       data = channel['result']
                       result = "    「 {} PROGRAM 」\n".format(tvid.upper())
                       for gx in data:
                           result += "\n{}".format(gx)
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("time adzan: ") or txt.startswith(key + " time adzan: "):
                       city = txt.split("adzan: ")[1]
                       adzan = self.media.adzan(city)
                       data = adzan['result']["adzan"]
                       result = "    「 Time Adzan 」\n\n▪︎City: {}\n\n» Imsa': {}\n» Subuh: {}\n» Dhuhur: {}\n» Ashar: {}\n» Maghrib: {}\n» Isya: {}".format(city.title(),data["terbit"],data["subuh"],data["dzuhur"],data["ashar"],data["maghrib"],data["isya"])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("wallpaper: ") or txt.startswith(key + " wallpaper: "):
                       query = txt.split("wallpaper: ")[1]
                       wallpaper = self.media.wallpaper(query)
                       data = wallpaper['result']
                       setro = random.choice(data)
                       self.client.sendImageWithURL(to,setro)

                   if txt.startswith("wikipedia: ") or txt.startswith(key + " wikipedia: "):
                       query = txt.split("wikipedia: ")[1]
                       wikipedia = self.media.wikipedia(query)
                       data = wikipedia['result']               
                       result = "    「 Wikipedia 」\n\n» Wikipedia: {}\n» Result:\n{}".format(query.title(),data)
                       self.client.sendImageWithURL(to,thumbnail[0])
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("arti nama: ") or txt.startswith(key + " arti nama: "):
                       hoax = txt.split("nama: ")[1]
                       artinama = self.media.nama(hoax)
                       data = artinama['result']
                       result = "    「 Arti Nama '{}' 」\n\n» Karakter: {}\n» Keseluruhan: {}".format(hoax.title(),data["definition"],data["description"])	
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("arti mimpi: ") or txt.startswith(key + " arti mimpi: "):
                       tahayul = txt.split("mimpi: ")[1]
                       mimpi = self.media.mimpi(tahayul)
                       data = mimpi['result']
                       no=1;result = "    「 Arti Mimpi」"
                       for dream in data:
                           result += "\n\n{}.{}\n» Arti: {}".format(no,dream["dream"],dream["meaning"])
                           no = (no+1)
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("handphone: ") or txt.startswith(key + " handphone: "):
                       query = txt.split("handphone: ")[1]
                       phone = self.media.cellular(query)
                       data = phone['result']
                       no = 1 ; result = "    「 Phone Specification 」"
                       for mbul in data:
                           result +="\n\n{}. {}\n  » Battery: {}\n  » RAM: {}\n  » Display: {}\n  » Storage: {}\n  » Release: {}\n  » Screen: {}\n  » Chipset: {}\n  » More detail: {}".format(no,mbul["brands"],mbul["battery"],mbul["ram"],mbul["display"],mbul["storage"],mbul["release"],mbul["screen"],mbul["chipset"],mbul["pageUrl"])
                           no = (no+1)
                       self.client.sendReplyMessage(id,to,result)

                   if txt.startswith("birthday: ") or txt.startswith(key + " birthday: "):
                       date = txt.split("birthday: ")[1]
                       try:
                          birth = self.media.lahir(date)
                          data = birth['result']
                          result = "    「 Info Birthday 」\n\nTanggal Lahir: {}\n\n» Hari Pasaran: {}\n» Ulang Tahun: {} lagi\n» Usia: {}\n» Zodiak: {}".format(data["lahir"],data["hari"],data["ultah"],data["usia"],data["zodiak"])
                          self.client.sendReplyMessage(id,to,result)
                       except:self.client.sendReplyMessage(id,to,"「 Format Salah 」\nContoh: \nBirthday: 07-02-2020")

                   if txt.startswith("myanniv: ") or txt.startswith(key + " myanniv: "):
                       date = txt.split("myanniv: ")[1]
                       try:
                         anniv = self.media.jadian(date)
                         data = anniv['result']
                         result = "    「 Info Anniversary」\n\n» Tanggal Jadian: {}\n» Komitmen: {}\n» Karakteristik: {}".format(data["date"],data["description"],data["related"])
                         self.client.sendReplyMessage(id,to,result)
                       except:self.client.sendReplyMessage(id,to,"「 Format Salah 」\nContoh: \nMyanniv: 17-07-2019")

# ** Random & Info **

                   if txt== "coronavirus" or txt == key + " coronavirus":
                       corona = self.media.corona()
                       data = corona['result']
                       result = "    「 CORONA INFO 」\n\nDate: {}\n  • Indonesia:\n    » Positif: {}\n    » Recovered: {}\n    » Dead: {}\n\n  • Worldwide:\n    » Positif: {}\n    » Recovered: {}\n    » Dead: {}".format(data["date"],data["indonesia"]["case"],data["indonesia"]["fit"],data["indonesia"]["rip"],data["world"]["case"],data["world"]["fit"],data["world"]["rip"])
                       self.sendFleximg(to,thumbnail[1])
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "kamasutra" or txt == key + " kamasutra":
                       kama = self.media.kamasutra()
                       data = kama['result']
                       result = "    「 Kamasutra 」\n\n» Style: {}\n» Definition: {}".format(data["style"],data["description"])
                       self.sendFleximg(to,data["thumbnail"])
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "info bmkg" or txt == key + " info bmkg":
                       bmkg = self.media.bmkg()
                       data = bmkg['result']
                       result = "    「 BMKG NEWS 」\n\n» Location: {}\n» Area: {}\n» Date: {}\n» Time: {}\n» Magnitudo: {}\n» Cordinate: {}\n» Earthquake: {}\n» Warning: {}n» Instruction: {}".format(data["lokasi"],data["wilayah"],data["tanggal"],data["pukul"],data["kekuatan"],data["kedalaman"],data["saran"],data["arahan"])
                       self.sendFleximg(to,data["skema"])
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "topnews" or txt == key + " topnews":
                       news = self.media.topnews()
                       data = news['result']
                       no = 1;result = "    「 Top News 」"
                       for top in data:                           
                           result += "\n\n{}. {}\n\n  » Author:{}\n  » Source: {}\n  » Page: {}".format(no,top["title"],top["author"],top["source"],top["url"])
                           no = (no+1)
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "pornstar" or txt == key + " pornstar":
                       porn = self.media.pornstar()
                       data = random.choice(porn['result'])
                       result = "    「 Pornstar 」\n\n{}\n\n» Birth: {}\n» Breast: {}\n» Country: {}\n» Height: {}\n» Tits: {}".format(data["pornstar"].upper(),data["birth"],data["breast"],data["country"],data["height"],data["tits"])
                       self.sendFleximg(to,data["image"])
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "quotes" or txt == key + " quotes":
                       quote = self.media.movie_quotes()
                       data = quote['result']
                       result = "    「 Quotes 」\n\n`` {} ``".format(data)
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "hentai" or txt == key + " hentai":
                       hentai = self.media.hentai()
                       data = random.choice(hentai['result'])
                       self.sendFleximg(to,data)

                   if txt== "job hiring" or txt == key + " job hiring":
                       job = self.media.karir()
                       data = job['result']
                       no = 1;result = "    「 JOB HIRING 」\n"
                       for dasi in data:                           
                           result += "\n{}. {}\n\n  » Job Descript:{}\n  » Salary: {}\n  » Position: {}\n  » Location: {}\n  » Education: {}\n  » Experience: {}\n  » Company: {}\n  » Section: {}\n  » Requirements: {}\n  » More detail: {}\n────────────────\n".format(no,dasi["bagian"].upper(),dasi["deskripsi"],dasi["gaji"],dasi["jabatan"],dasi["lokasi"],dasi["pendidikan"],dasi["pengalaman"],dasi["perusahaan"],dasi["profesi"],dasi["syarat"],dasi["sumber"])
                           no = (no+1)
                       self.client.sendReplyMessage(id,to,result)

                   if txt== "bye" or txt == key + " bye":
                       self.sendMention(to,"Jancuk lu @! ",[of])
                       self.client.leaveGroup(to)


                   if txt== "convertimage" or txt == key + " convertimage":
                       self.setting["convUser"] = of
                       self.setting["convImg"] = True
                       self.client.sendReplyMessage(id,to,"send an image")

                   if txt.startswith("fancytext: ") or txt.startswith(key + " fancytext: "):
                       text = txt.split("fancytext: ")[1]
                       host = "https://api.imjustgood.com/fancy?text={}".format(text)                   
                       data = json.loads(requests.get(host).text)
                       result = "「   Fancy Text   」"
                       for x in data["result"]:
                           result +="\n{}".format(x)
                       self.client.sendReplyMessage(id,to,"{}".format(result))

#  *GET & PRANK COMMAND*

                   if txt.startswith("dick ") or txt.startswith(key + " dick "):
                      if 'MENTION' in msg.contentMetadata.keys() != None:
                         names = re.findall(r'@(\w+)', txt)
                         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                         mentionees = mention['MENTIONEES']
                         dick = self.media.dick()
                         data = dick['result']
                         result = "    「 Dick Info 」\n"
                         for mention in mentionees:
                             if mention["M"] != self.mid:
                                 result += "\n▪︎ {}\n  » User: @! it, \n  » Size: {}\n  » Ability: {}\n  » Flexibelity: {}\n  » Description: {}".format(data["dick"].upper(),data["size"],data["ability"],data["flexibility"],data["description"])
                                 self.sendFleximg(to,data["picture"])               
                                 self.client.sendReplyMention(id,to,result,"",[mention["M"]])

                   if txt.startswith("tits ") or txt.startswith(key + " tits "):
                      if 'MENTION' in msg.contentMetadata.keys() != None:
                         names = re.findall(r'@(\w+)', txt)
                         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                         mentionees = mention['MENTIONEES']
                         nenen = self.media.tits()
                         data = nenen['result']
                         result = "    「 Nenen info 」\n"
                         for mention in mentionees:
                             if mention["M"] != self.mid:
                                 result += "\n▪︎ {}\n  » User: @! it, \n  » Size: {}\n  » Cup: {}\n  » Aerola: {}\n  » Nipple: {}\n  » Description: {}".format(data["tits"].upper(),data["size"],data["cup"],data["aerola"],data["nipple"],data["description"])
                                 self.sendFleximg(to,data["picture"])               
                                 self.client.sendReplyMention(id,to,result,"",[mention["M"]])

                   if txt.startswith("vagina ") or txt.startswith(key + " vagina "):
                      if 'MENTION' in msg.contentMetadata.keys() != None:
                         names = re.findall(r'@(\w+)', txt)
                         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                         mentionees = mention['MENTIONEES']
                         memek = self.media.vagina()
                         data = memek['result']
                         result = "    「 Vagina info 」\n"
                         for mention in mentionees:
                             if mention["M"] != self.mid:
                                 result += "\n▪︎ {}\n  » User: @! it, \n  » Kedalaman: {}\n  » Kelembaban: {}\n  » Elastistik: {}\n  » Cengkraman: {}\n  » Description: {}".format(data["vagina"].upper(),data["depth"],data["humidity"],data["elasticity"],data["grip"],data["description"])
                                 self.sendFleximg(to,data["picture"])               
                                 self.client.sendReplyMention(id,to,result,"",[mention["M"]])

                   if txt.startswith("meme: ") or txt.startswith(key + " meme: "):
                       text = txt.split("/ ")[1].split(" - ")[0]
                       text2 = txt.split("- ")[1]
                       if 'MENTION' in msg.contentMetadata.keys() != None:
                         names = re.findall(r'@(\w+)', txt)
                         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                         mentionees = mention['MENTIONEES']
                         for mention in mentionees:
                             if mention["M"] != self.mid:
                                 imageurl = "https://obs.line-scdn.net/" + self.client.getContact(mention['M']).pictureStatus
                                 meme = self.media.meme(text,text2,imageurl)
                                 data = meme['result']
                                 self.client.sendImageWithURL(to,data)               

#  *UTILITY*
                   if txt== "tagall" or txt == key + " tagall":
                      group = self.client.getGroup(to)
                      yosh = [contact.mid for contact in group.members]
                      suka = len(yosh)//20
                      for tante in range(suka+1):
                            ret_ = "• I'M JUSTGOOD\n• PUBLIC SAMPLE\n"
                            rendy = [];ewe = 1
                            for juara in group.members[tante*20 : (tante+1)*20]:
                                rendy.append(juara.mid)
                                ret_ += "\n{}. @!\n".format(ewe)
                                ewe = (ewe+1)
                            ret_ += "\n\n• Total {} Users.\n──────────────\n•Version: BETA 0.0.1\n• Imjustgood.com".format(len(rendy))
                            self.sendMention(to, ret_, rendy)

                   if txt== "tagnote" or txt == key + " tagnote":
                       self.tagnote(to)

                   if txt.startswith("sider ") or txt.startswith(key + " sider "):
                       aho = txt.split("sider ")[1]
                       if aho == "on":
                          if to in self.read["cctv"]:self.read["cctv"][to]={};self.client.sendReplyMessage(id,to,"Check sider restarting..")
                          else:self.read["cctv"][to]= {};self.client.sendReplyMessage(id,to,"Sider active.")
                       elif aho == "off":
                           if to not in self.read["cctv"]:self.client.sendReplyMessage(id,to,"Sider already nonactive.")
                           else:del self.read["cctv"][to];self.client.sendReplyMessage(id,to,"Sider nonactive.")

                   if txt.startswith("autojoin ") or txt.startswith(key + " autojoin "):
                    if of in self.maker:
                       aho = txt.split("autojoin ")[1]
                       if aho == "on":
                          if self.join:self.client.sendReplyMessage(id,to,"Already on.")
                          else:self.join= True;self.client.sendReplyMessage(id,to,"Auto join on.")
                       elif aho == "off":
                           if self.join == False:
                              self.client.sendReplyMessage(id,to,"Already off.")
                           else:
                              self.join =False
                              self.client.sendReplyMessage(id,to,"aujoin off.")

#  *Owner Command*

                   if txt.startswith("unsend: ") or txt.startswith(key + " unsend: "):
                    if of in self.maker:
                       Msgid = txt.split("unsend: ")[1]
                       Mess = self.client.getRecentMessagesV2(to,999)                     
                       Mes = []
                       for x in Mess:
                           if x._from == self.mid:    
                               Mes.append(x.id)                            
                               if len(Mes) == int(Msgid):break                       
                       for b in Mes:
                           try:self.client.unsendMessage(b)
                           except:pass

                   if txt.startswith("broadcast: ") or txt.startswith(key + " broadcast: "):
                    if of in self.maker:
                       bc = txt.split("broadcast: ")[1]
                       groups = self.client.getGroupIdsJoined()
                       allGc = self.client.getGroups(groups)
                       aho = self.client.crawl(self.weAr)
                       youBc = "「   Broadcast Message   」\nSender: @! \nSupport: https://{}\nBroadcasted: {} Groups\n────────────────\n{}".format(aho,len(allGc),bc)
                       for x in range(len(allGc)):
                           self.sendMention(allGc[x].id, youBc,[of])                           
                       self.client.sendReplyMessage(id,to,"Success Broadcasted on {} groups.".format(len(allGc)))

                   if txt.startswith("upbio: ") or txt.startswith(key + " upbio: "):
                    if of in self.maker:
                       bio = txt.split("upbio: ")[1]
                       if len(bio) <= 500:
                           agx = self.client.getProfile()
                           agx.statusMessage = bio
                           self.client.updateProfile(agx)
                           self.client.sendMessage(to,"Bio updated:\n{}".format(bio))
                       else:self.client.sendMessage(to,"Text is Limit")

                   if txt.startswith("upname: ") or txt.startswith(key + " upname: "):
                    if of in self.maker:
                       upnm = txt.split("upname: ")[1]
                       if len(upnm) <= 20:
                            name = self.client.getProfile()
                            name.displayName = upnm.title()
                            self.client.updateProfile(name)
                            self.client.sendMessage(to,"Bio updated:\n{}".format(upnm.title()))
                       else:self.client.sendMessage(to,"Text is Limit")

                   if txt.startswith("updatekey: ") or txt.startswith(key + " updatekey: "):
                    if of in self.maker:
                       upkey = txt.split("updatekey: ")[1]
                       self.key["key"] = upkey;self.client.sendMessage(to,"Key updated:\n{}".format(upkey))

                   if txt== "resetkey" or txt == key + " resetkey":
                    if of in self.maker:
                      self.key["key"]  = "";self.client.sendMessage(to,"Key reseted")

                   if txt.startswith("updateapi: ") or txt.startswith(key + " updateapi: "):
                    if of in self.maker:
                       apikey = text.split(": ")[1]
                       self.api["apikey"] = apikey;self.client.sendMessage(to,"Apikey upgraded.")

                   if txt== "allowliff" or txt == key + " allowliff":
                    if of in self.maker:
                      try:self.allow();self.client.sendReplyMessage(id,to,"Flex mode enabled")
                      except Exception as e:print(e)

                   if txt.startswith("apistatus: ") or txt.startswith(key + " apistatus: "):
                    if of in self.maker:
                       idapi = text.split(": ")[1]
                       url = "https://api.imjustgood.com/status?apikey={}".format(idapi)
                       apikey = json.loads(requests.get(url).text)
                       data = apikey['result']
                       result = "    「 Apikey Status 」\n\nYour ID: {}\n  » Type: {}\n  » Usage: {}\n  » Restarted: {}\n  » Expired: {}".format(data["id"],data["type"],data["usage"],data["restart"],data["expired"])
                       self.client.sendReplyMessage(id,to,result)

               if msg.contentType == 1:
                   if self.setting["convImg"] == True and of in self.setting["convUser"]:    
                       try:
                          image = self.client.downloadObjectMsg(msg.id)                          
                          imgid = open(image,'rb')
                          host = "https://api.imjustgood.com/imgurl"
                          headers = {"apikey": "imjustgood"}
                          data = {"file": imgid }
                          main = json.loads(requests.get(host, headers=headers, files=data).text)
                          self.client.sendReplyMessage(id,to,"Your URL:\n{}".format(main["result"]))
                          try:self.client.deleteFile(image)
                          except:pass
                          self.setting["convUser"] = {};self.setting["convImg"] = False
                       except Exception as e:print(e)
        except Exception as e:
           print("Goperation error: {}".format(e))

    def sendMention(self,to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@Justgood "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            for mid in mids:
                textx += str(texts[mids.index(mid)])
                slen = len(textx)
                elen = len(textx) + 15
                arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ""
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        self.client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0) 

    def sendFleximg(self, to,image):
       xGx = {"type":"image","originalContentUrl":"{}".format(image),"previewImageUrl":"{}".format(image),"animated":True,"extension":"jpg","sentBy":{"label": "Im Just Good","iconUrl":"{}".format(self.weAre),"linkUrl":"https://{}".format(self.client.crawl(self.weAr))}}
       self.client.sendFlex(to, xGx)

    def allow(self):
       url = 'https://access.line.me/dialog/api/permissions'
       data = {'on': ['P','CM'],'off': []}
       headers = {'X-Line-Access': self.client.authToken,'X-Line-Application': self.client.server.APP_NAME,'X-Line-ChannelId': '1602876096','Content-Type': 'application/json'}
       requests.post(url, json=data, headers=headers)

    def tagnote(self,to):
        h = [];s = []
        ang = self.client.getProfile()
        group = self.client.getGroup(to);nama = [contact.mid+'||//{}'.format(contact.displayName) for contact in group.members];nama.remove(ang.mid+'||//{}'.format(ang.displayName))
        data = nama
        k = len(data)//500
        for aa in range(k+1):
            nos = 0
            if aa == 0:dd = '• IMJUSTGOOD\n• TAGNOTE\n';no=aa
            else:dd = '• IMJUSTGOOD\n• TAGNOTE\n';no=aa*500
            msgas = dd
            for i in data[aa*500 : (aa+1)*500]:
                no+=1
                if no == len(data):msgas+='\n  {}. @'.format(no)
                else:msgas+='\n  {}. @'.format(no)
            msgas = msgas
            for i in data[aa*500 : (aa+1)*500]:
                gg = [];dd = ''
                for ss in msgas:
                    if ss == '@':
                        dd += str(ss)
                        gg.append(dd.index('@'))
                        dd = dd.replace('@',' ')
                    else:
                        dd += str(ss)
                s.append({'type': "RECALL", 'start': gg[nos], 'end': gg[nos]+1, 'mid': str(i.split('||//')[0])})
                nos +=1
            cons= '{}\n• Total: {} Members\n• Group: {}'.format(msgas,no,self.client.getGroup(to).name)
            self.createPostGroup(cons,to,holdingTime=None,textMeta=s)


    def createPostGroup(self, text,to, holdingTime=None,textMeta=[]):
        params = {'homeId': to, 'sourceType': 'GROUPHOME'}
        url = self.client.server.urlEncode(self.client.server.LINE_TIMELINE_API, '/v39/post/create.json', params)
        payload = {'postInfo': {'readPermission': {'type': 'ALL'}}, 'sourceType': 'GROUPHOME', 'contents': {'text': text,'textMeta':textMeta}}
        if holdingTime != None:
            payload["postInfo"]["holdingTime"] = holdingTime
        data = json.dumps(payload)
        r = self.client.server.postContent(url, data=data, headers=self.client.server.timelineHeaders)
        return r.json()
