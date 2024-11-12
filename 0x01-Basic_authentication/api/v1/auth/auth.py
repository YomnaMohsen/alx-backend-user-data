#!/usr/bin/env python3
"""auth module"""
from flask import request 
from typing import List, TypeVar
from models.user import User


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """args: path,excluded_paths """
        return False
    
    
    def authorization_header(self, request=None) -> str:
        """takes req as param"""
        return None
    
    
    def current_user(self, request=None) -> TypeVar("User"): # type ignore
        """args request"""
        return None
