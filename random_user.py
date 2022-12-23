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
    def get_email(self):
        """
        Returns the email of the user
        """
        return self._data['email']
    def get_phone(self):
        """
        Returns the phone number of the random user
        """
        return self._data['phone']
    def get_location(self):
        """
        Returns the location of the random user
        """
        l=self._data['location']
        return l 
    def get_picture(self):
        """
        Returns the picture of the random user
        """
        return self._data['picture']