from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError

_password_hasher = PasswordHasher()


def hash_password(plain_password: str) -> str:
    """Return a salted Argon2id hash of the password."""
    return _password_hasher.hash(plain_password)


def verify_password(plain_password: str, password_hash: str) -> bool:
    """Return True only if the password matches the stored hash."""
    try:
        return _password_hasher.verify(password_hash, plain_password)
    except (VerificationError, InvalidHashError):
        return False