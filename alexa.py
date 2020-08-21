import os
import webbrowser
import time
import requests
import dropbox

headers = {
    'authority': 'ifttt.com',
    'accept': '*/*',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://ifttt.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://ifttt.com/applets/JjiX7yBU/edit',
    'accept-language': 'es-ES,es;q=0.9',
    'cookie': '_anon_id=ImRiM2U5MTQ0MTBiNGUxNGI4MjUyNDM0OTJkM2U0ZjU0Ig%3D%3D--79a0d85d1dc62199fbf00f35339ec99bd9876e84; timezone=Europe/Madrid; __stripe_mid=d89c60bc-1cb8-4965-bcc5-d495446930938568b5; G_ENABLED_IDPS=google; remember_token=f06d6f9ca0a4942854a9b498c9e28c30be9e9f5f; shared_user_id=23206483; browser_session_id=U4QB-N-9DJaHoApu5H8ZQg; __stripe_sid=fe09c1d1-1eba-464d-80f2-0ac65106f0199628bc; expiring_session_token=KNvlDM11DTWABxfD3wDnQA; _applet_service_session=WWRRay9DRnlpOHp6cHlNM3o5TDF6cE9TQVcrNUUvOWpRVytFSy9xMDh4V1V3Tk5PMDJ0eXpXUXBDL0F0Q3VHMnFxTGFBRTZEQUNJTWZlNTlYL3pqSUZaaENoekpHRHBhT04yYkZta0NSSkhYRTNzdFk2dDZYQjFtczRVOVZwQkRsNm4xUjN0cUFmVlJldjRzcGRGdmRmOGR4U2JPaHJQczc5bVdFQWFtNHVrbEwzcFRydVQ0c0pobDAzaVBGZ0ZRTjJGc2xQV3Y1T2ZwNlhjVkRlcVpkU2ZaejYwbFB2UjZncVM1YU1RNFY3aFJxYXg0SVVNRVVReStmd2tJQTJZbjEyVWtJcVF4SERFZk41NnBrL1g0NjR2V0QvUStxeXJvenNnMzFnSFdpT009LS1uOXgwbDk1ckMvZzd2STc5MkpjUmRRPT0%3D--a307725167bfbe6e6042f8b6577e19ed47f406ba',
}

data = {
  'authenticity_token': '60TqrX/mPwfCKNq+ulHjw+rdaxOcolSdGlKHKbkKNjvDA22RU1wzIlg3I/O/P/iBFSlr2kyJNXOY1sfKTRZJ8w=='
}

browser_path = "C:/Users/black/AppData/Local/Programs/Opera GX/launcher.exe %s"
path = "C:/Users/black/Dropbox/Amazon Alexa"
accessToken = 'sl.AgOGDMe1Va54wk37OzuQCndtndRjUtzeiRSzckFAJZ_LMMfse0TsZB8ZcsLHK_-2faqjdAW-Unrie2qNwdEhaZq7-JLaSQkk9Qt0tcvPoIuM-Tdssz6CU8JwzuC1WNaPFzYSZec'
folder = "/Amazon Alexa"

while(True):
    dbx = dropbox.Dropbox(accessToken)
    response = dbx.files_list_folder(path=folder)
    nfiles = len(response.entries)

    time.sleep(1)
    r = requests.post('https://ifttt.com/applets/JjiX7yBU/check', headers=headers, data=data)

    if(nfiles != 0):
        time.sleep(1)
        
        path = folder+"/"+response.entries[0].name
        md,res = dbx.files_download(path)

        strings = res.content.decode().split(" ",1)

        dbx.files_delete_v2(path)

        if(strings[0] == "bloquear"):
            os.system("rundll32.exe user32.dll, LockWorkStation")

        elif(strings[0] == "apagar"):
            os.system("shutdown /s")

        elif(strings[0] == "reiniciar"):
            os.system("shutdown /r")

        else:
            webbrowser.open("http://"+strings[0]+".com")
