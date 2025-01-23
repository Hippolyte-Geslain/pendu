import random
import pygame
import json

words_list = []

#initialize pygame
white = (255, 255, 255)
black = (0, 0, 0)
font=pygame.font.Font(None,60)
height = 600 
width = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")

def load_words():
    try:
        with open("words.json", "r") as file:
            words_list = json.load(file).get("Words",[])
            return words_list
    except (FileNotFoundError,json.JSONDecodeError):
        default_words = {"words": ["example","resolution","error","football","caption","display","company","dog","cat","linux","windows","program","branch","apple","python"]}
        words_list = default_words
        with open("words.json", "w") as file:
            file.write(json.dumps(words_list))
            return words_list

def text_render(text,x,y,color=(black)):
    text=font.render(text,True,color)
    screen.blit(text,(x,y))

def display_wordlist():
    for i, word, in enumerate(words_list):
        text_render(f"{i+1}. {word}",50,200+i*50)


def display_word():
    

def menu():
