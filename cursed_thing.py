import curses
import random
import time

menu = ["Play", "Exit"]

class Player:
    def __init__(self, y_pos, x_pos, char_display):
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.char_display = char_display
    
    # def move_player(self, y, x):
    #     self.y_pos += self.y_pos + y
    #     self.x_pos += self.x_pos + x


class cursed_creature:
    # num_of_creatures = 0
    def __init(self, y_pos, x_pos, char_display):
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.char_display = char_display
        # num_of_creatures += 1


def print_menu(screen, selected_row_index):
    screen.clear()
    height, width = screen.getmaxyx()

    for index, row in enumerate(menu):
        x = width//2 - len(row)//2
        y = height//2 - len(menu)//2 + index
        if index == selected_row_index:
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, row)
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y, x, row)

    screen.refresh()


def move_player(player, key, height, width):
    if key == curses.KEY_UP and player.y_pos > 0:
        player.y_pos -= 1
    elif key == curses.KEY_DOWN and player.y_pos < height:
        player.y_pos += 1
    elif key == curses.KEY_LEFT and player.x_pos > 0:
        player.x_pos -= 1
    elif key == curses.KEY_RIGHT and player.x_pos < width:
        player.x_pos += 1


def play_game(screen, height, width):
    player1 = Player(height//2, width//2, '@')

    while True:
        screen.clear()

        screen.addstr(player1.y_pos, player1.x_pos, player1.char_display)

        screen.refresh()
        
        key = screen.getch()
        if key == ord("q"):
            return
        move_player(player1, key, height, width)


def main(screen):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_index = 0
    height, width = screen.getmaxyx()

    print_menu(screen, current_row_index)

    while 1:
        key = screen.getch()
        screen.clear()

        if key == curses.KEY_UP and current_row_index > 0:
            current_row_index -= 1
        elif key == curses.KEY_DOWN and current_row_index < len(menu) - 1:
            current_row_index += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_index == len(menu) - 1:
                screen.addstr(height//2, width//2 - len("goodbye")//2, "GOODBYE")
                screen.refresh()
                time.sleep(1)
                return
            elif current_row_index == 0:
                play_game(screen, height, width)
            
        print_menu(screen, current_row_index)
        screen.refresh()



curses.wrapper(main)