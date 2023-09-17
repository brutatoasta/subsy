import time
from collections import OrderedDict
from multiprocessing.pool import ThreadPool
from pathlib import Path

from transcribe import transcribe_audio_safe


def addd(f):
    return f + 1


def distribute(chunk_names, txt_file):
    # multi thread method
    start = time.time()
    chunk_names = [str(x) for x in chunk_names]
    with ThreadPool(20) as p:
        transcribed = p.map(transcribe_audio_safe, chunk_names)

        # clean names to just the line numbers
        numbers = [int(number.split("/chunk")[1][:-4]) for number in chunk_names]
        unsorted = dict(zip(numbers, transcribed))
        final = dict(sorted(unsorted.items()))

        # save numbers : speech to text
        with open(txt_file, mode="a", encoding="utf-8") as f:
            for k, v in final.items():
                f.write(f"{k}: {v}\n")
    print(f"stt time: {time.time() - start}")


if __name__ == "__main__":
    chunk_names = Path("downloads/《新心的起点》第四课：人与自己的关系 I 23-0203/audio-chunks").iterdir()
    txt_file = Path(
        "downloads/《新心的起点》第四课：人与自己的关系 I 23-0203/《新心的起点》第四课：人与自己的关系 I 23-0203.txt"
    )
    distribute(chunk_names, txt_file)
