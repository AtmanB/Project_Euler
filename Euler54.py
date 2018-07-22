from Timer import timethis


@timethis
def main():
    hands1 = []
    hands2 = []
    ans = 0
    with open('p054_poker.txt') as text:
        for line in text:
            hands1.append(line[:-1].split(' ')[0:5])
            hands2.append(line[:-1].split(' ')[5:10])
    for i in range(1000):
        result = compare_poker_hands(hands1[i], hands2[i])
        if result == 1:
            ans += 1
    print(ans)


def analyze_poker_hand(hand):
    h = ''.join(i for i in hand)
    ranking = [0] * 7
    card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    cards_per_rank = [0] * 13

    for rank in card_ranks:
        cards_per_rank[card_ranks.index(rank)] = h.count(rank)
    m = max(cards_per_rank)
    temp_i = 2
    for i in range(12, -1, -1):
        if cards_per_rank[i] >= 1:
            ranking[temp_i] = i
            temp_i += 1

    if m == 1:
        if ranking[2] - ranking[6] == 4:
            ranking[0] = 4  # Straight

    elif m == 2:
        if cards_per_rank.count(2) == 2:
            ranking[0] = 2  # 2 pairs
            temp_i = 1
            for i in range(12, -1, -1):
                if cards_per_rank[i] == 2:
                    ranking[temp_i] = i
                    temp_i += 1
                elif cards_per_rank[i] == 1:
                    ranking[3] = i
        else:
            ranking[0] = 1  # 1 pair
            ranking[1] = cards_per_rank.index(2)
    elif m == 3:
        if 2 in cards_per_rank:
            ranking[0] = 6  # full house
            ranking[1] = cards_per_rank.index(3)
        else:
            ranking[0] = 3  # 3 of a kind
            ranking[1] = cards_per_rank.index(3)
    elif m == 4:
        ranking[0] = 7  # 4 of a kind
        ranking[1] = cards_per_rank.index(4)

    if h.count('H') == 5 or h.count('D') == 5 or h.count('S') == 5 or h.count('C') == 5:
        if h.count('A') == 1 and h.count('K') == 1 and h.count('Q') == 1 and h.count('J') == 1 and h.count('T') == 1:
            ranking[0] = 9  # GG Royal flush
        elif ranking[2] - ranking[6] == 4:
            ranking[0] = 8  # Straight flush
        else:
            ranking[0] = 5  # Flush
    return ranking


def compare_poker_hands(hand1, hand2):
    hand1_ranking = analyze_poker_hand(hand1)
    hand2_ranking = analyze_poker_hand(hand2)

    for i in range(len(hand1_ranking)):
        if hand1_ranking[i] > hand2_ranking[i]:
            return 1
        elif hand1_ranking[i] < hand2_ranking[i]:
            return 2
        else:
            continue
    return 0


main()
