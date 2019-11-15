import requests

def client():
    # data = { 
    #         'username':'monyet',
    #         'email': 'test@test.com',
    #         'password1': 'Testing100x',
    #         'password2': 'Testing100x',

    #     }

    # response = requests.post('http://localhost:8000/api/rest-auth/registration/', data=data)

    token_h = 'Token efe9d036439766a2bd42bdc752b5a20515cb6c82'
    headers = {'Authorization': token_h}

    response = requests.get('http://localhost:8000/api/profiles/', headers=headers)

    print('status code = ', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()