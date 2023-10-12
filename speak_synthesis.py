import speechkit.exceptions
from speechkit import Session, SpeechSynthesis
import setting
import pyaudio
import struct
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import librosa

try:
    session = Session.from_yandex_passport_oauth_token(setting.oauth_token, setting.catalog_id)
except Exception as e:
    print("токен инвалид: ", e)

synthesizeAudio = SpeechSynthesis(session)


class TextToSpeak:

    def __init__(self):
        self.audio_data = None
        self.data = setting.datas

    def synthesis(self):
        pass

    def pith_apply(self):
        pass

    # @staticmethod
    # def byte_to_float(data):
    #     print(data)
    #     # data_bytes = np.array(data, dtype=np.uint8)
    #     data_as_float = data_bytes.view(dtype=np.float32)
    #     print(data_as_float)

    def randomize_pith(self):
        pass

    def visualisation(self, audio):
        x_1, fs = librosa.load('audio/sir_duke_slow.ogg')
        # And a second version, slightly faster.
        x_2, fs = librosa.load('audio/sir_duke_fast.ogg')

        fig, ax = plt.subplots(nrows=2, sharex=True, sharey=True)
        librosa.display.waveshow(x_1, sr=fs, ax=ax[0])
        ax[0].set(title='Slower Version $X_1$')
        ax[0].label_outer()

        librosa.display.waveshow(x_2, sr=fs, ax=ax[1])
        ax[1].set(title='Faster Version $X_2$')

    def pyaudio_play_audio_function(self, text, num_channels=1, sample_rate=setting.sample_rate,
                                    chunk_size=4000) -> None:
        """
        Воспроизводит бинарный объект с аудио данными в формате lpcm (WAV)
        :param text: Текст, который подается для озвучивания
        :param integer num_channels: количество каналов, спич кит генерирует
            моно дорожку, поэтому стоит оставить значение `1`
        :param integer sample_rate: частота дискретизации, такая же
            какую вы указали в параметре sampleRateHertz
        :param integer chunk_size: размер семпла воспроизведения,
            можно отрегулировать если появится потрескивание
        """

        if text == '' or text == ' ':
            return
        # try:
        print(text, "text")

        self.audio_data = synthesizeAudio.synthesize_stream(**setting.datas, text=text)

        # except speechkit.exceptions.RequestError:

        p = pyaudio.PyAudio()

        stream = p.open(
            format=pyaudio.paInt16,
            channels=num_channels,
            rate=sample_rate,
            output=True,
            frames_per_buffer=chunk_size
        )

        try:
            for i in range(0, len(self.audio_data), chunk_size):
                stream.write(self.audio_data[i:i + chunk_size])
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()


if __name__ == '__main__':
    a = TextToSpeak()
    a.pyaudio_play_audio_function("Убейте меня")
