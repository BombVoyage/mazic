import pygame
import logging
from Logger import Logger

class Mazic:
    def __init__(self) -> None:
        # Instantiate Logger
        self.logger = Logger(self.__class__.__name__, logging.INFO)

        # Instantiate pygame
        pygame.init()

        # Create the display
        self.screen = pygame.display.set_mode((1200, 1000))
        ## Set window title
        pygame.display.set_caption("Mazic")
        ## Set window icon
        self.icon = pygame.image.load("assets/frames/big_demon_idle_anim_f1.png")
        pygame.display.set_icon(self.icon)

        # Instantiate attributes
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        # Game loop
        while self.running:
            self.clock.tick(60)
            self.events()

    def events(self) -> None:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False