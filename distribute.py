from redis import Redis
from rq import Queue

from transcribe import transcribe_audio_safe
def distribute_chunks(chunk_names):
    q = Queue(connection=Redis())
    for i in chunk_names:
        result = q.enqueue(transcribe_audio_safe, i)

       