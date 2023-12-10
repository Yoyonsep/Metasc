import requests,json,re
ses=requests.Session()
id = []

def login():
	cookie = input(" Masukan Cookie : ")
	url = ses.get("https://www.facebook.com/adsmanager/manage/campaigns",cookies={"cookie":cookie}).text
	regex = re.search("act=(.*?)&nav_source",str(url)).group(1)
	get = ses.get(f"https://www.facebook.com/adsmanager/manage/campaigns?act={regex}&nav_source=no_referrer",cookies={"cookie":cookie}).text
	token = re.search('accessToken="(.*?)"',str(get)).group(1)
	print(f" Token : {token}")
	print("")
	idt = input(" Masukan ID : ")
	dump(idt,"",{"cookie":cookie},token)
	
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			print(i["id"]+"<=>"+i["name"])
			id.append(i["id"]+"<=>"+i["name"])
			#print(f" sedang mengumpulkan {len(id)} id....", end="\r")
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
	
login()