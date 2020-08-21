import requests
import time

headers = {
    'authority': 'ifttt.com',
    'accept': '*/*',
    'x-newrelic-id': 'VwAOU1RRGwAFUFZRDgQB',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://ifttt.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://ifttt.com/applets/JjiX7yBU/edit',
    'accept-language': 'es-ES,es;q=0.9',
    'cookie': '_anon_id=ImRiM2U5MTQ0MTBiNGUxNGI4MjUyNDM0OTJkM2U0ZjU0Ig^%^3D^%^3D--79a0d85d1dc62199fbf00f35339ec99bd9876e84; timezone=Europe/Madrid; __stripe_mid=d89c60bc-1cb8-4965-bcc5-d495446930938568b5; G_ENABLED_IDPS=google; remember_token=f06d6f9ca0a4942854a9b498c9e28c30be9e9f5f; shared_user_id=23206483; browser_session_id=U4QB-N-9DJaHoApu5H8ZQg; expiring_session_token=9eBJBH5tONHc8AOwjb-I7g; __stripe_sid=fe09c1d1-1eba-464d-80f2-0ac65106f0199628bc; _applet_service_session=ZkxTK0JtdnZnNzE2YXl0NDlVeFdpbkE1dXN4WDBlQkRlQjM0UjlvMysxelpHRERIcjVWMnkrR2ZqaHNNM0Q2YmdvQ1pWMTU3NVJPS2doWWorellVTGJTeDEvaDN5TW54MXhOYXdhQW1icWNTZU5wWDRXb3pCb0c1STFwdVBycStzTmN0c05QRWNXMExuUnFEUnhZaWErQU9KVThDdjVLN2NHR3BxQUpwVkFLREx4NUp4cnVFNjN0aEpQbThIS2hUU200TXBRU0J1ejlNcE1FU3NWSmM3RXNRZ1k1a2d0b2l2LzE1VTdoZi9tbUFtVURHSDdLQXppV2NzNGlYem94RlFrL3doZnpCUEJLUWFaMGw1Y2owWjV5S2Q5MlltMkZsNzhiYkFoRENRNnM9LS1HV0lyMHFzMCtPNXdCUnZCRXdLRHd3PT0^%^3D--ee94f16d8a8707b086495c7c8dbd762294607715',
}

data = {
  'authenticity_token': '60TqrX^%^2FmPwfCKNq^%^2BulHjw^%^2BrdaxOcolSdGlKHKbkKNjvDA22RU1wzIlg3I^%^2FO^%^2FP^%^2FiBFSlr2kyJNXOY1sfKTRZJ8w^%^3D^%^3D'
}

#while(True):
time.sleep(1)
response = requests.post('https://ifttt.com/applets/JjiX7yBU/check', headers=headers, data=data)