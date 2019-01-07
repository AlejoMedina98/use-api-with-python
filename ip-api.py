import requests as Req

if __name__ == '__main__':
	url = 'http://ip-api.com/json'
	response = Req.get(url)
	print(response.status_code)
	print(response.content)