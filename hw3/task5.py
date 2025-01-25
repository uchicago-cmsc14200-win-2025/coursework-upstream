'''
This module implements a GUI to depict complete graphs of varying sizes.
'''

import math
import sys
import pygame

def debug(msg: str) -> None:
    '''Print message to stderr.
    '''
    print(msg,file=sys.stderr)

class Application:
    '''GUI to display K_n (complete graph with n vertices).
    '''
    window: pygame.surface.Surface
    clock: pygame.time.Clock
    n: int

    def __init__(self) -> None:
        self.n = 2

    def run(self) -> None:
        '''Run the application. Intended to be called once at the top level.
        '''
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Complete Graphs')
        # NOTE: change the window size as you see fit
        self.window = pygame.display.set_mode((480,480))
        self.clock = pygame.time.Clock()
        self.draw()
        self.run_event_loop()

    def quit(self) -> None:
        '''Quit the application.
        '''
        pygame.quit()
        sys.exit(0)

    def draw(self) -> None:
        '''Draw K_n.
        '''
        # TODO draw K_n
        pygame.display.update()

    def run_event_loop(self) -> None:
        '''React to keystrokes: up, down, and q.
        '''
        # TODO implement the event loop

if __name__ == "__main__":
    app = Application()
    app.run()
