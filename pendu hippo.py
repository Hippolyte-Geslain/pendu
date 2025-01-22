import json
import pygame
import random

#initializing pygame
pygame.init()

#initializing words file
words_file="words.txt"


#intializing the screen and colors
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Hangman")
font=pygame.font.Font(None,60)
WHIITE=(255,255,255)
BLACK=(0,0,0)


def open_file():
    try:
        with open(words_file, "r") as f:
            content = f.read()
            if not content.strip():  # Check if the file is empty or contains only whitespace
                raise FileNotFoundError
            words_dict = json.loads(content)
            return words_dict
    except (FileNotFoundError, json.JSONDecodeError):
        print("File not found or invalid JSON. Creating a new file with default words.")
        default_dict = {"words": ["example", "hangman", "python", "programming"]}
        with open(words_file, "w") as f:
            f.write(json.dumps(default_dict))
        return default_dict
    
#randomaly selecting a word from the list
def words_list():
    words=open_file()
    words=words["words"]
    if not words:
        raise ValueError("The words list is empty")
    return random.choice(words)


def word_display(text,x,y,color=(BLACK)):
    text=font.render(text,True,color)
    screen.blit(text,(x,y))

def hangman_display(attempts):
    pygame.draw.line(screen, BLACK,(450, 300), (700, 300),5)
    pygame.draw.line(screen, BLACK,(500, 125), (525, 100),5)
    pygame.draw.lines(screen, BLACK, False, [(500, 300), (500, 100), (650, 100), (650, 125)], 5)
    if attempts < 6:
        pygame.draw.circle(screen, BLACK, (650, 145), 20,5)
    if attempts < 5:
        pygame.draw.line(screen, BLACK, (650, 165), (650, 215), 5)
    if attempts < 4:
        pygame.draw.line(screen, BLACK, (650, 187), (625, 165), 5)
    if attempts < 3:
        pygame.draw.line(screen, BLACK, (650, 187), (675, 165), 5)
    if attempts < 2:
        pygame.draw.line(screen, BLACK, (650, 215), (625, 237), 5)
    if attempts < 1:
        pygame.draw.line(screen, BLACK, (650, 215), (675, 237), 5)
    pygame.display.flip()
    


def playing():
    run = True
    
    word = words_list()
    word = word.lower()
    guessed_letters = set()
    attempts = 6        
    clock = pygame.time.Clock()
    while run:      

        screen.fill((WHIITE))
        word_display(" ".join([letter if letter in guessed_letters else "_" for letter in word]), 50, 150)
        word_display(f"Attemps: {attempts}", 50, 250)
        word_display(word, 50, 50)
        hangman_display(attempts)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                letter = event.unicode.lower()
                if letter.isalpha() and letter not in guessed_letters:
                    if letter in word:
                        guessed_letters.add(letter)
                    else:
                        attempts -= 1

        if attempts == 0:        
            pygame.draw.line(screen, BLACK, (650, 215), (675, 237), 5)
            word_display(f'You lost..The word was "{word}"', 50, 350)
            pygame.display.flip()
            pygame.time.delay(2000)
            break

        if all (letter in guessed_letters for letter in word):
            word_display(f"You won!", 50, 350)
            pygame.display.flip()
            pygame.time.delay(2000)
            break

        clock.tick(30)
    
playing()