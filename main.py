from myinstants import download_media
from myinstants import fetch_link
import play_audio
import keyboard

while True:
    keyboard.wait('pagedown')
    record = keyboard.record('pagedown')
    recorded_strings = ""
    for event in record:
        if event.event_type == keyboard.KEY_DOWN and not event.name == 'page down':  # You can choose to only record key down events
            recorded_strings += (event.name)
    link = fetch_link.getLink(str(recorded_strings), 1)
    if not link == '':
        download_media.downloadMedia(link, 'ias.mp3')
        play_audio.play_audio('ias.mp3')



