from rnnoise_wrapper import RNNoise
from setting import SAMPLE_RATE

denoiser = RNNoise(f_name_lib='librnnoise_default.so.0.4.1')


def reNoise(audio_data: object) -> object:
    return denoiser.filter(audio_data, sample_rate=SAMPLE_RATE)


if __name__ == '__main__':
    denoiser = RNNoise(f_name_lib='librnnoise_default.so.0.4.1')

    audio = denoiser.read_wav('test.wav')
    denoised_audio = denoiser.filter(audio)
    denoiser.write_wav('test_denoised.wav', denoised_audio)
