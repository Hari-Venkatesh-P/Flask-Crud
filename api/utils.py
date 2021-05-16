from flask import make_response


def send_response(data, status_code):
    response = make_response(data, status_code)
    cnt_type = "application/json; charset=utf-8"
    response.headers["Content-Type"] = cnt_type
    return response

def list_to_dict(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct