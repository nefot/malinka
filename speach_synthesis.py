import librosa
import requests.exceptions
import pyaudio
from speechkit import Session, SpeechSynthesis
from loger import setup_logging
import numpy as np
import matplotlib.pyplot as plt

logger = setup_logging()
from setting import (
    OAUTH_TOKEN, CATALOG_ID,
    NUM_CHANNELS, SAMPLE_RATE, CHUNK_SIZE,
    INVALID_ELEMENTS, SPEAK_SETTING, CHUNK
)


class SoundProcessor:
    def __init__(self):
        self.logger = setup_logging()
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
        text = "возвращает массив numpy с преобразованными данными. "
        audio = sound_processor.process_and_play_audio(text)
        audio = np.frombuffer(audio, dtype=np.int16)
        shifted_audio_data = sound_processor.harmonic_analysis_resynthesis(audio, 55)
        print(type(audio))
        # Создаем пример аудио сигнала для визуализации (заглушка)
        audio_signal = np.sin(2 * np.pi * np.linspace(0, 1, SAMPLE_RATE))
        print(type(audio_signal))
        sound_processor.visualize_audio(audio)
        sound_processor.visualize_audio(shifted_audio_data)
