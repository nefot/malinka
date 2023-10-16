## Натройки SpeechKit Recognition API v3
прежде чем синтезировать речь необходимо отправить настройки распознавания

отправка настроек на сервер производится командой 
```python 
yield stt_pb2.StreamingRequest(session_options=<Настройки речи>)
```
Настройки речи миеют следущую структуру:

StreamingRequest
- session_options = StreamingOptions
- 
- chunk = AudioChunk
- silence_chunk = SilenceChunk
- eou = Eou