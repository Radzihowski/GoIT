import logging

# створюємо handler для виведення в консоль та встановлюємо рівень DEBUG
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

# створюємо форматтер: час виведення (asctime), ім'я модуля (name), рівень (levelname) та саме повідомлення (message)
formatter = logging.Formatter(f"%(asctime)s [%(levelname)s] - %(name)s - %(funcName)s(%(lineno)d) - %(message)s")

# додаємо зазначений форматтер до handler ch
sh.setFormatter(formatter)

# Створюємо файловий handler для логера:
fh = logging.FileHandler("data/app.log")
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

def get_logger(file_name: str):
    # створюємо логер, даємо йому ім'я та встановлюємо рівень logging.DEBUG
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)
    # додаємо handler sh до логера
    logger.addHandler(sh)
    # додаємо файловий handler fh до логера
    logger.addHandler(fh)
    return logger

