import json
import requests
from google.oauth2 import service_account

def lambda_handler(event, context):
    # Get the purchase token from the event
    purchase_token = event["purchaseToken"]
    
    # Load the Google Play Developer API credentials
    credentials = service_account.Credentials.from_service_account_file('path/to/credentials.json')
    
    # Set up the API request
    url = "https://www.googleapis.com/androidpublisher/v3/applications/" + event["packageName"] + "/purchases/products/" + event["productId"] + "/tokens/" + purchase_token
    headers = {
        "Authorization": "Bearer " + credentials.token,
        "Accept": "application/json"
    }
    
    # Send the API request
    response = requests.get(url, headers=headers)
    
    # Parse the API response
    response_json = json.loads(response.text)
    
    # Verify the purchase data
    if response_json["purchaseState"] == 0 and response_json["consumptionState"] == 1 and response_json["productId"] == event["productId"]:
        # Purchase is valid, mark it as consumed
        url = "https://www.googleapis.com/androidpublisher/v3/applications/" + event["packageName"] + "/purchases/products/" + event["productId"] + "/tokens/" + purchase_token + ":consume"
        response = requests.post(url, headers=headers)
        return {"status": "success"}
    else:
        # Purchase is invalid
        return {"status": "fail"}
