import time
from getpass import getuser

response_code = {100: 'базовое уведомление', 101: 'важное уведомление',
                 200: 'OK', 201: '(created) — объект создан', 202: '(accepted) — подтверждение',
                 400: 'неправильный запрос/JSON-объект', 401: 'не авторизован', 402: 'неправильный логин/пароль',
                 403: '(forbidden) — пользователь заблокирован',
                 404: '(not found) — пользователь/чат отсутствует на сервере',
                 409: '(conflict) — уже имеется подключение с указанным логином',
                 410: '(gone) — адресат существует, но недоступен (offline)',
                 500: 'ошибка сервера'}


def get_presence():
    presence = {
        "action": "presence",
        "time": time.time(),
        "type": "status",
        "user": {
            "account_name": getuser(),
            "status": "onlain"
                }
    }
    return presence


def get_response(num):
    response = {
        "response": num,
        "time": time.time(),
        "alert": response_code[num]
    }
    return response


def create_response(data):
    ''' Должна быть проверка на исключения, но пока так '''
    return get_response(200)
