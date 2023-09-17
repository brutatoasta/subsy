from download import download
from transcribe import save_chunks_on_silence
from distribute import distribute


def main():
    # get link and metadata
    link = "https://www.youtube.com/watch?v=DtncJJR5W50"
    # download
    download_path, txt_file = download(link)
    chunk_names = save_chunks_on_silence(download_path)
    distribute(chunk_names, txt_file)


if __name__ == "__main__":
    main()
