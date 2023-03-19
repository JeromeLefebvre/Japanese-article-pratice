import requests

# Replace YOUR_API_TOKEN with your Wanikani API token
headers = {'Authorization': 'Bearer 890578c5-c281-42d1-91b2-b1bac3c8fcb2'}

# Search for the "木" kanji
search_params = {'types': 'kanji', 'query': '木'}
search_response = requests.get('https://api.wanikani.com/v2/subjects', headers=headers, params=search_params).json()

# Get the ID of the "木" kanji
kanji_id = search_response['data'][0]['id']

# Get information about the "木" kanji
kanji_response = requests.get(f'https://api.wanikani.com/v2/subjects/{kanji_id}', headers=headers).json()

# Print all readings of the "木" kanji
for reading in kanji_response['data']['readings']:
    print(reading['reading'])
