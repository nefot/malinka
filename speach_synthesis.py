import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import requests.exceptions
from scipy.io.wavfile import write
from speechkit import Session, SpeechSynthesis



from setting import *
from service import benchmark, Charisma

SPEAK_SETTING = {

    'lang': 'ru-RU',
    'voice': VOICE,  # oksana
    'emotion': EMOTION,
    'speed': SPEED,
    'format': 'lpcm',
    'sampleRateHertz': 16000,
}


class SoundProcessor:
    def __init__(self):
        self.synthesize_audio = None

        self.authenticate()

    @benchmark
    def authenticate(self):
        try:

            session = Session.from_yandex_passport_oauth_token(OAUTH_TOKEN, CATALOG_ID)
            self.synthesize_audio = SpeechSynthesis(session)
        except requests.exceptions.ConnectionError:
            text = 'authenticate error'
            print("\033[31m {}".format(text))
        return True

    @benchmark
    def process(self, text):
        return self.synthesize_audio.synthesize_stream(**SPEAK_SETTING, text=text)


    def process_and_play_audio(self, text):
        if text in INVALID_ELEMENTS:
            return

        audio_data = self.process(text)

        # self.logger.debug(f"Озвучил: {text}")

        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate= 16000,
            output=True,
            frames_per_buffer=CHUNK_SIZE
        )

        try:



            charisma = Charisma(audio_data)
            audio_data = charisma.add_neighing()
            for i in range(0, len(audio_data), CHUNK_SIZE):
                stream.write(audio_data[i:i + CHUNK_SIZE])

        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()
        return audio_data

    def visualize_audio(self, audio_signal):
        plt.plot(np.arange(0, len(audio_signal)), audio_signal)
        plt.xlabel('Время')
        plt.ylabel('миллисекунды')
        plt.title('Аудио сигнал')
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


@benchmark
def save_audio_to_file(audio_data):
    filename = f'ausios.wav'
    waveform_integers = np.int16(audio_data)

    write(filename, int(16000), waveform_integers)

# Пример использования
if __name__ == "__main__":

    sound_processor = SoundProcessor()
    if sound_processor.authenticate():
        SPEED = "1.0"
        text = ('+и-и-и-и-[[g]] о-  [[u g]] о ')
        audio = sound_processor.process_and_play_audio(text)
        audio = np.frombuffer(audio, dtype=np.int16)
        # shifted_audio_data = sound_processor.harmonic_analysis_resynthesis(audio, 55)
        # audio_signal = np.sin(2 * np.pi * np.linspace(0, 1, SAMPLE_RATE))
        # print(type(audio_signal))
        # sound_processor.visualize_audio(audio)
        # sound_processor.visualize_audio(shifted_audio_data)
        # save_audio_to_file(audio)
