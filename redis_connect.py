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

for _, row in df.iterrows():
    patient_data = row.to_dict()
    # Uses PatientID as the key and the rest as a serialized JSON string
    r.set(patient_data['PatientID'], json.dumps(patient_data))


# if r.exists(1):
#     print("Key 'P001' exists in Redis.")

#     # Retrieve and decode the value
#     stored_data = json.loads(r.get(1))
#     print("Stored data for PatientID P001:", stored_data)
# else:
#     print("Key 'P001' does not exist in Redis.")