"""
Логика голосового ассистента.
Выступает в роли независимого-класса.
Реализован паттерн Моносостояние
"""
import sys

import speech_recognition
import speech_recognition as sr
import os
from gtts import gTTS
import random
import file_data_manager as FDM
import pyaudio
from playsound import playsound     # для воспроизведения звука
from observer import Subject        # импорт наблюдаемого класса
#from pyau import play


class Assistant(Subject, FDM.DataMixin):
    """Класс голосового помощника"""
    def __new__(cls, *args, **kwargs):  # элементарный конструктор класса
        if not hasattr(cls, 'instance'):    # Синглтон
            cls.instance = super().__new__(cls)
        return cls.instance

    # Моносостояние
    MONOCONDITIONAL_DATA = {
        'recognizer': sr.Recognizer(),
        'data': FDM.config_data,
        'threadAwait_flag': False,
        "ERRORLIMIT": 3,
    }

    def __init__(self, mode="commands"):    # элементарный инициализатор класса
        self.__dict__ = self.MONOCONDITIONAL_DATA
        super().__init__()
        self.phrases = []
        self.source = sr.Microphone(device_index=1)
        self.mode = mode
        self.user_num: int

    def execute(self):
        """Запуск помощника"""

        if not FDM.is_any_registrated():
            self.mode = "service"
            self.name, self.age, self.keyword = self.register()
        else:
            self.name, self.age, self.keyword = FDM.get_user_info(self.user_num)
        self.mode = "commands"
        self.answer(f"Привет, {self.name}", continue_target='commands')

    def askWhileFalse(self, text_to_reanswer: str, text_to_answer_finally: str, type_: str):
        """Функция для переспрашивания, пока не истинно условие"""
        try:
            try_phrase = self.listen_service(phrase_to_reanswer=text_to_reanswer)
            if validDate(type_, try_phrase):
                self.answer(continue_target='service', response=text_to_answer_finally)
                return try_phrase
            return self.askWhileFalse(type_, text_to_reanswer, text_to_answer_finally)
        except RecursionError:
            return "Ошибка регистрации"

    def speechExceptionCommands(func):
        """Декоратор прослушивания команд"""
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except speech_recognition.UnknownValueError:
                print('UnknownValueError')
                # проверка на превышение времени отклика пользователя
                self.reanswer_phrases += 1
                if self.reanswer_phrases >= self.ERRORLIMIT:
                    # self.send_error()
                    return
                else:
                    self.answer(self.answer(random.choice(self.data['commands']["misunderstand"]['response']),
                                            continue_target="commands"))
            except speech_recognition.WaitTimeoutError:
                print('WaitTimeoutError')
                # проверка на превышение времени отклика пользователя
                self.reanswer_phrases += 1
                if self.reanswer_phrases >= self.ERRORLIMIT:
                    # self.send_error()
                    return
                else:
                    self.answer(random.choice(self.data['commands']['silence']['response']),
                                continue_target="commands")
        return wrapper

    def speechExceptionService(func):
        """Декоратор прослушивания сервисных фраз"""
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except speech_recognition.UnknownValueError:
                print("serv", 'UnknownValueError')
                print(self, args, kwargs)
                self.answer(response=kwargs['phrase_to_reanswer'],
                            continue_target="service")
            except speech_recognition.WaitTimeoutError:
                print("serv", 'WaitTimeoutError')
                print(self, args, kwargs)
                self.answer(response=kwargs['phrase_to_reanswer'],
                            continue_target="service")
        return wrapper

    def register(self):
        """Проверка на регистрацию -> регистрация"""
        if not FDM.isRegistrated():
            self.answer(response='Привет, давай познакомимся!', continue_target='service')
            self.answer(response='Как тебя зовут?', continue_target='service')
            try_name = self.askWhileFalse(type_='str', text_to_reanswer='Не понимаю! Как тебя зовут?',
                                          text_to_answer_finally='Отлично! Сколько тебе лет?')
            print('age')
            try_age = self.askWhileFalse(type_='int', text_to_reanswer='Не понимаю! Сколько тебе лет?',
                                          text_to_answer_finally='Отлично! Придумай кодовое слово?')
            print('password')
            try_password = self.askWhileFalse(type_='str', text_to_reanswer='Не понимаю! Придумай кодовое слово?',
                                          text_to_answer_finally='Отлично! Регистрация закончена!')

            return FDM.register(try_name, try_age, try_password)

    @speechExceptionCommands
    def listen_commands(self):   # метод прослушивания команд
        # listening
        with self.source as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source=source, timeout=4)
            text = self.recognizer.recognize_google(audio_data=audio, language='ru_RU')

        # setting user phrase
        self.phrases.append(("Me: ", text))
        self.set_data(self.phrases)
        # matching with commands data
        return self.matchText(text)

    @speechExceptionService
    def listen_service(self, phrase_to_reanswer):
        # listening
        with self.source as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source=source, timeout=4)
            text = self.recognizer.recognize_google(audio_data=audio, language='ru_RU')

        # setting user phrase
        self.phrases.append(("Me: ", text))
        self.set_data(self.phrases)
        return text

    # поиск фразы в триггерах - ответ
    def matchText(self, phrase: str):   # распознает команды
        # проходимся по каждой команде из бд
        print('распознование')
        for command in self.data['commands']:
            # проверка на наличие слова-триггера в списке триггеров команды (триггер = спусковой крючок)
            if phrase.lower().strip() in self.data['commands'][command]["trigger"]:
                if command in FDM.commands_functions_dict:
                    response = FDM.commands_functions_dict[command]()
                else:
                    response = random.choice(self.data['commands'][command]['response'])
                continue_ = False if command == 'goodbye' else True
                return self.answer(response, continue_=continue_, continue_target='commands')     # вызов метода ответа с флагом продолжения
        return self.answer("Я вас не понимаю", continue_target='commands')

    def answer_text(self, response,  continue_target='commands', continue_=True,):
        # print(response.title())
        if continue_:   # если любая команда кроме goodbye
            if continue_target == 'commands':  # если слушаем команды
                self.listen_commands()
            else: pass   # если слушаем служебные команды
        self.phrases.append(("Assistant: ", response))
        return self.set_data(self.phrases)

    @FDM.safe_delete_response
    def answer(self, response, continue_target='commands', continue_=True,):
        # setting assistant phrase
        self.phrases.append(("Assistant: ", response))
        self.set_data(self.phrases)
        # audio-answer
        audio_text = gTTS(text=response, lang='ru')
        audio_text.save(self.DATA_DIR + self.RESPONSE_FILE_NAME)
        playsound(self.DATA_DIR + self.RESPONSE_FILE_NAME)
        FDM.delete_response()
        # play()
        # решение о продолжении прослушивания команд
        if continue_:
            if continue_target == 'commands':
                self.listen_commands()
            elif continue_target == 'service':
                return


def validDate(type_: str, phrase, maxQuantityWords: int = 3, maxLength: int = 40):
    """Проверка слов"""
    if phrase is not None:
        if type_ == 'int':
            return validAge(phrase)
        elif type_ == 'str':
            phrase_divided = phrase.split()
            if len(phrase) <= maxLength and len(phrase_divided) <= maxQuantityWords:
                return True
    return False


def validAge(phrase) -> bool:
    """Проверка возраста"""
    if phrase.isdigit():
        if 9 <= int(phrase) <= 100:
            return True
    return False
