# Program gets Link with JSON format, decode it in dict-format and make a selection of Bank Holidays dates
# Author: Dima Kozlovskyy 
#
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

    
print("Northern Ireland:", bank_holidays_dates)



# tricky part   DATES
# Program prints the bank holidays that are unique to northern Ireland
# (i.e. do not happen elsewhere in the UK)

uk_bank_holidays_dates = []

for region in data:
    if region != 'northern-ireland':
        for event in data[region]['events']:
            uk_bank_holidays_dates.append(event['date'])

print("Other UK:", uk_bank_holidays_dates)




unique_bank_holidays_ie = []

for date in bank_holidays_dates:
    if date not in uk_bank_holidays_dates:
        unique_bank_holidays_ie.append(date)


print("Unique dates for Northern-Ireland:", unique_bank_holidays_ie)


# tricky part   TITLES
# Program prints the bank holidays that are unique to northern Ireland
# (i.e. do not happen elsewhere in the UK)

uk_bank_holidays_titles = []

for region in data:
    # print(region)
    if region != 'northern-ireland':     
        for event in data[region]['events']:
            if 'bank' in event['title'].lower():
                uk_bank_holidays_titles.append(event['title'])
                
print(uk_bank_holidays_titles)

bank_holidays_titles_ie = []

for region in data:
    # print(region)
    if region == 'northern-ireland':     
        for event in data[region]['events']:
            if 'bank' in event['title'].lower():
                bank_holidays_titles_ie.append(event['title'])
                

unique_bank_holidays_titles_ie = []

for event in data['northern-ireland']['events']:
    if 'bank' in event['title'].lower() and event['title'] not in uk_bank_holidays_titles:
        unique_bank_holidays_titles_ie.append(event['title'])

print(unique_bank_holidays_titles_ie)

# looks like it doesnt work propely, needs to make some changes
