import pandas as pd
import redis
import os
from dotenv import load_dotenv
import json

load_dotenv()

redis_password = os.getenv('redis_password')
df = pd.read_csv('patient_info.csv')

r = redis.Redis(
  host='redis-12009.c124.us-central1-1.gce.redns.redis-cloud.com',
  port=12009,
  password=redis_password,
  decode_responses=True    
)

# Dump dataset to Redis database
for _, row in df.iterrows():
    patient_data = row.to_dict()
    # Uses PatientID as the key and the rest as a serialized JSON string
    r.set(patient_data['PatientID'], json.dumps(patient_data))

# Get PatientID = 1 data
patient_1_data = r.get(1)  # returns a string data type, not dict
patient_1_dict = json.loads(patient_1_data)  # convert to dict

# Update the treatment plan
patient_1_dict['TreatmentPlan'] = "Occupational Therapy"

# Save that change to Redis
r.set(1, json.dumps(patient_1_dict))