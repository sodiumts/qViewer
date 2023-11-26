import requests

class DataScraper():
    def __init__(self, providedCookie, providedSessionToken) -> None:
        # Initialize the session
        self.session = requests.Session()
        self.cookie = {"ClientToken": providedCookie}

        self.refreshHeader = {
                "Authorization" : f"Bearer {providedSessionToken}",
                "Connection" : "keep-alive",
                "Cache-Control" : "no-cache",
                "Content-Type" : "application/json; charset=utf-8"
            }
        # Acquire the accessToken 
        


    def getRooms(self) -> list:
        response1 = self.session.post("https://horus.apps.utwente.nl/api/auth/token/refresh", headers=self.refreshHeader, cookies=self.cookie)
        if response1.status_code == 200:
            self.rooms_access_token = response1.json()['accessToken']
        else:
            print(f"Error getting the access_token, status code: {response.status_code}")
            exit()
        headers2 = {
            'Authorization' : f"Bearer {self.rooms_access_token}",
            "Connection" : "keep-alive",
            "Cache-Control" : "no-cache",
            "Content-Type" : "application/json; charset=utf-8"
        }
        
        response = self.session.get("https://horus.apps.utwente.nl/api/queuing/197/rooms", headers=headers2)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting the rooms list, status code: {response.status_code}")
            exit()
