import json

from aylienapiclient import textapi
import csv,io
# client=textapi.Client("your_app_ID", "your_application_key")
# # sentiment=client.Sentiment({'text':'enter some of your own text here'})
# client=textapi.Client("4507cc1b","0350a64fad617ab25c4b9820b25b9124")
# sentiment=client.Sentiment({'text':'this is the first line'})
# print(sentiment)
"""
json_data='{"name":"smith","email":"smithjack@gmail.com"}'
json_parsed=json.loads(json_data)
print(json_parsed['email'])
"""
employee_data='{"employee_details":[{"employee_name":"James","email":"james@gmail.com","job_profile":"Sr. Developer"}]}'
employee_parsed=json.loads(employee_data)
emp_data=employee_parsed['employee_details']
# open a file for writing
employee_data=open('data.csv','w+')
#create the csv writer object
csvwriter=csv.writer(employee_data)
count=0
for emp in employee_data:
    if count==0:
        header=emp.keys()
        csvwriter.writerow(header)
        count+=1
    csvwriter.writerow(emp.values())
employee_data.close()


#initialize a new client of AYLIEN Text API
client=textapi.Client("4507cc1b","0350a64fad617ab25c4b9820b25b9124")

with io.open('Trump_Tweets.csv','w',encoding='utf-8',newline='')as csvfile:
    csv_writer=csv.writer(csvfile)
    csv_writer.writerow(["Tweet","Sentiment"])
    with io.open("Trump.txt",'r',encoding='utf-8') as f:
        for tweet in f.readlines():
            # remove extra spaces or newlines around the text
            tweet=tweet.strip()

            # reject tweets which are empty so you dont waste your API credits
            if len(tweet)==0:
                print('skipped')
                continue

            print(tweet)


            # make call to AYLIEN text API
            sentiment=client.Sentiment({'text':tweet})

            # write the sentiment result into csv file
            csv_writer.writerow([sentiment['text'],sentiment['popularity']])
