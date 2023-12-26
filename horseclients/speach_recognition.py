import grpc
import pyaudio
import setting
import yandex.cloud.ai.stt.v3.stt_pb2 as stt_pb2
import yandex.cloud.ai.stt.v3.stt_service_pb2_grpc as stt_service_pb2_grpc
from setting import *


class Recognition:
    FORMAT = pyaudio.paInt16
    audio = pyaudio.PyAudio()
    default_classifier_type = "HIGH"

    def __init__(self, api: str):
        self.audio = pyaudio.PyAudio()
        self.api = api
        self.recognize_options = self.recognize_option()

    def recognize_option(self):
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
                    profanity_filter=True,
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
                    type=self.default_classifier_type
                )

            )
        )

        return recognize_options

    @staticmethod
    def connection_server() -> object:

        cred = grpc.ssl_channel_credentials()
        channel = grpc.secure_channel('stt.api.cloud.yandex.net:443', cred)
        stub = stt_service_pb2_grpc.RecognizerStub(channel)
        print('conected')
        print(type(stub))
        return stub

    def gen(self):
        yield stt_pb2.StreamingRequest(session_options=self.recognize_option())
        stream = self.audio.open(format=self.FORMAT, channels=1,
                                 rate=RATE, input=True,
                                 frames_per_buffer=CHUNK)


        frames = []
        self.connection_server()
        while True:
            data = stream.read(CHUNK)
            yield stt_pb2.StreamingRequest(chunk=stt_pb2.AudioChunk(data=data))
            frames.append(data)

    def conected(self):
        stub = self.connection_server()

    def run(self):
        self.conected()
        stub = self.connection_server()
        it = stub.RecognizeStreaming(self.gen(), metadata=(
            ('authorization', f'Api-Key {self.api}'),
        ))
        print(it)
        try:
            for r in it:
                event_type, alternatives = r.WhichOneof('Event'), None
                if event_type == 'partial' and len(r.partial.alternatives) > 0:
                    alternatives = [a.text for a in r.partial.alternatives]
                if event_type == 'final':
                    alternatives = [a.text for a in r.final.alternatives]
                    return alternatives
                if event_type == 'final_refinement':
                    alternatives = [a.text for a in r.final_refinement.normalized_text.alternatives]


        except grpc._channel._Rendezvous as err:
            raise err


if __name__ == '__main__':
    test = Recognition(setting.API)
    text = test.run()[0]
    print("\033[34m {}".format(text))
