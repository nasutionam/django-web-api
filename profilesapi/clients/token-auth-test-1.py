import requests

def client():
    credentials = { 'username':'nam', 'password': 'nam'}

    response = requests.post('http://localhost:8000/api/rest-auth/login/', data=credentials)

    print('status code = ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()