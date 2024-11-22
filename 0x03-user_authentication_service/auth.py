#!/usr/bin/env python3
"""auth module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """auth method"""
    psw_bytes = password.encode("utf-8")
    return bcrypt.hashpw(psw_bytes, bcrypt.gensalt())
