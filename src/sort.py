import logging

logger = logging.getLogger("sort")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/sort.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def sort_vacancies(vacancies: list, include_words: list = [], exclude_words: list = []) -> list:
    """Сортирует список вакансий, в названии которых есть слова из include_words.
    По умолчанию include_words = [], возвращает все вакансии.
    Исключает вакансии, в названии которых есть слова из exclude_words.
    По умолчанию exclude_words = [], не исключает никаких вакансий."""
    sorted_vacancies = []

    try:
        logger.info(f"Сортировка вакансий по ключевым словам: {include_words}, с исключением слов: {exclude_words}")
        for vacancy in vacancies:
            if all(word.lower() not in vacancy["name"].lower() for word in exclude_words):
                if len(include_words) == 0 or (any(word.lower() in vacancy["name"].lower() for word in include_words)):
                    sorted_vacancies.append(vacancy)

        start_len = len(vacancies)
        end_len = len(sorted_vacancies)
        logger.info(f"Отвергнуто {start_len - end_len} вакансий")
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")

    return sorted_vacancies


def sort_list(my_list: list, value: str) -> list:
    """Удаляет из списка элементы со значением value (необходимо для удаления пустых строк из списков сортировки)."""
    for _ in range(my_list.count(value)):
        my_list.remove(value)
    return my_list
