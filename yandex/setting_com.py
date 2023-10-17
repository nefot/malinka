from setting import *
n = f"--- Список настроек ---\
F” <pre>\
<ins> Настройки потокового распознавания. </ins>\
<b>CHANNELS</b> = {CHANNELS}\
<b>RATE</b> = {RATE}\
MAX_PAUSE_BETWEEN_WORDS_HINT_MS = {MAX_PAUSE_BETWEEN_WORDS_HINT_MS},\
TYPE = {TYPE}\
\
<b>CHUNK</b> = {CHUNK}\ 
<b>RECORD_SECONDS</b> = {RECORD_SECONDS}\
<ins> pyaudio_play_audio_function </ins>\
<b>SAMPLE_RATE</b> = {SAMPLE_RATE}\
<b>CHUNK_SIZE</b> = {CHUNK_SIZE}\
<b>NUM_CHANNELS</b> = {NUM_CHANNELS}\
\
<ins> Настройки голоса </ins>\
<b>INVALID_ELEMENTS</b> = {INVALID_ELEMENTS}  \
<b>VOICE</b> = {VOICE}\
<b>EMOTION</b> ={EMOTION}\
<b>SPEED</b> ={SPEED}\
</pre> \"