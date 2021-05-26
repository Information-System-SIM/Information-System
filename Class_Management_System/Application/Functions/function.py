import os
from Class_Management_System.settings import BASE_DIR


def transfer(date_str,time_str):
    lst = str(date_str).split("/")
    time_lst = str(time_str).split(":")
    result = lst[-1] + "-" + lst[0] + "-" + lst[1] + " " + time_lst[0] + ":" + time_lst[1] + ":00"
    return result

def get_image_path(student_num):
    path = "/Image/" + student_num + ".jpeg"
    files = os.listdir(os.path.join(BASE_DIR, 'static/Image/'))
    default_path = "/Image/default.png"
    if str(student_num) + ".jpeg" not in files:
        path = default_path
    return path