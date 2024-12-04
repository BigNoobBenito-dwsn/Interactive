import arcade
import urllib.request
import enum
from random import choice

def download_image(url, save):
    urllib.request.urlretrieve(url, save)

image_url1 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/compy.png'
save_as = 'compy.jpg'
image_url2 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/srock.png'
save_as1 = 'srock.jpg'
image_url3 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/spaper.png'
save_as2 = 'spaper.jpg'
image_url4 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/scissors.png'
save_as3 = 'scissors.jpg'
image_url5 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/faceBeard.png'
save_as4 = 'faceBeard.jpg'
image_url6 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/scissors-close.png'
save_as5 = 'scissors-close.jpg'
image_url7 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/srock-attack.png'
save_as6 = 'srock-attack.jpg'
image_url8 = 'https://raw.githubusercontent.com/bigNoobBenito/assets/main/assets/spaper-attack.png'
save_as7 = 'spaper-attack.jpg'
download_image(image_url6, save_as5)
download_image(image_url7, save_as6)
download_image(image_url8, save_as7)
download_image(image_url5, save_as4)
download_image(image_url4, save_as3)
download_image(image_url3, save_as2)
download_image(image_url2, save_as1)
download_image(image_url1, save_as)
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "game"

class AttackType(enum.Enum):
    """
    """
    NOT_CHOSEN = 0
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class GameState(enum.Enum):
    NOT_STARTED = 0
    ROUND_ACTIVE = 1
    ROUND_DONE = 2
    GAME_OVER = 3

class AttackAnimation(arcade.Sprite):
    """
    """
    ATTACK_SCALE = 0.50
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type):
        super().__init__()
        self.animation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0.0
        self.attack_type = attack_type
        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("srock.jpg"),
                arcade.load_texture("srock-attack.jpg"),
            ]
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("spaper.jpg"),
                arcade.load_texture("spaper-attack.jpg"),
            ]
        else:
            self.textures = [
                arcade.load_texture("scissors.jpg"),
                arcade.load_texture("scissors-close.jpg"),
            ]

        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)

    def on_update(self, delta_time: float = 1 / 60):
        """
        This method is used to update the animation.
        """
        # Update the animation.
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0


screen_width = 1080
screen_height = 720
screen_title = "Rock Paper Scissors"

class Player(arcade.Sprite):
    """
    Class to create the player
    """
    def __init__(self, image, scale, center_x, center_y):
        super().__init__(image, scale)
        self.center_x = center_x
        self.center_y = center_y
        self.scale = 0.5
        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)
        self.choice = None

    def draw_animation(self):
        """
        Draw the player's attack animation
        """
        self.rock.on_update()
        self.paper.on_update()
        self.scissors.on_update()


class MyGame(arcade.Window):
    """
    The main class of the application

    NOTE: You can delete the methods you don't need.
    If you need them, replace the keyword "pass" with your own code.
    """

    def __init__(self, width, height, title):
        """
        Initialize the window
        """
        super().__init__(width, height, title)
        self.code_finish = None
        self.player_win = None
        self.partie_nulle = None
        self.user = Player("faceBeard.jpg", 0.5, 150, 500)
        self.pc = arcade.Sprite("compy.jpg", 0.5)
        self.pc_rock = AttackAnimation(AttackType.ROCK)
        self.pc_paper = AttackAnimation(AttackType.PAPER)
        self.pc_scissors = AttackAnimation(AttackType.SCISSORS)
        self.rock_position_x = 45
        self.rock_position_y = 290
        self.paper_position_x = 150
        self.paper_position_y = 290
        self.scissors_position_x = 250
        self.scissors_position_y = 290
        self.game_state = GameState.NOT_STARTED
        self.pc_choices = [AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS]
        self.pc_choice = False
        self.have_chosen = False
        self.user_score = 0
        self.pc_score = 0
        self.user.choice = AttackType.NOT_CHOSEN
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def setup(self):
        """
        Set up your game variables here. Call the method again if you restart a new game.
        """
        # This is where you will create your sprite lists and your sprites.
        # This is also where you will load the sounds of your game.
        pass



    def reset_pos(self):
        """
        Reset the positions of the rock, paper, and scissors sprites to their initial positions
        """
        self.user.rock.center_x = self.rock_position_x
        self.user.rock.center_y = self.rock_position_y
        self.user.paper.center_x = self.paper_position_x
        self.user.paper.center_y = self.paper_position_y
        self.user.scissors.center_x = self.scissors_position_x
        self.user.scissors.center_y = self.scissors_position_y

    def draw_menu(self):
        """
        Draw the game menu
        """
        self.reset_pos()
        arcade.draw_text("Rock, Paper, Scissors :)", 350, 675, arcade.color.BLACK, 25, width=400, align="center")
        self.pc.center_x = 900
        self.pc.center_y = 500
        self.pc.scale = 2.3
        self.pc.draw()
        self.user.draw()
        arcade.draw_text("VS", 500, 500, arcade.color.BLACK, 25)
        arcade.draw_rectangle_outline(900, 290, 75, 75, arcade.color.BLACK, 5)

    def draw_pc_choice_animation(self):
        """
        Draw the computer's attack animation based on its choice
        """
        if self.pc_choice == AttackType.ROCK:
            self.pc_rock.on_update()
        elif self.pc_choice == AttackType.PAPER:
            self.pc_paper.on_update()
        elif self.pc_choice == AttackType.SCISSORS:
            self.pc_scissors.on_update()

    def play_game(self):
        """
        Draw the game
        Compare the choices of the player and the computer to determine the winner for each round + the score
        """
        if self.have_chosen:
            self.pc_choice = choice(self.pc_choices)
            if self.user.choice == self.pc_choice:
                self.partie_nulle = True
                self.player_win = None
            elif self.user.choice == AttackType.ROCK and self.pc_choice == AttackType.PAPER:
                self.pc_score += 1
                self.player_win = False
            elif self.user.choice == AttackType.ROCK and self.pc_choice == AttackType.SCISSORS:
                self.user_score += 1
                self.player_win = True
            elif self.user.choice == AttackType.PAPER and self.pc_choice == AttackType.ROCK:
                self.user_score += 1
                self.player_win = True
            elif self.user.choice == AttackType.PAPER and self.pc_choice == AttackType.SCISSORS:
                self.pc_score += 1
                self.player_win = False
            elif self.user.choice == AttackType.SCISSORS and self.pc_choice == AttackType.ROCK:
                self.pc_score += 1
                self.player_win = False
            elif self.user.choice == AttackType.SCISSORS and self.pc_choice == AttackType.PAPER:
                self.user_score += 1
                self.player_win = True
            self.game_state = GameState.ROUND_DONE
            self.have_chosen = False

    def draw_choice(self):
        """
        Draw the choices of the player and the computer
        """
        if self.have_chosen or self.game_state == GameState.ROUND_DONE or self.game_state == GameState.GAME_OVER:
            if self.user.choice == AttackType.ROCK:
                self.user.rock.center_x = self.user.paper.center_x
                self.user.rock.center_y = self.user.paper.center_y
                self.user.rock.draw()
            elif self.user.choice == AttackType.PAPER:
                self.user.paper.draw()
            elif self.user.choice == AttackType.SCISSORS:
                self.user.scissors.center_x = self.user.paper.center_x
                self.user.scissors.center_y = self.user.paper.center_y
                self.user.scissors.draw()
            if self.pc_choice == AttackType.ROCK:
                self.pc_rock.center_x = 900
                self.pc_rock.center_y = 290
                self.pc_rock.draw()
            elif self.pc_choice == AttackType.PAPER:
                self.pc_paper.center_x = 900
                self.pc_paper.center_y = 290
                self.pc_paper.draw()
            elif self.pc_choice == AttackType.SCISSORS:
                self.pc_scissors.center_x = 900
                self.pc_scissors.center_y = 290
                self.pc_scissors.draw()

    def reset_state(self):
        """
        Reset the game to its initial state
        """
        self.reset_pos()
        self.pc_choice = False
        self.have_chosen = False
        self.game_state = GameState.ROUND_ACTIVE

    def on_draw(self):
        """
        This method is invoked by Arcade at each "frame" to display the elements
        of your game on the screen.
        """
        arcade.start_render()
        self.draw_menu()
        arcade.draw_rectangle_outline(145, 290, 75, 75, arcade.color.BLACK, 5)
        arcade.draw_text(f"Player's score: {self.user_score}", 25, 200,
                         arcade.color.BLACK, 20, width=300, align="center")
        arcade.draw_text(f"Computer's score: {self.pc_score}", 750, 200,
                         arcade.color.BLACK, 20, width=300, align="center")

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text("Press the space key to start", 200, 600, arcade.color.BLACK, 25, width=800,
                             align="center")
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Choose your attack by clicking on it", 350, 600, arcade.color.BLACK, 25, width=400,
                             align="center")
            if not self.have_chosen and not self.pc_choice:
                arcade.draw_rectangle_outline(45, 290, 75, 75, arcade.color.BLACK, 5)

                self.user.paper.draw()
                arcade.draw_rectangle_outline(145, 290, 75, 75, arcade.color.BLACK, 5)
                self.user.scissors.draw()
                arcade.draw_rectangle_outline(245, 290, 75, 75, arcade.color.BLACK, 5)
                self.user.rock.draw()
            else:
                self.draw_choice()
        elif self.game_state == GameState.ROUND_DONE:
            if self.player_win is None:
                arcade.draw_text(f"Draw, press space to play another round",
                                 150, 80, arcade.color.BLACK, 25, width=800, align="center")
            elif self.player_win:
                arcade.draw_text(f"You won, press space to play another round",
                                 150, 80, arcade.color.BLACK, 25, width=800, align="center")
                if self.user_score == 3:
                    self.game_state = GameState.GAME_OVER
                self.draw_choice()
            elif not self.player_win:
                arcade.draw_text(f"You lost, press space to play another round",
                                 150, 80, arcade.color.BLACK, 25, width=800, align="center")
                if self.pc_score == 3:
                    self.game_state = GameState.GAME_OVER
            self.draw_choice()
        elif self.game_state == GameState.GAME_OVER:
            if self.user_score == 3:
                arcade.draw_text(f"You won, the game is over, press space to play another game",
                                 150, 100, arcade.color.BLACK, 25, width=800, align="center")
                self.draw_choice()
            elif self.pc_score == 3:
                arcade.draw_text(f"You lost, the game is over, press space to play another game",
                                 150, 100, arcade.color.BLACK, 25, width=800, align="center")

            self.draw_choice()

    def on_update(self, delta_time):
        """
        All the logic to move the objects of your game and simulate its logic is here. Normally, this is where
        the "update()" method on your sprite lists will be called.
        Parameter:
            - delta_time: the number of milliseconds since the last update.
        """
        self.user.draw_animation()
        self.draw_pc_choice_animation()
        self.play_game()

    def on_key_press(self, key, key_modifiers):
        """
        This method is invoked whenever the user presses a key on the keyboard.
        Parameters:
            - key: the key pressed
            - key_modifiers: are "shift" or "ctrl" pressed?
        """
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.GAME_OVER:
                self.user_score = 0
                self.pc_score = 0
                self.code_finish = False
                self.reset_state()
                self.game_state = GameState.NOT_STARTED
            elif self.game_state == GameState.ROUND_DONE:
                self.reset_state()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Method invoked when the user clicks a mouse button.
        Parameters:
            - x, y: coordinates where the button was clicked
            - button: the mouse button pressed
            - key_modifiers: are "shift" or "ctrl" pressed?
        """
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.user.paper.collides_with_point((x, y)):
                self.user.choice = AttackType.PAPER
                self.have_chosen = True
            if self.user.rock.collides_with_point((x, y)):
                self.user.choice = AttackType.ROCK
                self.have_chosen = True
            if self.user.scissors.collides_with_point((x, y)):
                self.user.choice = AttackType.SCISSORS
                self.have_chosen = True


def main():
    """ Main method """
    game = MyGame(screen_width, screen_height, screen_title)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()