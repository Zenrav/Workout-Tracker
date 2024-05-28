import requests
import datetime
APP_ID='c1168719'
API_KEY='6fcbfefb904efe54ac54442725297657'
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text=input('Enter the exercises you did today:  ')
GENDER='male'
WEIGHT_KG= 55
HEIGHT_CM= 167
AGE=19
sheety_endpoint='https://api.sheety.co/640f075c4f2d5b04280903670c416ced/workoutTracker/workouts'

headers={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters={
    'query': exercise_text,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}
response=requests.post(url=exercise_endpoint,json=parameters,headers=headers)
data=response.json()
data_exercise=data['exercises']

today=datetime.datetime.now()
today_date=today.strftime('%d/%m/%Y')
today_time=today.strftime('%X')

for exercise in data_exercise:
    sheety_params={
        'workout':{
            'date':today_date,
            'time':today_time,
            'exercise':exercise['name'].title(),
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories']
        }
    }
bearer_headers = {
"Authorization": "Bearer qwerty1234!@#"
}
sheet_response=requests.post(url=sheety_endpoint,json=sheety_params,headers=bearer_headers)
print(sheet_response.text)