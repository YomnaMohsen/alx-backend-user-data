#!/usr/bin/env python3
"""basic_auth module
"""


from .auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(
         self, authorization_header: str) -> str:
        """return  Base64 part of the Authorization header"""
        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
         self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string"""
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.b64decode(
                            base64_authorization_header).decode("utf-8")
            return decoded_value
        except(TypeError, base64.binascii.Error):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
         ) -> (str, str):
        """returns the user email and password from the Base64
        decoded value."""

        if isinstance(decoded_base64_authorization_header, str):
            split = decoded_base64_authorization_header.find(":")
            if split != -1:
                return (
                    decoded_base64_authorization_header[:split],
                    decoded_base64_authorization_header[split + 1:]
                )
        return (None, None)

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
         ) -> TypeVar('User'):
        """returns the User instance based on
        his email and password.
        """
        if not isinstance(user_email, str) or not user_email:
            return None
        if not isinstance(user_pwd, str)  or not user_pwd:
            return None
        try:
            user = (User.search({"email": user_email}))
            if not user:
                return None
            if (user[0].is_valid_password(user_pwd)):
                return user[0]
        except:
            return None
        