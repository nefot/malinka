## Натройки SpeechKit Recognition API v3

прежде чем синтезировать речь необходимо отправить настройки распознавания

отправка настроек на сервер производится командой

```python 
yield stt_pb2.StreamingRequest(session_options= < Настройки
речи >)
```

