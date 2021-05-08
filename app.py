import requests
import time

class Monitor:

    def __init__(self):
        self.status = ""
        self.indicator = ""
        self.webhook_url = "https://discord.com/api/webhooks/840426783828475954/cM4bnSRwZrQy2D_WQvdWIMnAW-0XSyQVKK4Ej_oqHSuaGtsL3BWZSlEfgz3ORpk6qj7H"


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
              "description": "TopShot Marketplace Maintenance Monitor -",
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
                "name": "NBA TopShot Status"
              },
              "footer": {
                "text" : "Made by Adi | Heavydrops CG"
              }
            }
          ]
        }


        r = requests.post(self.webhook_url, json=data)
