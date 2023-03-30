from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def load_test(self):
        self.client.get("/predict")
        self.client.post("/predict")