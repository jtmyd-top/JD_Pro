import requests
def get_ql_token(base_url, client_id, client_secret):
    response = requests.get(f"{base_url}/open/auth/token?client_id={client_id}&client_secret={client_secret}")
    token_data = response.json()
    if token_data['code'] == 200:
        return token_data['data']['token']
    else:
        raise Exception(f"Failed to get token: {token_data['message']}")