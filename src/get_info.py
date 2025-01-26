import requests
import logging


logger = logging.getLogger("vacancies")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/vacancies.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_info() -> list:
    """Возвращает список вакансий с заданной зарплатой, опубликованных на сайте hh.ru за сегодняшний день."""
    base_url = "https://api.hh.ru/vacancies"
    params = {
        "text": "",
        "period": 1,
        "only_with_salary": True,
        "per_page": 100,
        "page": 0,
    }
    vacancies = []
    info = requests.get(base_url, params).json()
    try:
        while True:
            logger.info(f"Просмотр страницы номер {params["page"]}")
            if info.get("items"):
                vacancies += info["items"]
            if info["pages"] == params["page"]:
                break
            else:
                params["page"] += 1

        result = []
        for item in vacancies:
            vacancy = {
                "name": item["name"],
                "url": item["alternate_url"]
            }
            if item.get("salary"):
                vacancy["salary"] = {
                    "from": item["salary"]["from"],
                    "to": item["salary"]["to"],
                }
            result.append(vacancy)
        logger.info(f"Всего вакансий: {info["found"]}")
        logger.info(f"Просмотрено вакансий: {len(vacancies)}")
        return result
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []

