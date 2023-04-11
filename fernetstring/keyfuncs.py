"""Collection of wrapped functions that return a compatible Fernet encryption key"""
import base64
import hashlib


def fernet_key(func) -> bytes:
    """Wrapper Function that returns a Fernet compatible base64 encoded byte string\
        for any method that returns a standard str

    Args:
        func (function): The wrapped function

    Returns:
        bytes: Fernet compatible base64 encoded byte string
    """
    def inner():
        input_str = func()
        md5_hex = hashlib.md5(input_str.encode('utf-8')).hexdigest()
        key = base64.urlsafe_b64encode(md5_hex.encode())
        return key

    return inner


@fernet_key
def test_key() -> str:
    """This generates a simple test str

    Returns:
        str: 'TestKey'
    """
    return 'TestKey'


@fernet_key
def machine_key() -> str:
    """Returns the Operating System machine-id string

    Returns:
        str: Operating System machine-id
    """
    with open('/etc/machine-id', 'r', encoding='utf-8') as file:
        return file.readline().strip('\n')


def user_key(input_str: str) -> str:
    """Returns the input string argument

    Args:
        input_str (str): Input String

    Returns:
        str: Input String
    """
    @fernet_key
    def _user_key() -> str:
        return input_str

    return _user_key()
