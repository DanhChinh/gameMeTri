import time
import json
def get_time(options = "full"):
    # Lấy thời gian hiện tại dưới dạng struct_time
    current_time = time.localtime()

    # Lấy các thành phần của thời gian hiện tại
    minute = current_time.tm_min
    hour = current_time.tm_hour
    day = current_time.tm_mday
    month = current_time.tm_mon
    year = current_time.tm_year
    if options == "full":
        return f"{hour}:{minute} {day}/{month}"
    if options == "hour":
        return hour
    return f"{day}-{month}"
def get_total(string):
    try:
        return eval(string)
    except:
        return "???"

def read_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Ghi dữ liệu vào file JSON
def write_data_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
