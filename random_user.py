import requests
class RandomUser:
    baseURL = "https://randomuser.me/api/"
    def __init__(self):
        """
        This class will be used to get a random user from the randomuser.me API.
        """
        response = requests.get(self.baseURL).json()
        self._data = response["results"][0]


    def get_first_name(self)->str:
        """
        Returns the first name of the user.
        """
        return self._data["name"]["first"]

    def get_last_name(self)->str:
        """
        Returns the last name of the user.
        """
        return self._data["name"]["last"]

    def get_full_name(self)->str:
        """
        Returns the full name of the user.
        """
        return f"{self.get_first_name()} {self.get_last_name()}"
    def get_email_name(self)->str:
        """
        Returns the email name of the user.
        """
        return self._data["email"]
    def get_phone_name(self)->str:
        """
         Returns the phone name of the user
        """
        return self._data["phone"]
    def get_location_name(self)->str:
        """
         Returns the locaion name of the user
        """
        return self._data["location"]
    def get_picture_name(self)->str:
         """
         Returns the picture name of the user
        """
         return self._data["picture"]
    def get_users(self):
        """
         Returns a list of RandomUser objects
        """
        return f'{self.get_first_name()} {self.get_last_name()} {self.get_full_name()} {self.get_email_name()} {self.get_location_name()} {self.get_picture_name}'

