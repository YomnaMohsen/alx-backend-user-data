#!/usr/bin/env python3
"""auth module"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """args: path,excluded_paths """
        if (path and excluded_paths):
            p = path if path[-1] == '/' else path + "/"
            if (p in excluded_paths):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """takes req as param"""
        if request:
            if 'Authorization' in request.headers:
                return request.headers['Authorization']
                
        return None

    def current_user(self, request=None) -> TypeVar("User"):   # type ignore
        """args request"""
        return None
