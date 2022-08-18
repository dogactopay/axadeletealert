import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/delete_alert/{alert_id}")
async def read_item(alert_id):
    resp = requests.delete(f"https://axa-alerts.monitorpark.net/api/alert/{alert_id}",headers={'Authorization': f'Key PRhOXD4TGnO2JTxKB2kRZRhDbHT7caIAqErn32A7','content-type': 'application/json'}).text
    return resp