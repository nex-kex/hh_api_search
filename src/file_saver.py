import json
import logging


logger = logging.getLogger("saving")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/saving.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def save_to_file(file_path: str, data: list) -> None:
    """Сохраняет список data в файл file_path в формате JSON."""

    try:
        logger.info(f"Попытка записи в файл {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")
