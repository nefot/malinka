from rnnoise_wrapper import RNNoise

denoiser = RNNoise(f_name_lib='librnnoise_default.so.0.4.1')

audio = denoiser.read_wav('test.wav')
denoised_audio = denoiser.filter(audio)
denoiser.write_wav('test_denoised.wav', denoised_audio)