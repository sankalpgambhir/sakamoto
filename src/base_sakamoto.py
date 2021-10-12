import random

sassy = [
    "Don't make me do your petty work, kid."
]

image = {
    'heads' : "https://i.imgur.com/NusQZZR.png",
    'tails' : "https://i.imgur.com/IkJzBOX.png",
    'lick'  : "https://i.imgur.com/AYCmeEa.jpg"
}

def get_rand_sassy():
    return sassy[random.randint(0, len(sassy)-1)]