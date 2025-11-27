from .handle import NotificationHandle
from CEACStatusBot.request import query_status, update_last_update_date
from CEACStatusBot.captcha import CaptchaHandle,OnnxCaptchaHandle

class NotificationManager():
    def __init__(self,number:str, passport_number:str, surname:str, captchaHandle:CaptchaHandle=OnnxCaptchaHandle("captcha.onnx")) -> None:
        self.__handleList = []
        self.__number = number
        self.__passport_number = passport_number
        self.__surname = surname
        self.__captchaHandle = captchaHandle

    def addHandle(self, notificationHandle:NotificationHandle) -> None:
        self.__handleList.append(notificationHandle)

    def send(self, last_update_date, always_notify=False) -> None:
        res = query_status(self.__number, self.__passport_number, self.__surname, self.__captchaHandle)
        
        if res["case_last_updated"] != last_update_date:
            update_last_update_date(res["case_last_updated"])

        if res["case_last_updated"] != last_update_date or always_notify:
            for notificationHandle in self.__handleList:
                notificationHandle.send(res)
