import pygame
import random

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 60) #pygame.font.SysFont(None, 60) sert a changer la police

# Charger les mots depuis un fichier
MOTS_FICHIER = "mots.txt"

def charger_mots():
    try:
        with open(MOTS_FICHIER, "r") as f:
            return f.read().splitlines() #read().splitlines() sert a lire les lignes du fichier
    except FileNotFoundError: #si le fichier n'existe pas
        return ["exemple"]

def choisir_mot():
    mots = charger_mots()
    return random.choice(mots)

# Initialiser l'écran
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #pygame.display.set_mode((WIDTH, HEIGHT)) sert a creer la fenetre
pygame.display.set_caption("Jeu du Pendu") #pygame.display.set_caption("Jeu du Pendu") sert a changer le titre de la fenetre

# Fonction pour afficher du texte sur l'écran
def afficher_texte(texte, x, y, couleur=BLACK):
    texte_render = FONT.render(texte, True, couleur) #.render(texte, True, couleur) sert a creer un objet texte
    screen.blit(texte_render, (x, y))  #.blit(texte_render, (x, y)) sert a afficher le texte sur l'ecran

# Fonction principale du jeu
def jouer():
    mot = choisir_mot()
    lettres_trouvees = set()
    essais_restants = 6
    clock = pygame.time.Clock() #pygame.time.Clock() sert a creer un objet clock (qui est un minuteur)

    # Boucle principale du jeu
    running = True
    while running:
        screen.fill(WHITE)  # Remplir l'écran avec du blanc

        # Afficher l'état actuel
        mot_affiche = " ".join([lettre if lettre in lettres_trouvees else "_" for lettre in mot])
        afficher_texte(f"Mot: {mot_affiche}", 50, 150)
        afficher_texte(f"Essais restants: {essais_restants}", 50, 250)

        pygame.display.flip()  # Mettre à jour l'affichage

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                lettre = event.unicode.lower()
                if lettre.isalpha() and lettre not in lettres_trouvees:
                    if lettre in mot:
                        lettres_trouvees.add(lettre)
                    else:
                        essais_restants -= 1

        # Conditions de fin
        if essais_restants <= 0:
            afficher_texte("Perdu!", WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        if all(lettre in lettres_trouvees for lettre in mot):
            afficher_texte("Gagné!", WIDTH // 2 - 100, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        clock.tick(30)  # Limiter à 30 FPS

# Lancer le jeu
if __name__ == "__main__":
    jouer()
    pygame.quit()
