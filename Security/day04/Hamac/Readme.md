If you've made it this far, you must be a crypto boss ;)

I'm going to challenge you with some AES...

To make it easier for you, here is how I encrypted my flag:

```py
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

print("Enter your password")
password = input(">>> ").encode()
h = HMAC.new(password, digestmod = SHA256)
h.update(b"POC2023")

iv = get_random_bytes(16)
k  = SHA256.new(password).digest()
c  = AES.new(k, AES.MODE_CBC, iv = iv).encrypt(pad(open("flag.txt", "rb").read(), 16))
r = {
	"iv": iv.hex(),
	"c": c.hex(),
	"h": h.hexdigest(),
}
open("output.txt", "w").write(json.dumps(r))
```

**{"iv": "eb5b0eef749406c48d222c3a0510b878", "c": "f442aec5f2dbec603ed6af079892109e202e340feb231f4758f80cfd64ee26e825c0692d02a719cac251492ec6e4e245", "h": "70fc9c22bb109cb2ff586555931f6b98ee7afd50eeb9ec095b02b930fd3f7be6"}**
