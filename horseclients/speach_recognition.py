import grpc
import pyaudio
import setting
import yandex.cloud.ai.stt.v3.stt_pb2 as stt_pb2
import yandex.cloud.ai.stt.v3.stt_service_pb2_grpc as stt_service_pb2_grpc
from setting import *
from service import benchmark



FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 1000

WAVE_OUTPUT_FILENAME = "audio.wav"

audio = pyaudio.PyAudio()


class Recognition:
    @classmethod
    def validate(cls, api):
        return api

    def __init__(self, api):
        self.audio = pyaudio.PyAudio()
        self.api = api
        self.recognize_options = self.recognize_option()
        self.stub = self.connection_server()


    @staticmethod
    def recognize_option():

        recognize_options = stt_pb2.StreamingOptions(

            recognition_model=stt_pb2.RecognitionModelOptions(
                audio_format=stt_pb2.AudioFormatOptions(
                    raw_audio=stt_pb2.RawAudio(
                        audio_encoding=stt_pb2.RawAudio.LINEAR16_PCM,
                        sample_rate_hertz=8000,
                        audio_channel_count=1
                    )
                ),
                text_normalization=stt_pb2.TextNormalizationOptions(
                    text_normalization=stt_pb2.TextNormalizationOptions.TEXT_NORMALIZATION_ENABLED,
                    profanity_filter=False,
                    literature_text=False
                ),
                language_restriction=stt_pb2.LanguageRestrictionOptions(
                    restriction_type=stt_pb2.LanguageRestrictionOptions.WHITELIST,
                    language_code=['ru-RU']
                ),
                audio_processing_type=stt_pb2.RecognitionModelOptions.REAL_TIME
            ),
            eou_classifier=stt_pb2.EouClassifierOptions(
                default_classifier=stt_pb2.DefaultEouClassifier(
                    max_pause_between_words_hint_ms=500,
                    type="HIGH"
                )

            )
        )

        return recognize_options

    @staticmethod
    def connection_server():

        cred = grpc.ssl_channel_credentials()
        channel = grpc.secure_channel('stt.api.cloud.yandex.net:443', cred)
        stub = stt_service_pb2_grpc.RecognizerStub(channel)
        print('conected')
        return stub

    def gen(self):
        yield stt_pb2.StreamingRequest(session_options=self.recognize_option())
        stream = self.audio.open(format=FORMAT, channels=1,
                                 rate=RATE, input=True,
                                 frames_per_buffer=CHUNK)


        frames = []
        self.connection_server()
        while True:
            # data = denoiser.filter(stream.read(CHUNK), sample_rate=SAMPLE_RATE)
            yield stt_pb2.StreamingRequest(chunk=stt_pb2.AudioChunk(data=stream.read(CHUNK)))
            frames.append(stream.read(CHUNK))

    @benchmark
    def run(self):

        it = self.stub.RecognizeStreaming(self.gen(), metadata=(
            ('authorization', f'Api-Key {self.api}'),
        ))
        try:
            for r in it:
                event_type, alternatives = r.WhichOneof('Event'), None
                if event_type == 'partial' and len(r.partial.alternatives) > 0:
                    alternatives = [a.text for a in r.partial.alternatives]
                    print(alternatives, 'partical')
                if event_type == 'final':
                    alternatives = [a.text for a in r.final.alternatives]
                    print(alternatives, 'final')

                    return alternatives
                if event_type == 'final_refinement':
                    alternatives = [a.text for a in r.final_refinement.normalized_text.alternatives]


        except grpc._channel._Rendezvous as err:
            raise err


if __name__ == '__main__':
    test = Recognition(setting.API)
    while True:
        text = test.run()[0]
        print("\033[34m {}" .format(text))

