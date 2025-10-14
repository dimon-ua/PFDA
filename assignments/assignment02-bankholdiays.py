# Program gets Link with JSON format, decode it in dict and make a selection of Bank Holidays dates
# Author: Dima Kozlovskyy 
import requests

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


# tricky part
# Program prints the bank holidays that are unique to northern Ireland
# (i.e. do not happen elsewhere in the UK)

uk_bank_holidays = []

for region in data:
    print(region)
    for event in data[region]['events']: 
        if 'bank' in event['title']: 
            print(event['title'])  
