from get_info import get_info
from sort import sort_vacancies, sort_list
from file_saver import save_to_file
import datetime
import logging


logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/main.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def main():
    try:
        logger.info(f"Начало работы программы в {datetime.datetime.now()}")
        today_vacancies = get_info()

        logger.info("Запрос от пользователя")
        include = input("Введите слова для поиска (через запятую): ")
        exclude = input("Введите слова, которые нужно исключить из поиска (через запятую): ")

        include_list = sort_list(include.replace(" ", "").split(","), "")
        exclude_list = sort_list(exclude.replace(" ", "").split(","), "")
        logger.info(f"Полученные списки: include_list = {include_list}, exclude_list = {exclude_list}")

        sorted_vacancies = sort_vacancies(today_vacancies, include_list, exclude_list)

        time = datetime.datetime.now()
        date = time.strftime("%d_%m_%Y")
        words = "_".join(include_list).lower()

        file_name = f"../data/{date}_{words}.json"
        logger.info(f"Сохранение в файл {file_name}")

        save_to_file(file_name, sorted_vacancies)
        for i in sorted_vacancies:
            print(i)

        logger.info(f"Конец работы программы в {datetime.datetime.now()}")
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")

if __name__ == "__main__":
    main()
