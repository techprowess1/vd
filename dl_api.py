import random

from fastapi import FastAPI
import dl_script

app = FastAPI()


@app.get('/downloader')
async def downloader(url: str):
    download_inst = dl_script.Downloader(url)
    download_options = [download_inst.saveFromNet]

    if 'facebook' in url or 'instagram' in url:
        download_options.append(download_inst.snapSave)
    elif 'tiktok' in url:
        download_options.extend([download_inst.saveTikCo, download_inst.tiktokDownloadOnline, download_inst.snapSave])
    elif 'pinterest' in url:
        download_options.append(download_inst.pinterestDownloader)
    elif 'twitter' in url:
        pass

    final_choice = random.choice(download_options)
    return final_choice()
