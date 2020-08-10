from datetime import datetime, timedelta
import jwt
import time

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

with open("key_files/rnd-private-key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

data = {
    "iss": '''app''',
    "aud": '''sync-up-lambda''',
    "exp": int(round(time.time() * 1000)).__add__(5 * 60 * 1000),
    "nbf": datetime.utcnow(),
    "sub": "CustomerApp",
    "request": {"name": "yak", "purpose": "shave"}
}
print('data:: '+ str(data))

jwt_token = jwt.encode(data, key=private_key, algorithm='RS512')

print('jwt_token:: ' + str(jwt_token))

with open("key_files/rnd-public-key.pub", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

dtoken = jwt.decode(jwt_token, public_key, audience='''sync-up-lambda''',
                    issuer='''app''')
print('decoded with public key :: ' + str(dtoken))
