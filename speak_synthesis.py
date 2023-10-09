from speechkit import Session, SpeechSynthesis
import setting
import pyaudio

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

    def randomize_pith(self):
        pass
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
        self.audio_data = synthesizeAudio.synthesize_stream(**setting.datas, text=text)
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
