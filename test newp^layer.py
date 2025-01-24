score = {
         'joueur':['hippo','zac','akram'],
         'score_facile':[1,2,3],
         'score_moyen':[4,5,6],
         'score_difficile':[7,8,9]
         }

def newplayer():
    new_player = input('Enter player name: ')

    score['joueur'] += {new_player}
    score['score_facile'] += {0}
    score['score_moyen'] += {0}
    score['score_difficile'] += {0}
    print(score)
    print('score:',score['joueur'][0],score['score_facile'][0],score['score_moyen'][0],score['score_difficile'][0])
newplayer()