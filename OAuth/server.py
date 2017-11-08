## FOR DATASHARK
client_id = '228MWF'
client_secret = 'ed16cd1e79a28f00c990e304b87f3bb6'


## FOR SPECIFIC USER - ROHAN - CONFIDENTIAL
access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1U1pMN0YiLCJhdWQiOiIyMjhNV0YiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJhY3QgcnNldCBybG9jIHJ3ZWkgcmhyIHJwcm8gcm51dCByc2xlIiwiZXhwIjoxNTA3NDM5OTc3LCJpYXQiOjE1MDc0MTExNzd9.RGXvH1fUoAJjhqGEwP_wsjL7MYkP2xvzQgs36BtxlvA'
refresh_token = 'bbb44b3a0e05a4235b9bd837481d4796372ee3d51d5a1f4b2b82af4c85216534'


import requests
import json
import pandas as pd
from collections import defaultdict

header = {'Authorization': 'Bearer ' + access_token}


## FOR FITBIT DAILY ACTIVITY SUMMARY

fitbit_daily_activity_summary_values = ['lightlyActiveMinutes', 'caloriesBMR', 'caloriesOut', 'marginalCalories', 'fairlyActiveMinutes', 'veryActiveMinutes', 'sedentaryMinutes', 'restingHeartRate', 'elevation', 'activityCalories', 'activeScore', 'floors', 'steps']
fitbit_daily_activity_summary_endpoint = 'https://api.fitbit.com/1/user/-/activities/date/2017-9-{0}.json'

dict = defaultdict(lambda: [])

for date in range(1, 30):
	endpoint = fitbit_daily_activity_summary_endpoint.format(str(date).zfill(2))
	print(endpoint)
	response = requests.get(endpoint, headers=header)
	parsed = json.loads(response.text)

	print(date)
	for value in fitbit_daily_activity_summary_values:
		if value in parsed['summary']:
			dict[value].append(parsed['summary'][value])
		else:
			dict[value].append(None)
	if 'distances' in parsed['summary']:
		distances = parsed['summary']['distances']
		if len(distances) > 0:
			if 'distance' in distances[0]:
				dict['distance'].append(distances[0]['distance'])

fitbit_daily_activity_summary_df = pd.DataFrame(dict)