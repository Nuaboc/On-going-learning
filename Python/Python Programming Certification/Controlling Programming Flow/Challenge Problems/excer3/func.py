"""
Module for scoring blackjack hands.

In blackjack, face cards are worth 10, number cards are worth their value, and Aces
are worth either 1 or 11, whichever is more advantageous. The latter is what makes
scoring blackjack so tricky.

In this module, we assume that a card hand is represented by a tuple of strings, where
each string is two characters representing a card.  The first character is the rank of
the card: '2'-'9' for numerical cards, 'T' for 10, 'J' for Jack, 'Q' for Queen, 'K' for
King and 'A' for Ace.  The second character is the suit: 'H' for hearts, 'D' for diamonds,
'C' for clubs, and 'S' for spades.

For example ('KS','AD') is a blackjack hand with the King of Spades and Ace of Diamonds.

Author: Gabriel Martinez
Date: September 15, 2020
"""
import introcs


def bjack(hand):
    """
    Returns the score of the blackjack hand.

    When scoring the hand, number cards are always worth their value and face cards
    (Jack, Queen, King) are always worth 10.  However, Aces are either worth 1 or 11,
    which ever is more advantageous.

    When determining how to value a hand, the score should be as high as possible without
    going over 21.  If the hand is worth more than 21 points, then all Aces should be
    worth 1 point.

    Examples:
        bjack(('KS','AD')) returns 21
        bjack(('KS','9C','AD')) returns 20
        bjack(('AS','AC','KH')) returns 12
        bjack(('AS','AC','KH','TD')) returns 22
        bjack(()) returns 0

    Parameter hand: the blackjack hand to score
    Precondition: hand is a (possibly empty) tuple of 2-character strings representing
    cards. The first character of each string is '2'-'9', 'T', 'J', 'Q', 'K', or 'A'.
    The second character of each string is 'H', 'D', 'C', or 'S'.
    """
    # Hint: Keep track of whether you have seen any aces in the hand that are worth 11
    # If so, subtract 10 from the accumulator if you go over.
    cards = ('2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH',
             '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD',
             '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC',
             '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS',)
    score = 0
    cards_checked = 0
    aces_on_hand = 0
    present_card = 0

    while True:
        print('starting loop')
        # found = introcs.find_tup(cards, card)
        if len(hand) > cards_checked:
            print('cards left to check ' + str(len(hand) - cards_checked))
            cards_checked += 1
        else:
            print('all cards checked')
            return score

        if hand[present_card][0] == 'T' or hand[present_card][0] == 'J' or \
                hand[present_card][0] == 'Q' or hand[present_card][0] == 'K':
            print(hand[present_card][0])
            print('conditional for == to # 2-9 or "T, J, Q, or K" passed')
            score += 10
            print(score)
            if score > 21 and aces_on_hand * -10 == score > 21:
                score -= 10
                aces_on_hand -= 1
                print(score)
                print('aces on hand ' + str(aces_on_hand))
        elif hand[present_card][0] == 'A':
            print('conditional >> present_card == "A" passed')
            aces_on_hand += 1
            print(' aces on hand: ' + str(aces_on_hand))
            if score >= 11:
                print('need "A" as 1')
                score += 1
            else:
                print('need "A" as 11')
                score += 11

            if score > 21 and aces_on_hand > 0:
                score -= 10

        else:
            print('add card from 2-9 or 10')
            score += int(hand[present_card][0])
            print(score)

        present_card += 1
        print(score)


print(bjack(('AS', 'AC', 'KH', 'TD')))
