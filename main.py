import requests as Requests

if __name__ == '__main__':
	url = 'https://www.google.com.mx'
	response = Requests.get(url)
	if(response.status_code == 200):
		file = open('google.html', 'wb')
		file.write(response.content)
		file.close()