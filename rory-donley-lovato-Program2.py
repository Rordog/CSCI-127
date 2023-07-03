# -----------------------------------------+
# Rory Donley-Lovato                       |
# CSCI 127, Program 2                      |
# Last Updated: September 21, 2020         |
# -----------------------------------------|
# Simplified Poker Hand evaluation system. |
# -----------------------------------------+


def get_all_ranks(hand):
    result = []
    for card in hand:
        result.append(card[0])
    return result

def royal_flush(hand):
    if (hand[0][1] == hand[1][1] and hand[0][1] == hand[2][1] and hand[0][1] == hand[3][1] and hand[0][1] == hand[4][1]) and (hand[0][0] == 10 and hand[1][0] == 11 and hand[2][0] == 12 and hand[3][0] == 13 and hand[4][0] == 14):
        return True
    else:
        return False

def straight_flush(hand): 
    if (hand[0][1] == hand[1][1] and hand[0][1] == hand[2][1] and hand[0][1] == hand[3][1] and hand[0][1] == hand[4][1]) and (hand[1][0] == hand[0+1][0] and hand[2][0] == hand[1+1][0] and hand[3][0] == hand[2+1][0]and hand[4][0] == hand[3+1][0]):
        return True
    else:
        return False

def straight(hand):
##  Found assistance on Stack Overflow.
    rank_set = { card[0] for card in hand }
    rank_range = max(rank_set) - min(rank_set) + 1
    return rank_range == len(hand) and len(rank_set) == len(hand)
   

def four_of_a_kind(hand):
    if (hand[1] == hand[0] and hand[2] == hand[1] and hand[3] == hand[2]) or (hand[1] == hand[2] and hand[2] == hand[3] and hand[3] == hand[4]):
        return True
    else:
        return False

def full_house(ranks):
    if (ranks[0] == ranks[1] and ranks[1] == ranks[2] and ranks[3] == ranks[4]) or (ranks[0] == ranks[1] and ranks[2] == ranks[3] == ranks[4]):
        return True
    else:
        return False

def three_of_a_kind(ranks):
    if (ranks[0] == ranks[1] and ranks[1] == ranks[2]) or (ranks[1] == ranks[2] and ranks[2] == ranks[3]) or (ranks[2] == ranks[3] and ranks[3] == ranks[4]):
        return True
    else:
        return False

def two_pair(ranks):
    if (ranks[0]==ranks[1] and ranks[2]==ranks[3]) or (ranks[0]==ranks[1] and ranks[3]==ranks[4]) or (ranks[1]==ranks[2] and ranks[3]==ranks[4]):
        return True
    else:
        return False

def one_pair(ranks):
    if (ranks[0]==ranks[1]) or (ranks[1]==ranks[2]) or (ranks[2]==ranks[3]) or (ranks[3]==ranks[4]):
        return True
    else:
        return False


# -----------------------------------------+
# Do not modify the evaluate function.     |
# -----------------------------------------+

def evaluate(poker_hand):
    poker_hand.sort()
    poker_hand_ranks = get_all_ranks(poker_hand)
    print(poker_hand, "--> ", end="")
    if royal_flush(poker_hand):
        print("Royal Flush")
    elif straight_flush(poker_hand):
        print("Straight Flush")
    elif four_of_a_kind(poker_hand_ranks):
        print("Four of a Kind")
    elif full_house(poker_hand_ranks):
        print("Full House")
    elif straight(poker_hand):
        print("Straight")
    elif three_of_a_kind(poker_hand_ranks):
        print("Three of a Kind")
    elif two_pair(poker_hand_ranks):
        print("Two Pair")
    elif one_pair(poker_hand_ranks):
        print("One Pair")
    else:
        print("Nothing")
		
# -----------------------------------------+

def main():
    print("CSCI 127: Poker Hand Evaluation Program")
    print("---------------------------------------")
    evaluate([[10, "spades"], [14, "spades"], [12, "spades"], [13, "spades"], [11, "spades"]])  # royal flush
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "clubs"]])           # straight flush
    evaluate([[2, "diamonds"], [7, "clubs"], [2, "hearts"], [2, "clubs"], [2, "spades"]])       # 4 of a kind
    evaluate([[8, "diamonds"], [7, "clubs"], [8, "hearts"], [8, "clubs"], [7, "spades"]])       # full house
    evaluate([[13, "diamonds"], [7, "clubs"], [7, "hearts"], [8, "clubs"], [7, "spades"]])      # 3 of a kind
    evaluate([[10, "clubs"], [9, "clubs"], [6, "clubs"], [7, "clubs"], [8, "spades"]])          # straight
    evaluate([[10, "spades"], [9, "clubs"], [6, "diamonds"], [9, "diamonds"], [6, "hearts"]])   # 2 pair
    evaluate([[10, "spades"], [12, "clubs"], [6, "diamonds"], [9, "diamonds"], [12, "hearts"]]) # 1 pair
    evaluate([[2, "spades"], [7, "clubs"], [8, "diamonds"], [13, "diamonds"], [11, "hearts"]])  # nothing

# -----------------------------------------+

main()
