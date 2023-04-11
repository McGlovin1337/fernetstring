from cryptography.fernet import Fernet
from fernetstring.keyfuncs import machine_key


class FernetString:
    def __init__(self, input_string: str | bytes, key: bytes = machine_key()) -> None:
        self._secure_string = input_string if isinstance(input_string, bytes) else self._encrypt(input_string, key)

    @property
    def secure_string(self):
        return self._secure_string

    @classmethod
    def from_secure_string(cls, secure_string: bytes):
        return cls(secure_string)

    def _encrypt(self, input_str: str, key: bytes) -> bytes:
        fernet = Fernet(key)

        return fernet.encrypt(input_str.encode('utf-8'))

    def decrypt(self, key: bytes = machine_key()) -> str:
        fernet = Fernet(key)

        return fernet.decrypt(self.secure_string).decode('utf-8')
