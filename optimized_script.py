import requests
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from typing import AnyStr
from flask import Flask, request

app = Flask(__name__)

# -------------------------------- SETTING --------------------------------

setting = dict(
    speed='1.1',
    delay=500,
    api_code="AQVNyUzOGjKeZLACdq8b96ibAT1WnAUPcRpx5jbX",
    voice='ermil',
    emotion='good'
)


# -------------------------------- GET --------------------------------

@app.route('/get_text', methods=['GET'])
def get_text():
    text = request.args.get('text')
    return text


# -------------------------------- SEND --------------------------------

def send_request_to_server(text: str, speed: float, delay: int, api_code: str, voice: str, emotion: str):
    """
    @param emotion: эмоция с которой происходит озвучивание
    @param voice: голос озвучиваема
    @param text: Текст для озвучивания
    @param api_code: код для авторизации
    @param delay: время ожидания после конца фразы
    @type speed: скорость речи
    """
    server_url = 'http://127.0.0.1/api'

    params = {
        'text': text,
        'speed': speed,
        'delay': delay,
        'api-code': api_code,
        'voice': voice,
        'emotion': emotion
    }

    try:
        response = requests.get(server_url, params=params)
        if response.status_code == 200:
            return response.text
        return 'Ошибка при запросе на сервер'

    except requests.exceptions.RequestException as e:
        return str(e)


# -------------------------------- assistant --------------------------------

def assistant(question: AnyStr):
    question = question.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    stemmer = SnowballStemmer("russian")
    question = tokenizer.tokenize(question)

    word_array = [stemmer.stem(word).lower() if word != "рост" else "ростов" for word in question]

    hello_keywords = ['кон', "привет", "здравств"]
    goodbye_keywords = ['пок', "проща", "забуд"]

    response = ''

    if any(hello_word in word_array for hello_word in hello_keywords):
        response += ("Здравствуйте! Я конь Василий, ваш гид по достопримечательностям Ростовской области. sil<[500]>. "
                     "Задайте мне"
                     "вопросы об интересующей вас достопримечательности, и, если я знаю о ней, то поведаю вам! sil<["
                     "500]> Для"
                     "завершения разговора скажите пока")
        return response

    if any(goodbye_keyword in word_array for goodbye_keyword in goodbye_keywords):
        response += "До свидания, рад был помочь!"
        return response

    keywords_to_responses = {
        'достопримечательность 1': "Вот некоторые из достопримечательностей Ростовской Области...",
        'достопримечательность 2': 'Древний город основанный греками выходцами из Боспорского царства...',
        'достопримечательность 3': 'Это великий храм, открывшийся в тысяча девятьсот пятом году...',
        'достопримечательность 4': 'Это великий храм, открывшийся в тысяча девятьсот пятом году...',
        'достопримечательность 5': 'Год открытия этого мемориала – тысяча девятьсот семьдесят седьмой год...',
        'достопримечательность 6': 'Год открытия этого мемориала – тысяча девятьсот семьдесят седьмой год...',
        'достопримечательность 7': 'Год основания этого музея – тысяча девятьсот семьдесят пятый год...',
        'достопримечательность 8': 'Главные крепостные ворота Азова постройки семнадцатого века...',
        'достопримечательность 9': 'Год основания – тысяча восемьсот восемьдесят шестой...'
    }

    for keyword, response_text in keywords_to_responses.items():
        if keyword in word_array:
            response += response_text
            break

    if not response:
        response = ("К сожалению, я не могу ответить на ваш вопрос. Или я вас не так понял, или вы спрашиваете меня о "
                    "том, о чем я не знаю, не могли бы вы повторить вопрос, если он относится к теме "
                    "достопримечательностей Ростовской области")

    return response


if __name__ == '__main__':
    app.run(debug=True)
    print(send_request_to_server(text=assistant(get_text()), **setting))
