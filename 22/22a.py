total = 10007
deck = list(range(total))

def deal_into_new_stack(deck):
    return list(reversed(deck))

def cut_n_cards(deck, N):
    return deck[N:] + deck[:N]

def increment_n(deck, N):
    result = deck[:]
    for i in range(total):
        result[(i * N) % total] = deck[i]

    return result

shuffles = open('22.txt').read().split('\n')[:-1]
for shuffle in shuffles:
    if shuffle == 'deal into new stack':
        deck = deal_into_new_stack(deck)
    else:
        N = int(shuffle.split(' ')[-1])
        if 'deal' in shuffle:
            deck = increment_n(deck, N)
        else:
            deck = cut_n_cards(deck, N)

print(deck.index(2019))
