import requests

def client():
    # credentials = { 'username':'nam', 'password': 'nam'}

    # response = requests.post('http://localhost:8000/api/rest-auth/login/', data=credentials)

    token_h = 'Token ae23d0ef134762ff06948948193b2f72160503e9'
    headers = {'Authorization': token_h}

    response = requests.get('http://localhost:8000/api/profiles/', headers=headers)

    print('status code = ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()