import requests
class RandomUser:
    baseURL = "https://randomuser.me/api/"
    def __init__(self):
        """
        This class will be used to get a random user from the randomuser.me API.
        """
        response = requests.get(self.baseURL).json()
        self._data = response["results"][0]