import os

import requests
from fastapi import HTTPException


class UserService:
    URL = os.getenv("USER_SERVICE_URL", "http://test.com/")

    @staticmethod
    def get_all_users():
        response = requests.get(UserService.URL + "users")
        status = response.status_code

        if 200 <= status < 300:
            return response.json()["users"]
        else:
            raise HTTPException(status_code=500, detail="User Service Error")