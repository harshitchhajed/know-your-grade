from bs4 import BeautifulSoup as bs
import requests

# URL of website to scrape
URL = 'https://www.gradescope.ca/'
LOGIN_ROUTE = 'login/'     # login page


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
	'origin': 'https://www.gradescope.ca',
	'referer': 'https://www.gradescope.ca/login'
}

s = requests.Session()

r = s.get(URL)


soup = bs(r.text, 'html.parser')
authenticity = soup.select_one('meta[name="csrf-token"]')['content']


login_payload = {
	'authenticity_token': authenticity,
        'session[email]': '',  # email here
        'session[password]': '',   # password here
        'session[remember_me]': '1',
        'commit': 'Log In',
        'session[remember_me_sso]': '0'
}

cookie = r.cookies

login_req = s.post(URL + LOGIN_ROUTE, headers=HEADERS, cookies=cookie, data=login_payload)

print(login_req.status_code)


# Use Beautiful to parse and scrape your webpage like the example below
soup = bs(s.get(URL + 'courses').text, 'html.parser')
print(soup.prettify())