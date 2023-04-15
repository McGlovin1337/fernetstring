# fernetstring
A simple package that provides a string encrypted by the cryptography.fernet module in class.
This package also provide functions for producing an encryption key from a number of sources.
A wrapper function - fernet_key, is available that produces a fernet compatible encryption key from a function that returns a string.

## Usage

This example encrypts the string 'test' using the default encryption key used by the FernetString class:

```python
import fernetstring as fstr

my_secure_string = fstr.FernetString('test')
print('Encrypted String: ' + str(my_secure_string.secure_string))
Output: Encrypted String: b'gAAAAABkOqoSLOnlWVFTrIn0r2gWyr5ahfRfbrO_DddYs5TskWfENaws2o91WXIaXVucG-k89lgWYAyqdxmiA8_F-zbKctiZ1Q=='

print('Original String: ' + my_secure_string.decrypt())
Output: test
```

Use a user defined encryption key:

```python
import fernetstring as fstr
from fernetstring import keyfuncs

my_secure_string = fstr.FernetString('test', keyfuncs.user_key('secretkey'))
print('Encrypted String: ' + str(my_secure_string.secure_string))
Output: Encrypted String: b'gAAAAABkOsGf0GIWbCEuqU6ykKOfXRHJ6Bb7tnMU7jO3dN2nz19FjzRR38SSMauy16RvKvteAJMOJ5B8O7eFYSBAhCX6SccRBw=='

print('Original String: ' + my_secure_string.decrypt(keyfuncs.user_key('secretkey')))
Output: test
```

Use a custom function to produce an encryption key:

```python
import fernetstring as fstr
from fernetstring.keyfuncs import fernet_key

@fernet_key
def super_secret_key() -> str:
    return 'Password123'

my_secure_string = fstr.FernetString('test', super_secret_key())
print('Encrypted String: ' + str(my_secure_string.secure_string))
Output: Encrypted String: b'gAAAAABkOsM_ykKQ5UA62bVP2iMQTrK4t-uFh7Hvu6E2RvAovOEccauYay6uX5HxViLDhBD2EI2MuSphjp6Xlw77gARxhTUlWA=='

print('Original String: ' + my_secure_string.decrypt(super_secret_key()))
Output: test
```