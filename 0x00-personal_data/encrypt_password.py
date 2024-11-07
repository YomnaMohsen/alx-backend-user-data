#!/usr/bin/env python3
"""encrypted password module"""
import bcrypt


def hash_password(password: str) -> bytes:
    """function that returns hashed password
    that is passed as parameter"""
    psw_bytes = password.encode("utf-8")
    return bcrypt.hashpw(psw_bytes, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """check if password arg is valid or not"""
    psw_bytes = password.encode("utf-8")
    return bcrypt.checkpw(psw_bytes, hashed_password)
