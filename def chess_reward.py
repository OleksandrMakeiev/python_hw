# 24

def chess_reward():

    checkerboard = 0
    seeds = 1

    while seeds <= 1000000:
        seeds *= 2
        checkerboard += 1

    return  checkerboard, seeds - 1
chess_reward()
print("На %d клеточке зерен будет %d " % (chess_reward()))