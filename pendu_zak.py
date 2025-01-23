import pygame
import random
import os

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600  
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 60)

# Fichiers locaux
words_file = "words.txt"  # Fichier contenant les mots
socres_file = "scores.txt"   # Fichier pour enregistrer les scores

# Charger les mots depuis le fichier
def load_words():
    if not os.path.exists(words_file):
        with open(words_file, "w") as f:
            f.write("exemple\n")
    with open(words_file, "r") as f:
        mots = f.read().splitlines()
    return mots

def effacer_mots():
    with open(words_file, "w") as f:
        f.write("")  # Réinitialise le fichier en l'effaçant

def ajouter_score(score):
    if not os.path.exists(socres_file):
        with open(socres_file, "w") as f:
            f.write("Scores:\n")
    with open(socres_file, "a") as f:
        f.write(f"{score}\n")

def choisir_mot():
    mots = load_words()
    return random.choice(mots)

# Initialiser l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

def afficher_texte(texte, x, y, couleur=BLACK):
    texte_render = FONT.render(texte, True, couleur)
    screen.blit(texte_render, (x, y))

def menu_principal():
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)
        afficher_texte("JEU DU PENDU", WIDTH // 2 - 150, 50)
        afficher_texte("1. Jouer", WIDTH // 2 - 100, 200)
        afficher_texte("2. Ajouter un mot", WIDTH // 2 - 200, 300)
        afficher_texte("3. Voir les mots", WIDTH // 2 - 200, 400)
        afficher_texte("4. Effacer la liste des mots", WIDTH // 2 - 300, 500)
        afficher_texte("5. Quitter", WIDTH // 2 - 100, 600)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    jouer_partie()
                elif event.key == pygame.K_2:
                    ajouter_mot_interface()
                elif event.key == pygame.K_3:
                    voir_mots()
                elif event.key == pygame.K_4:
                    effacer_mots()
                elif event.key == pygame.K_5:
                    pygame.quit()
                    return

        clock.tick(30)

def voir_mots():
    clock = pygame.time.Clock()
    mots = load_words()
    while True:
        screen.fill(WHITE)
        afficher_texte("Liste des mots:", 50, 50)
        for i, mot in enumerate(mots):
            afficher_texte(mot, 50, 100 + i * 40)
        afficher_texte("Appuyez sur Echap pour revenir au menu", 50, HEIGHT - 50, RED)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        clock.tick(30)

def jouer_partie():
    mot = choisir_mot()
    lettres_trouvees = set()
    lettres_tentees = set()
    essais_restants = 6
    clock = pygame.time.Clock()

    def mot_cache():
        return " ".join([lettre if lettre in lettres_trouvees else "_" for lettre in mot])

    while True:
        screen.fill(WHITE)
        afficher_texte("PENDU", WIDTH // 2 - 100, 50)
        afficher_texte(f"Mot: {mot_cache()}", 50, 150)
        afficher_texte(f"Essais restants: {essais_restants}", 50, 250)
        afficher_texte(f"Lettres tentées: {', '.join(sorted(lettres_tentees))}", 50, 350)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                lettre = event.unicode.lower()
                if lettre.isalpha() and lettre not in lettres_tentees:
                    lettres_tentees.add(lettre)
                    if lettre in mot:
                        lettres_trouvees.add(lettre)
                    else:
                        essais_restants -= 1

        if essais_restants <= 0:
            afficher_texte("Perdu!", WIDTH // 2 - 100, HEIGHT // 2, RED)
            pygame.display.flip()
            pygame.time.delay(2000)
            ajouter_score(0)  # Score de 0 pour une partie perdue
            return

        if all(lettre in lettres_trouvees for lettre in mot):
            afficher_texte("Gagné!", WIDTH // 2 - 100, HEIGHT // 2, RED)
            pygame.display.flip()
            pygame.time.delay(2000)
            score = essais_restants * 10  # Exemple de calcul de score
            ajouter_score(score)
            return

        clock.tick(30)

def ajouter_mot_interface():
    clock = pygame.time.Clock()
    mot = ""
    while True:
        screen.fill(WHITE)
        afficher_texte("Ajouter un mot", WIDTH // 2 - 150, 50)
        afficher_texte("Tapez le mot et appuyez sur Entrée:", 50, 150)
        afficher_texte(mot, 50, 250)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    ajouter_mot(mot)
                    return
                elif event.key == pygame.K_BACKSPACE:
                    mot = mot[:-1]
                else:
                    mot += event.unicode

        clock.tick(30)

if __name__ == "__main__":
    menu_principal()