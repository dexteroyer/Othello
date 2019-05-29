
import pygame
import sys
from pygame.locals import *
import time
from config import BLACK, WHITE, DEFAULT_LEVEL, HUMAN, COMPUTER, RANDOM
import os


class Gui:
    def __init__(self):
        """ Initializes graphics. """

        pygame.init()

        # Colors
        bg = pygame.image.load('res/bg.png')

        self.BLACK = (0, 0, 0)
        self.BACKGROUND = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (128, 128, 0)

        # Display
        self.SCREEN_SIZE = (640, 480)
        self.BOARD_POS = (100, 20)
        self.BOARD = (120, 40)
        self.BOARD_SIZE = 400
        self.SQUARE_SIZE = 50
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)

        # Messages
        self.BLACK_LAB_POS = (5, self.SCREEN_SIZE[1] / 4)
        self.WHITE_LAB_POS = (560, self.SCREEN_SIZE[1] / 4)
        self.font = pygame.font.SysFont("Times New Roman", 22)
        self.scoreFont = pygame.font.SysFont("Serif", 58)

        # Image files
        self.board_img = pygame.image.load(os.path.join(
            "res", "board.bmp")).convert()
        self.black_img = pygame.image.load(os.path.join(
            "res", "police.png")).convert()
        self.white_img = pygame.image.load(os.path.join(
            "res", "drkside.png")).convert()
        self.tip_img = pygame.image.load(os.path.join("res",
                                                      "tip.bmp")).convert()
        self.clear_img = pygame.image.load(os.path.join("res",
                                                        "nada.bmp")).convert()

    def show_options(self):
        """ Shows game options screen and returns chosen options
        """
        # Default values
        player1 = HUMAN
        player2 = COMPUTER
        level = DEFAULT_LEVEL

        while True:

            bg = pygame.image.load('res/bg.png')

            title = pygame.image.load('res/title.png')
            title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=100)

            start_txt = pygame.image.load('res/start.png')
            start_txt = pygame.transform.scale(start_txt, (100, 50))
            start_pos = start_txt.get_rect(centerx=self.screen.get_width() / 2, centery=220)

            player1_txt = pygame.image.load('res/player 1.png')
            player1_txt = pygame.transform.scale(player1_txt, (100, 50))
            player1_pos = player1_txt.get_rect(centerx=self.screen.get_width() / 2, centery=280)

            player2_txt = pygame.image.load('res/player 2.png')
            player2_txt = pygame.transform.scale(player2_txt, (100, 50))
            player2_pos = player2_txt.get_rect(centerx=self.screen.get_width() / 2, centery=340)

            level_txt = pygame.image.load('res/computer level.png')
            level_txt = pygame.transform.scale(level_txt, (150, 50))
            level_pos = level_txt.get_rect(centerx=self.screen.get_width() / 2, centery=400)

            human_txt = self.font.render("Human", True, self.WHITE)
            comp_txt = self.font.render("Computer", True, self.WHITE)

            self.screen.blit(bg, [0,0])
            self.screen.blit(title, title_pos)
            self.screen.blit(start_txt, start_pos)
            self.screen.blit(player1_txt, player1_pos)
            self.screen.blit(player2_txt, player2_pos)
            self.screen.blit(level_txt, level_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if start_pos.collidepoint(mouse_x, mouse_y):
                        return (player1, player2, level)
                    elif player1_pos.collidepoint(mouse_x, mouse_y):
                        player1 = self.get_chosen_player()
                    elif player2_pos.collidepoint(mouse_x, mouse_y):
                        player2 = self.get_chosen_player()
                    elif level_pos.collidepoint(mouse_x, mouse_y):
                        level = self.get_chosen_level()

            pygame.display.flip()
            # desafoga a cpu

    def show_winner(self, player_color):
        self.screen.fill(pygame.Color(0, 0, 0, 50))
        font = pygame.font.SysFont("Courier New", 34)
        if player_color == WHITE:
            msg = font.render("White player wins", True, self.WHITE)
        elif player_color == BLACK:
            msg = font.render("Black player wins", True, self.WHITE)
        else:
            msg = font.render("Tie !", True, self.WHITE)
        self.screen.blit(
            msg, msg.get_rect(
                centerx=self.screen.get_width() / 2, centery=120))
        pygame.display.flip()

    def get_chosen_player(self):
        """ Asks for a player
        """
        while True:
            bg = pygame.image.load('res/bg.png')

            human_txt = pygame.image.load('res/human.png')
            human_txt = pygame.transform.scale(human_txt, (150, 50))
            human_pos = human_txt.get_rect(centerx=self.screen.get_width() / 2, centery=220)

            comp_txt = pygame.image.load('res/computer.png')
            comp_txt = pygame.transform.scale(comp_txt, (150, 50))
            comp_pos = comp_txt.get_rect(centerx=self.screen.get_width() / 2, centery=280)

            random_txt = pygame.image.load('res/random.png')
            random_txt = pygame.transform.scale(random_txt, (150, 50))
            random_pos = random_txt.get_rect(centerx=self.screen.get_width() / 2, centery=340)

            self.screen.blit(bg, [0,0])

            self.screen.blit(human_txt, human_pos)
            self.screen.blit(comp_txt, comp_pos)
            self.screen.blit(random_txt, random_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if human_pos.collidepoint(mouse_x, mouse_y):
                        return HUMAN
                    elif comp_pos.collidepoint(mouse_x, mouse_y):
                        return COMPUTER
                    elif random_pos.collidepoint(mouse_x, mouse_y):
                        return RANDOM

            pygame.display.flip()

    def get_chosen_level(self):
        """ Level options
        """

        while True:
            bg = pygame.image.load('res/bg.png')
            title_fnt = pygame.font.SysFont("Times New Roman", 34)

            title = pygame.image.load('res/select lvl.png')
            title_pos = title.get_rect(centerx=self.screen.get_width() / 2, centery=60)

            one_txt = pygame.image.load('res/lvl 1.png')
            one_txt = pygame.transform.scale(one_txt, (150, 50))
            one_pos = one_txt.get_rect(centerx=self.screen.get_width() / 2, centery=220)

            two_txt = pygame.image.load('res/lvl 2.png')
            two_txt = pygame.transform.scale(two_txt, (150, 50))
            two_pos = two_txt.get_rect(centerx=self.screen.get_width() / 2, centery=280)

            three_txt = pygame.image.load('res/lvl 3.png')
            three_txt = pygame.transform.scale(three_txt, (150, 50))
            three_pos = three_txt.get_rect(centerx=self.screen.get_width() / 2, centery=340)

            self.screen.blit(bg, [0,0])
            self.screen.blit(title, title_pos)
            self.screen.blit(one_txt, one_pos)
            self.screen.blit(two_txt, two_pos)
            self.screen.blit(three_txt, three_pos)

            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
                    if one_pos.collidepoint(mouse_x, mouse_y):
                        return 1
                    elif two_pos.collidepoint(mouse_x, mouse_y):
                        return 2
                    elif three_pos.collidepoint(mouse_x, mouse_y):
                        return 3

            pygame.display.flip()
            # desafoga a cpu
            time.sleep(.05)

    def show_game(self):
        """ Game screen. """

        # draws initial screen
        self.background = pygame.Surface(self.screen.get_size()).convert()
        # self.background.fill(self.BACKGROUND)
        bg = pygame.image.load('res/bg.png')
        self.score_size = 50
        self.score1 = pygame.Surface((self.score_size, self.score_size))
        self.score2 = pygame.Surface((self.score_size, self.score_size))
        self.screen.blit(bg, [0, 0], self.background.get_rect())
        self.screen.blit(self.board_img, self.BOARD_POS,
                         self.board_img.get_rect())
        self.put_stone((3, 3), WHITE)
        self.put_stone((4, 4), WHITE)
        self.put_stone((3, 4), BLACK)
        self.put_stone((4, 3), BLACK)

        pygame.display.flip()

    def put_stone(self, pos, color):
        """ This draws piece with given position and color. """
        if pos == None:
            return

        # Flip orientation - because xy screen orientation
        pos = (pos[1], pos[0])

        if color == BLACK:
            img = self.black_img
        elif color == WHITE:
            img = self.white_img
        else:
            img = self.tip_img

        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]

        self.screen.blit(img, (x, y), img.get_rect())
        pygame.display.flip()

    def clear_square(self, pos):
        """ Puts in the given position a background image, to simulate that the
        piece was removed.
        """
        # Flip orientation
        pos = (pos[1], pos[0])

        x = pos[0] * self.SQUARE_SIZE + self.BOARD[0]
        y = pos[1] * self.SQUARE_SIZE + self.BOARD[1]
        self.screen.blit(self.clear_img, (x, y), self.clear_img.get_rect())
        pygame.display.flip()

    def get_mouse_input(self):
        """ Get place clicked by mouse
        """
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    (mouse_x, mouse_y) = pygame.mouse.get_pos()

                    # The click was out of board, ignores
                    if mouse_x > self.BOARD_SIZE + self.BOARD[0] or \
                       mouse_x < self.BOARD[0] or \
                       mouse_y > self.BOARD_SIZE + self.BOARD[1] or \
                       mouse_y < self.BOARD[1]:
                        continue

                    # Find place
                    position = ((mouse_x - self.BOARD[0]) // self.SQUARE_SIZE), \
                               ((mouse_y - self.BOARD[1]) // self.SQUARE_SIZE)
                    # Fip orientation
                    position = (position[1], position[0])
                    return position

                elif event.type == QUIT:
                    sys.exit(0)

            time.sleep(.05)

    def update(self, board, blacks, whites, current_player_color):
        """Updates screen
        """
        for i in range(8):
            for j in range(8):
                if board[i][j] != 0:
                    self.put_stone((i, j), board[i][j])

        blacks_str = '%02d ' % int(blacks)
        whites_str = '%02d ' % int(whites)
        self.showScore(blacks_str, whites_str, current_player_color)
        pygame.display.flip()

    def showScore(self, blackStr, whiteStr, current_player_color):
        black_background = self.YELLOW if current_player_color == WHITE else self.BACKGROUND
        white_background = self.YELLOW if current_player_color == BLACK else self.BACKGROUND
        text = self.scoreFont.render(blackStr, True, self.BLACK,
                                     black_background)
        text2 = self.scoreFont.render(whiteStr, True, self.WHITE,
                                      white_background)
        self.screen.blit(text,
                         (self.BLACK_LAB_POS[0], self.BLACK_LAB_POS[1] + 40))
        self.screen.blit(text2,
                         (self.WHITE_LAB_POS[0], self.WHITE_LAB_POS[1] + 40))

    def wait_quit(self):
        # Waiting for the user to close the window.
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == KEYDOWN:
                break
