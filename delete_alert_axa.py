import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/delete_alert/{alert_id}")
async def read_item(alert_id):
    resp = requests.put(f"https://axa-alerts.monitorpark.net/api/alert/{alert_id}",headers={'Authorization': f'Key PRhOXD4TGnO2JTxKB2kRZRhDbHT7caIAqErn32A7','content-type': 'application/json'}).text
    return 







class alert_close(BaseModel):
    alert_id: str
    

@app.post("/delete_alert_post/")
async def signup(item: alert_close):
    resp = requests.put(f"https://axa-alerts.monitorpark.net/api/alert/{dict(item)['alert_id']}",headers={'Authorization': f'Key PRhOXD4TGnO2JTxKB2kRZRhDbHT7caIAqErn32A7','content-type': 'application/json'}).text
    return status
