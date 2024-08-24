import json

import requests


# Извлеките данные из API и сохраните их в файле json.
def fetch_data_save():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        # Создание файла posts.json и сохранение данных внутри него.
        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("Данные были успешно извлечены и сохранены в posts.json.")

    except requests.exceptions.HTTPError as err_http:
        print("Http error : ", err_http)
    except requests.exceptions.ConnectionError as err_cn:
        print("Ошибка подключения : ", err_cn)
    except requests.exceptions.Timeout as err_time:
        print("Истекло время ожидания : ", err_time)
    except requests.exceptions.RequestException as err:
        print("Неожиданная ошибка : ", err)