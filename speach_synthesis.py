import requests.exceptions
import helper
import setting
import pyaudio
import librosa
from speechkit import Session, SpeechSynthesis




def pyaudio_play_audio_function(text,
                                num_channels=setting.num_channels,
                                sample_rate=setting.sample_rate,
                                chunk_size=setting.chunk_size) -> str | None:
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
    try:
        session = Session.from_yandex_passport_oauth_token(setting.oauth_token, setting.catalog_id)
        synthesize_audio = SpeechSynthesis(session)
    except requests.exceptions.ConnectionError:
        helper.debug("Подключение нестабильно")
        return ''

    if text in setting.invalid_elements:
        return
    # try:
    print(text, "text")

    audio_data = synthesize_audio.synthesize_stream(**setting.datas, text=text)

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
        for i in range(0, len(audio_data), chunk_size):
            stream.write(audio_data[i:i + chunk_size])
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == '__main__':
    pyaudio_play_audio_function('sil<[300]> **Удобные** интерфейсы для решения задач.')
