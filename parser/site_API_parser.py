import requests

def fetch(url, params):
    headers = params['headers']
    body = params['body']
    if params['method']=="GET":
        return requests.get(url, headers=headers)
    if params['method']=="POSt":
        return requests.post(url, headers=headers, data=body)

all = fetch("https://auto.ru/cars/all/", {
  "headers": {
    "accept": "application/json",
    "accept-language": "en,en-US;q=0.9,ru;q=0.8",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-csrf-token": "814f3204948560ef6ebf814f794317c3e8565c3290f90e56",
    "x-requested-with": "fetch",
    "x-susanin-react": "true",
    "cookie": "_csrf_token=814f3204948560ef6ebf814f794317c3e8565c3290f90e56; autoru_sid=a%3Ag621d4a8d2rl2u3haaip81bnjq3s2uvc.60e3007255b03e186fd60af0f1fa4f89%7C1646086797839.604800.sMPyvqdz4HH_0qEdDMr-Ow.Kh4uKRCtiy9VrN1GCaERD9p4jZKVTdSETiEKv1Hapqs; autoruuid=g621d4a8d2rl2u3haaip81bnjq3s2uvc.60e3007255b03e186fd60af0f1fa4f89; autoru_gdpr=1; suid=24a57e77a79166332e095ed49a9d2f44.21c6f964d79917c51ff8c57cf0da2f64; from=direct; X-Vertis-DC=vla; yuidlt=1; yandexuid=3033453941607975162; my=YwA%3D; credit_filter_promo_popup_closed=true; _yasc=pDu9s6wBTExliwLZoou28T0mwPwDTuYzGLTQ2LxqXc/jfsLG; Session_id=noauth:1646086818; yandex_login=; ys=c_chck.3111755801; i=eSInP6CfJ3cS9aDWXbD2jESAhrxdU0SyI2Md9dz0KKw33tmLET/4qydtjsx/5R98Krb72C39kwOw7Da5MqeRUR4oJR4=; mda2_beacon=1646086818632; sso_status=sso.passport.yandex.ru:synchronized; from_lifetime=1646086821634",
    "Referer": "https://auto.ru/cars/ford/all/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": None,  #changed since Python expects None
  "method": "GET"
}); 

print(all.json().keys()) 
cars=all.json()["listing"]["offers"]
for car in cars:
  print(car['lk_summary'])