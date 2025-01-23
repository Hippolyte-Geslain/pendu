import json
import pygame
import random

#initializing pygame
pygame.init()

#initializing words file
words_file="words.txt"


#intializing the screen and colors
font=pygame.font.Font(None,60)
WHIITE=(255,255,255)
BLACK=(0,0,0)
height=600
width=800
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Hangman")

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
    
def add_word_interface():
    clock=pygame.time.Clock()
    run=True
    word=""
    while run:
        screen.fill(WHIITE)
        word_display("Enter the word",  width //2 - 150, 50)
        word_display(word, 50, 150)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    words=open_file()
                    words=words["words"]
                    words.append(word)
                    with open(words_file, "w") as f:
                        f.write(json.dumps({"words": words}))
                    run=False
                elif event.key==pygame.K_BACKSPACE:
                    word=word[:-1]
                else:
                    word+=event.unicode
    clock.tick(30)

def word_list_interface():
    clock=pygame.time.Clock()
    run=True
    words=open_file()
    words=words["words"]
    while run:
        screen.fill(WHIITE)
        word_display("Words List",  width //2 - 150, 50)
        for i, word in enumerate(words):
            word_display(f"{i+1}. {word}", 50, 150+i*50)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
    clock.tick(30)

def delete_word_list_interface():
    clock=pygame.time.Clock()
    run=True
    words=open_file()
    words=words["words"]
    while run:
        screen.fill(WHIITE)
        word_display("Delete Words List",  width //2 - 150, 50)
        word_display("Do you want to delete one word or all the words?", 50, 150)
        word_display("1. Delete one word", 50, 250)
        word_display("2. Delete all the words", 50, 350)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.unicode=="1":
                    delete_single_word()
                if event.unicode=="2":
                    clear_words_list()
                if event.key==pygame.K_ESCAPE:
                    run=False
        clock.tick(30)
        

def delete_single_word():
    clock=pygame.time.Clock()
    run=True
    words=open_file()
    words=words["words"]
    word=""
    while run:
        screen.fill(WHIITE)
        word_display("Enter the word index to delete",  width //4 - 150, 50)
        word_display("Words List",  width //2 - 150, 100)
        for i, word in enumerate(words):
            word_display(f"{i+1}. {word}", 50, 150+i*50)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.unicode=="1":
                    words.pop(0)
                    with open(words_file, "w") as f:
                        f.write(json.dumps({"words": words}))
                    run=False
                if event.unicode=="2":
                    words.pop(1)
                    with open(words_file, "w") as f:
                        f.write(json.dumps({"words": words}))
                    run=False
                if event.unicode=="3":
                    words.pop(2)
                    with open(words_file, "w") as f:
                        f.write(json.dumps({"words": words}))
                    run=False
                if event.unicode=="4":
                    words.pop(3)
                    with open(words_file, "w") as f:
                        f.write(json.dumps({"words": words}))
                    run=False
                        
                if event.key==pygame.K_ESCAPE:
                    run=False
        clock.tick(30)


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
        word_display(f"Attempts: {attempts}", 50, 250)
        word_display(word, 50, 50)
        hangman_display(attempts)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    run=False
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
    
def menu():
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHIITE)
        word_display("Hangman", width // 2 - 150, 50)
        word_display("1. Play", width // 2 - 100, 200)
        word_display("2. Add a word", width // 2 - 200, 300)
        word_display("3. Word List", width // 2 - 200, 400)
        word_display("4. Delete Word List", width // 2 - 300, 500)
        word_display("5. Exit", width // 2 - 100, 600)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.unicode == "1":
                    playing()
                if event.unicode == "2":
                    add_word_interface()
                if event.unicode == "3":
                    word_list_interface()
                if event.unicode == "4":
                    delete_word_list_interface()
                if event.unicode == "5":
                    pygame.quit()
                    return
                if event.key==pygame.K_ESCAPE:
                    run=False
        clock.tick(30)
menu()  