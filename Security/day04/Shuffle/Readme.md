When I reverse engineered a program I was able to reconstruct the encryption function:

```py
import random

flag = list(open("flag.txt", "rb").read().strip())
random.seed(random.randint(0, 256))
random.shuffle(flag)
print(bytes(flag).decode())
```

The hash seems to have been generated randomly, could you help me to find it?

**6364493633371377e52fb77f256o3f74273}345496f7C5a3633344367f69c63c{5P76**
