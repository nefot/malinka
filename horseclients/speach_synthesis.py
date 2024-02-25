import io

import grpc
import pyaudio

import yandex.cloud.ai.tts.v3.tts_pb2 as tts_pb2
import yandex.cloud.ai.tts.v3.tts_service_pb2_grpc as tts_service_pb2_grpc
from horseclients.setting import YANDEX_API_KEY


class SpeachGeneration:
    def __init__(self, api: str):
        self.api = api
        self.stub = tts_service_pb2_grpc.SynthesizerStub(
            grpc.secure_channel('tts.api.cloud.yandex.net:443', grpc.ssl_channel_credentials()))
        self.chunkSize = 1000

    def play_audio(self, audio: bytes) -> bytes:
        stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            output=True,
            frames_per_buffer=self.chunkSize
        )
        try:
            for i in range(0, len(audio), self.chunkSize):
                stream.write(audio[i:i + self.chunkSize])

        finally:
            stream.stop_stream()
            stream.close()
            pyaudio.PyAudio().terminate()
        return audio

    def synthesize(self, text: str):

        request = tts_pb2.UtteranceSynthesisRequest(
            text=text,
            output_audio_spec=tts_pb2.AudioFormatOptions(
                container_audio=tts_pb2.ContainerAudio(
                    container_audio_type=tts_pb2.ContainerAudio.WAV
                ),
                raw_audio = tts_pb2.RawAudio(
                    sample_rate_hertz=16000
                )
            ),
            loudness_normalization_type=tts_pb2.UtteranceSynthesisRequest.LUFS,
            hints=[tts_pb2.Hints(voice="zahar"), tts_pb2.Hints(speed=0.9), tts_pb2.Hints(volume=0),
                   tts_pb2.Hints(pitch_shift=270)],

        )

        it = self.stub.UtteranceSynthesis(request, metadata=(('authorization', f'Api-Key {self.api}'),))

        try:
            audio = io.BytesIO()
            for response in it:
                audio.write(response.audio_chunk.data)
            audio.seek(0)

            self.play_audio(audio.read())
        except grpc._channel._Rendezvous as err:
            print(f'Error code {err._state.code}, message: {err._state.details}')
            raise err


if __name__ == '__main__':
    print(YANDEX_API_KEY)
    SP = SpeachGeneration(YANDEX_API_KEY)
    print(SP.synthesize('привет API 3'))
