import hashlib
from datetime import datetime, timedelta, timezone
import sys

def datetime_to_timestamp(datetime_str):
    format = "%Y-%m-%d %I:%M:%S%p"
    datetime_obj = datetime.strptime(datetime_str, format)
    datetime_obj = datetime_obj.replace(tzinfo=timezone.utc)
    return int(datetime_obj.timestamp() * 1000)

def generate_reset_token(username, datetime_str):
    timestamp = datetime_to_timestamp(datetime_str)
    tokens = []
    for offset in range(-1000, 1000):
        adjusted_timestamp = timestamp + offset
        data = username + str(adjusted_timestamp)
        token = hashlib.md5(data.encode()).hexdigest()
        tokens.append((token, adjusted_timestamp))
    return tokens

if __name__ == '__main__':
    try:
        user = sys.argv[1]
        generated = sys.argv[2]
        tokens = generate_reset_token(user, generated)
        for token, ts in tokens:
            print(f"Token: {token}, Timestamp: {ts}")
            with open("wTokenHashes.txt", "a") as file:
                file.write(f"{token}\n")
    except IndexError:
        print(f"Usage: {sys.argv[0]} <username> <datetime>")
