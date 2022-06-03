import pygame
import pygame.mixer

# Initizalizes pygame's modules
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
"""Sound é uma classe de controle dos sons do jogo - efeitos, música"""
class Sound():
    """ATENÇÃO! O arquivo passado deve ser .OGG!!! Se não pode gerar problemas."""
    def __init__(self, sound_file):
        self.loop = False
        self.sound_file = sound_file
        self.volume = 50
        self.load(sound_file)
        self.set_volume(self.volume)

    def load(self, sound_file):
        if(pygame.mixer):
            pygame.mixer.music.load(sound_file)

    """Value deve ser um valor entre 0 e 100"""
    def set_volume(self, value):
        if(value >= 100):
            value = 100
        if(value <= 0):
            value = 0

        self.volume = value
        pygame.mixer.music.set_volume(value/100)

    def increase_volume(self, value):
        self.set_volume(self.volume + value)

    def decrease_volume(self, value):
        self.set_volume(self.volume - value)

    def is_playing(self):
        if(pygame.mixer.music.get_busy()):
            return True
        else:
            return False

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def play(self):
        if(self.loop):
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def set_repeat(self, repeat):
        self.loop = repeat

    def fadeout(self, time_ms):
        pygame.mixer.music.fadeout(time)


