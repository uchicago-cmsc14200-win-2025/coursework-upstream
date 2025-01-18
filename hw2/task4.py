'''
This module runs a simple GUI with buttons coded from scratch.
'''

import sys
import pygame

def debug(msg: str) -> None:
    '''Print message to stderr.
    '''
    print(msg,file=sys.stderr)

class Button:
    '''Clickable button.
    '''
    upper_left_x : int
    upper_left_y : int
    width : int
    height : int
    label : str

    def __init__(self, label: str, upper_left: tuple[int,int], w: int, h: int):
        self.upper_left_x = upper_left[0]
        self.upper_left_y = upper_left[1]
        self.width = w
        self.height = h
        self.label = label

    def contains(self, x: int, y: int) -> bool:
        '''Test if the button contains the location, boundary included.

        Args:
            x: x-coordinate
            y: y-coordinate
        Returns:
            result of test
        '''
        # TODO
        # test if the given (x,y) coordinate is contained inside the rectangle
        # note that being on the boundary *does* count as being contained
        raise NotImplementedError('Button.contains')

    def draw(self, window: pygame.surface.Surface) -> None:
        '''Draw button on window, including its label text.

        Args:
            window: the pygame window to draw on
        '''
        # TODO
        # draw a rectangular frame (and optional fill) onto window
        # create an image of the text for the label (see instructions)
        # blit the text image inside the aforementioned rectangle
        raise NotImplementedError('Button.draw')

class Application:
    '''GUI with buttons and movable gargoyle.
    '''
    window: pygame.surface.Surface
    width: int
    height: int
    buttons: list[Button]
    gargoyle : pygame.surface.Surface
    gargoyle_x : int
    gargoyle_y : int
    clock: pygame.time.Clock

    def __init__(self, width: int, height: int, buttons: list[Button]):
        self.width = width
        self.height = height
        self.buttons = buttons
        self.gargoyle = pygame.image.load('assets/garg.jpg')
        self.gargoyle_x = 200
        self.gargoyle_y = 200

    def run(self) -> None:
        '''Run the application. Typically called once at the top level.
        '''
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('HW2.Task4')
        self.window = pygame.display.set_mode((self.width,self.height))
        self.clock = pygame.time.Clock()
        self.draw()
        self.run_event_loop()

    def quit(self) -> None:
        '''Quit the application.
        '''
        pygame.quit()
        sys.exit(0)

    def draw(self) -> None:
        '''Draw the gargoyle and the buttons.
        '''
        # TODO
        # fill the window, blit the gargoyle, draw the buttons
        # this should be the last line of the draw method:
        pygame.display.update()

    def run_event_loop(self) -> None:
        '''React to clicks.
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    (px, py) = event.pos
                    debug(f'clicked window {px} {py}')
                    # TODO
                    # determine which, if any, button was clicked
                    # perform an action based on the button's label
                    # be sure to call self.draw() last to reflect changes

if __name__ == "__main__":
    # TODO
    # define the buttons
    # bt_up = ...
    # bt_down = ...
    # bt_left = ...
    # bt_right = ...
    # bt_quit = ...
    # bts = [bt_up,bt_down,bt_left,bt_right,bt_quit]
    # app = Application(800,600,bts)
    # app.run()
    pass # remove this "pass" when done
