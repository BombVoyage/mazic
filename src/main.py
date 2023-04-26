import pygame

class Mazic:
    
    def __init__(self) -> None:
        # Instantiate pygame
        pygame.init()
        
        # Create the display
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Mazic")
        
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
                
if __name__ == "__main__":
    # Run the game
    Mazic().run() 