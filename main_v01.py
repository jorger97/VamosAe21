from time import sleep


remaining_cards = 312
decks = 0
aces = 24
playing = True
running_count = 0
true_count = 0
my_game = []
hit_bool = False


def set_hand():
    global my_game
    global  hit_bool
    faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A']
    set_game = True
    sequence_calc = 0
    x = 0
    while set_game:
        pressed = input('Set Game: ')
        x += 1
        if pressed == 'p':
            if x == 1:
                pass
            elif x > 1:
                sequence_calc += 2
        elif pressed == 'm':
            sequence_calc -= 1
        elif pressed == 'a':
            if sequence_calc == 10:
                if hit_bool:
                    x = ace_converter()
                    my_game[0] += x
                    set_game = False
                    print(my_game)
                else:
                    my_game.append(faces[-1])
            else:
                if hit_bool:
                    my_game[0] += faces[sequence_calc]
                    set_game = False
                    print(my_game)
                else:
                    my_game.append(faces[sequence_calc])
            if len(my_game) == 3 and hit_bool == False:
                set_game = False
                print(my_game)
            hit_bool = False
            sequence_calc = 0
            x = 0


def ace_converter():
    global my_game
    return 10


def my_turn():
    global my_game
    dealer = my_game[2]
    print('my turn true count', true_count)

    if my_game[0] == 'A' or my_game[1] == 'A':
        # splitting aces
        if my_game[0] == my_game[1] and dealer != 'A':
            vibrate('split')
        elif my_game[0] == my_game[1] and dealer == 'A':
            if true_count >= -4:
                vibrate('split')
            else:
                vibrate('hit')

    elif my_game[0] != 'A' and my_game[1] != 'A':
        my_hold = int(my_game[0]) + int(my_game[1])

        # splitting
        if my_game[0] == my_game[1]:
            if my_hold == 4:
                if dealer == '2' and true_count >= 6:
                    vibrate('split')
                elif dealer == '3' and true_count >= 1:
                    vibrate('split')
                elif dealer == '4' and true_count >= -3:
                    vibrate('split')
                elif dealer == '5' and true_count >= -6:
                    vibrate('split')
                elif dealer == '6' or dealer == '7' and true_count >= -6:
                    vibrate('split')
                else:
                    vibrate('hit')

            elif my_hold == 6:
                if dealer == '2':
                    vibrate('hit')
                elif dealer == '3' and true_count >= 4:
                    vibrate('split')
                elif dealer == '4' and true_count >= 0:
                    vibrate('split')
                elif dealer == '5' and true_count >= -2:
                    vibrate('split')
                elif dealer == '6' or dealer == '7':
                    vibrate('split')
                else:
                    vibrate('hit')

            elif my_hold == 12:
                if dealer == '2' and true_count >= 2:
                    vibrate('split')
                elif dealer == '3' and true_count >= 0:
                    vibrate('split')
                elif dealer == '4' and true_count >= 1:
                    vibrate('split')
                elif dealer == '5' and true_count >= -4:
                    vibrate('split')
                elif dealer == '6' and true_count >= -5:
                    vibrate('split')
                else:
                    vibrate('hit')

            elif my_hold == 14:
                if (dealer == '8' or dealer == '9'
                        or dealer == '10' or dealer == 'A'):
                    vibrate('hit')
                else:
                    vibrate('split')

            elif my_hold == 16:
                if dealer != '10':
                    vibrate('split')
                elif dealer == '10' and true_count <= 5:
                    vibrate('split')
                elif dealer == '10' and true_count >= 0:
                    vibrate('stand')
                else:
                    vibrate('hit')

            elif my_hold == 18:
                if dealer == '2' and true_count >= -1:
                    vibrate('split')
                elif dealer == '3' and true_count >= -2:
                    vibrate('split')
                elif dealer == '4' and true_count >= -3:
                    vibrate('split')
                elif dealer == '5' and true_count >= -5:
                    vibrate('split')
                elif dealer == '6' and true_count >= -3:
                    vibrate('split')
                elif dealer == '7' and true_count >= 6:
                    vibrate('split')
                elif dealer == '8' or dealer == '9':
                    vibrate('stand')
                elif dealer == '10':
                    vibrate('stand')
                elif dealer == 'A' and true_count >= 6:
                    vibrate('split')
                else:
                    vibrate('stand')

            elif my_hold == 20:
                if dealer == '5' or dealer == '6' and true_count >= 4:
                    vibrate('split')
                elif dealer == '4' and true_count >= 6:
                    vibrate('split')
                else:
                    vibrate('stand')

        # hard standing and hitting
        if my_hold == 12:
            if dealer == '2' and true_count >= 2:
                vibrate('stand')
            elif dealer == '3' and true_count >= 1:
                vibrate('stand')
            elif dealer == '4' and true_count >= 0:
                vibrate('stand')
            elif dealer == '5' and true_count >= -1:
                vibrate('stand')
            elif dealer == '6' and true_count >= -1:
                vibrate('stand')
            else:
                vibrate('hit')

        elif my_hold == 13:
            if dealer == '2' and true_count >= -1:
                vibrate('stand')
            elif dealer == '3' and true_count >= -2:
                vibrate('stand')
            elif dealer == '4' and true_count >= -3:
                vibrate('stand')
            elif dealer == '5' or dealer == '6' and true_count >= -4:
                vibrate('stand')
            else:
                vibrate('hit')

        elif my_hold == 14:
            if dealer == '2' and true_count >= -3:
                vibrate('stand')
            elif dealer == '3' and true_count >= -4:
                vibrate('stand')
            elif dealer == '4' and true_count >= -5:
                vibrate('stand')
            elif dealer == '5':
                vibrate('stand')
            elif dealer == '6' and true_count >= -6:
                vibrate('stand')
            else:
                vibrate('hit')

        elif my_hold == 15:
            if dealer == '2' and true_count >= -5:
                vibrate('stand')
            elif dealer == '3' and true_count >= -6:
                vibrate('stand')
            elif dealer == '4' or dealer == '5' or dealer == '6':
                vibrate('stand')
            elif dealer == '7' or dealer == '8' or dealer == 'A':
                vibrate('hit')
            elif dealer == '9' and true_count >= 6:
                vibrate('stand')
            elif dealer == '10' and true_count >= 3:
                vibrate('stand')
            else:
                vibrate('hit')

        elif my_hold == 16:
            if dealer in str(range(2, 7)):
                vibrate('stand')
            elif dealer == '7' or dealer == 'A':
                vibrate('hit')
            elif dealer == '8' and true_count >= 6:
                vibrate('stand')
            elif dealer == '9' and true_count >= 4:
                vibrate('stand')
            elif dealer == '10' and true_count >= 0:
                vibrate('stand')
            else:
                vibrate('hit')

        elif my_hold == 17:
            if dealer == 'A' and true_count >= -6:
                vibrate('stand')
            elif dealer == 'A' and true_count < -6:
                vibrate('hit')
            else:
                vibrate('stand')

        elif my_hold >= 18:
            vibrate('stand')


def reset_my_game():
    global my_game
    my_game = []
    vibrate('reset_hand')


def reset_all():
    global aces
    global running_count
    global true_count
    global remaining_cards
    aces = 24
    running_count = 0
    true_count = 0
    remaining_cards = 312


def bet_units():
    if true_count <= 0:
        vibrate('lowtc')
    elif true_count == 1:
        vibrate('1tc')
    elif true_count == 2:
        vibrate('2tc')
    elif true_count == 3:
        vibrate('3tc')
    elif true_count >= 4:
        vibrate('4tc')


def set_true_count():
    global running_count
    global decks
    global true_count
    global aces

    decks = remaining_cards/52
    true_count = round(running_count/decks)  # or tc = tc + round(...)
    print('\nTrueCount: ', true_count)
    print('running count: ', running_count)
    print('Remaining cards: ', remaining_cards)
    print('Remaining decks', decks)
    print('Remaining aces: ', aces)
    running_count = true_count
    print('New running count: ', running_count)


def summary():
    global running_count
    global decks
    global true_count
    global aces
    global remaining_cards
    decks = remaining_cards/52
    true_count = round(running_count/decks)
    print('\nTrue count: ', true_count)
    print('Running count: ', running_count)
    print('Remaining cards: ', remaining_cards)
    print('Remaining decks', decks)
    print('Remaining aces: ', aces)
    running_count = true_count
    print('New running count: ', running_count)


def hitted():
    global my_game


def vibrate(move):
    global hit_bool
    if move == 'stand':
        print('***Vibrate***')
    elif move == 'hit':
        print('***vibrate***')
        print('***vibrate***')
        hit_bool = True
        hitted()
    elif move == 'double':
        print('***vibrate***')
        print('***vibrate***')
        print('***vibrate***')
    elif move == 'split':
        print('***vibrate***')
        print('***vibrate***')
        print('***vibrate***')
        print('***vibrate***')
    elif move == 'reset_hand':
        print('***Vibrate 1 Second***')
        print('Delay 2 seconds')
        sleep(2)
    elif move == 'lowtc':
        print('***Vibrate .5 seconds***')
    elif move == '1tc':
        print('***Vibrate 1 second***')
    elif move == '2tc':
        print('***Vibrate 1 second***')
        print('***Vibrate 1 second***')
    elif move == '3tc':
        print('***Vibrate 1 seconds***')
        print('***Vibrate 1 second***')
        print('***Vibrate 1 second***')
    elif move == '4tc':
        print('***Vibrate 1 seconds***')
        print('***Vibrate 1 second***')
        print('***Vibrate 1 second***')
        print('***Vibrate 1 second***')


print('Press corresponding buttons')
print('[A]=Ace')
print('[M]=Minus card')
print('[P]=Plus card')
print('[E] = Set Hand')
print('[A15]= My Turn')
print('[M15]=reset all')

while playing:
    i = input('Button Simulator [A], [M], [P], [E]')

    if i == 'a':
        aces -= 1
        remaining_cards -= 1

    elif i == 'm':
        running_count -= 1
        remaining_cards -= 1

    elif i == 'p':
        running_count += 1
        remaining_cards -= 1

    elif i == 'e':
        set_hand()

    elif i == 'a15':
        set_true_count()
        my_turn()
        reset_my_game()
        print('\nBET')
        bet_units()
    elif i == 'm15':
        reset_all()
