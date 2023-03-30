from locust import HttpUser, task
import json

class LoadTest(HttpUser):
    @task
    def load_test(self):

        payload = {
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
}

        
        headers = {'Content-Type': 'application/json'}
        self.client.get("/")
        self.client.post("/predict",data=json.dumps(payload),headers=headers)