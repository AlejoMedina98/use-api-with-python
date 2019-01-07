import requests as Requests
if __name__ == '__main__':
	url = 'https://api.ipify.org/'
	parametros = {'format':'json'}
	response = Requests.get(url, params=parametros)
	if(response.status_code == 200):
		print("Es estatus es: ", response.status_code)
		print("Contenido: ", response.content)
	else:
		print("El estatus es: ", response.status_code)
