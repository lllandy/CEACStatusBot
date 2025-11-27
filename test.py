import os
from CEACStatusBot import query_status,OnnxCaptchaHandle

try:
    NUMBER = os.environ["NUMBER"]
    PASSPORT_NUM = os.environ["PASSPORT_NUM"]
    SURNAME = os.environ["SURNAME"]
    print(query_status(NUMBER,PASSPORT_NUM,SURNAME,OnnxCaptchaHandle("captcha.onnx")))
except KeyError:
    print("ENV Error")
