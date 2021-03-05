import requests
import time

class Monitor:

    def __init__(self):
        self.status = ""
        self.indicator = ""
        self.webhook_url = "INPUT WEBHOOK URL HERE"


    def monitor_status(self):

        while True:

            r = requests.get('https://status.nbatopshot.com/api/v2/status.json')
            data = r.json()

            if r.status_code == 200:
                pulled_status = data['status']['description']

                if pulled_status != self.status:
                    self.status = pulled_status
                    self.indicator = data['status']['indicator']
                    self.send_webhook()
                    print("STATUS UPDATE - UPDATE PUSHED!")

                else:
                    print("NO STATUS CHANGE!")

            else:
                print("ERROR w REQUEST")


            time.sleep(5)


    def send_webhook(self):
        data = {
          "embeds": [
            {
              "title": "Status Changed!",
              "description": "Top Shot Maintenance Monitor -",
              "fields": [
                {
                  "name": "Indicator",
                  "value": self.indicator
                },
                {
                  "name": "Description",
                  "value": self.status
                }
              ],
              "author": {
                "name": "Top Shot Status"
              }
            }
          ]
        }


        r = requests.post(self.webhook_url, json=data)
