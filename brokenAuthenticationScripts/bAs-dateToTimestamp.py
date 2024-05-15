from datetime import datetime
import sys

def datetime_to_timestamp(datetime_str):
    format = "%Y-%m-%d %H:%M:%S"
    datetime_obj = datetime.strptime(datetime_str, format)
    timestamp = datetime_obj.timestamp()
    return int(timestamp * 1000)


if __name__ == '__main__':
    try:
        datetime_str = sys.argv[1]
        timestamp = datetime_to_timestamp(datetime_str)
        print(f"{timestamp}")
    except IndexError:
        print(f'Usage: {sys.argv[0]} "<2024-05-04 15:12:08>"')
