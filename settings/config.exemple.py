"""Модуль с настройками доступа к API Kinoposk.dev"""


class Settings:
    """ Класс настроек"""
    def __init__(self):
        self.api_version: str = "v1.4"  # версия API Kinopoisk
        self.api_url: str = f"https://api.kinopoisk.dev/{self.api_version}"
        self.api_key: str = "Ключ к API, полученный через телеграм бот @kinopoiskdev_bot"
