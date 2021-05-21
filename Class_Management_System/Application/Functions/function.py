def transfer(date_str,time_str):
    lst = str(date_str).split("/")
    time_lst = str(time_str).split(":")
    result = lst[-1] + "-" + lst[0] + "-" + lst[1] + " " + time_lst[0] + ":" + time_lst[1] + ":00"
    return result