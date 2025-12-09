import winsound

class Sounds:
    def sound_track(self, sound):
        winsound.PlaySound(f"{sound}", winsound.SND_FILENAME | winsound.SND_ASYNC)
