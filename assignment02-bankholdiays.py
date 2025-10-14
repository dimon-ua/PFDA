# Program gets Link with JSON format, decode it in dict and make a selection of Bank Holidays dates
# Author: Dima Kozlovskyy 
#
import requests

# just making some changes for git
url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

bank_holidays_dates = []

event_index = 0

while event_index < len(data['northern-ireland']['events']):
    if 'bank' in data['northern-ireland']['events'][event_index]['title']:
        bank_holidays_dates.append(data['northern-ireland']['events'][event_index]['date'])
        
    event_index += 1


    
print(bank_holidays_dates)