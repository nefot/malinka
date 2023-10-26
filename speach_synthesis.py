import librosa
import requests.exceptions
import pyaudio
from speechkit import Session, SpeechSynthesis

import numpy as np
import matplotlib.pyplot as plt

from loger import logger
from setting import (
    OAUTH_TOKEN, CATALOG_ID,
    NUM_CHANNELS, SAMPLE_RATE, CHUNK_SIZE,
    INVALID_ELEMENTS, SPEAK_SETTING, CHUNK
)


class SoundProcessor:
    def __init__(self):
        self.logger = logger
        self.authenticate()

    def authenticate(self):
        try:
            self.logger.debug("Аутентификация")
            session = Session.from_yandex_passport_oauth_token(OAUTH_TOKEN, CATALOG_ID)
            self.synthesize_audio = SpeechSynthesis(session)
        except requests.exceptions.ConnectionError:
            self.logger.debug("Нестабильное подключение")
            return False
        return True

    def process_and_play_audio(self, text):
        if text in INVALID_ELEMENTS:
            return

        audio_data = self.synthesize_audio.synthesize_stream(**SPEAK_SETTING, text=text)

        self.logger.debug(f"Озвучил: {text}")

        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paInt16,
            channels=NUM_CHANNELS,
            rate=SAMPLE_RATE,
            output=True,
            frames_per_buffer=CHUNK_SIZE
        )

        try:
            for i in range(0, len(audio_data), CHUNK_SIZE):
                stream.write(audio_data[i:i + CHUNK_SIZE])

        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()
        return audio_data

    def visualize_audio(self, audio_signal):
        plt.plot(np.arange(0, len(audio_signal)), audio_signal)
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.title('Audio Signal')
        plt.show()

    def harmonic_analysis_resynthesis(self, audio_data, num_harmonics=10):
        """
        Гармонический анализ и ресинтез аудио.
        """
        # Производим гармонический анализ: вычисляем амплитуду и фазу для каждой гармоники
        spectrum = np.fft.fft(audio_data)
        amplitudes = np.abs(spectrum)[:num_harmonics]
        phases = np.angle(spectrum)[:num_harmonics]
        resynthesized_spectrum = np.zeros_like(spectrum)
        for i in range(num_harmonics):
            resynthesized_spectrum[i] = amplitudes[i] * np.exp(1j * phases[i])
        resynthesized_audio = np.fft.ifft(resynthesized_spectrum)

        return np.real(resynthesized_audio)


# Пример использования
if __name__ == "__main__":
    sound_processor = SoundProcessor()
    if sound_processor.authenticate():
        text = ("Цисгендерный, гетеросексуальный мужчина априори свинья, поработитель и угнетатель.Даже при том, "
                "что ты безработная хикка, живущая в подвале у родителей. Для тебя это легко, потому что этот мир был "
                "построен агрессивными тестостероновыми хуемразями, для таких же агрессивных тестостероновых "
                "хуемразей. Ненавижу тебя. Хех очередной завод по производству спермы. Когда вы уже блять все "
                "переведётесь? Бесполезный блядословник-унтерменш, у которого на ебарезине написано, "
                "что он генетический придурок, который, сука, тупее чем чехол от телефона, и у которого есть лишь "
                "один лучший друг лучший друг - темнота, потому что она скрывает его кривое ебало. Знаешь, "
                "конечно не хорошо так говорить, но когда патриархат умрёт, это одна из рож, которая будет висеть на "
                "его надробии Очередное гендерное недоразумение. Чего тебе надо, пораждение патриархата? мммм? Того "
                "же чего и всем остальным хуястым, скорее всего. Ты этого не получишь. Небось гордишься тем, "
                "что ты мужчина и тем, что природа тебе дала возможность ссать стоя? Пол - это всего лишь социальный "
                "конструкт. Типа ты дофига весь такой рациональный, ведь у тебя нет месячных. Оставь свои кухонные "
                "рассуждения о патриархате кому нибудь другому, ок. Я хочу видеть тебя избитым в кровавое месиво, "
                "с каблуком, забитым тебе в рот, подобно яблоку в пасти у свиньи, мерзкое хуястое существо. Назвать "
                "тебя животным — значить льстить тебе ты — всего лишь машина, ходячий спермобак с вибратором. Хотя "
                "той же справедливости ради стоит заметить, что у мужика выше вероятность забухать. Особенно у такого "
                "как ты. Ты далёк от нормального члена общества так же, как неандерталец от кроманьонца. "
                "Патриархальный гиббон, ущемляющий права и свободы амазонок. Хуеблядский Спермоносец имени Первого "
                "Подзалупного Пиздострадального фронта. Мужчины мусор, даже маленькие. Сделаем человечество вновь "
                "эстетичным! Давайте же сотрём дешёвок в порошок. какая мерзость, господи блядь. будь мужиком и "
                "выпили себя ножом. низкотестостероновое агрессивное говно. ущемлённый несчастный кунчик. мужчина - "
                "спермоколонка. Ах ты хуемразь. Только и думаешь, чтобы изнасиловать независимую девушку!!! Отправь "
                "сюда фото с людьми, на этой фотографии я их не вижу. Озабоченный патриархальный угнетатель с "
                "отростком между ног. Злоебучие спермобаки, какого хуя я тут за вас одна отдуваюсь?")
        audio = sound_processor.process_and_play_audio(text)
        audio = np.frombuffer(audio, dtype=np.int16)
        shifted_audio_data = sound_processor.harmonic_analysis_resynthesis(audio, 55)
        print(type(audio))
        # Создаем пример аудио сигнала для визуализации (заглушка)
        audio_signal = np.sin(2 * np.pi * np.linspace(0, 1, SAMPLE_RATE))
        print(type(audio_signal))
        sound_processor.visualize_audio(audio)
        sound_processor.visualize_audio(shifted_audio_data)
