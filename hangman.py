def hangman (word):
    wrong = 0 #Number of misstakes made by player 1
    stages = ["",
              "_________         ",
              "|                 ",
              "|        |        ",
              "|        0        ",
              "|       /|/       ",
              "|       //        ",
              "|                 ",
              ]
    rletters = list(word) #list of letters of word
    board = ["_"] * len(word) #list with _ for the number of charactors included in word
    win = False
    print("Welcom to hungman!")
    while wrong < len(stages) - 1: # e.g. the number of stages is 8 but max wrogn is 7
        print("\n")
        msg = "Guess one letter "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print ("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The answer is {}.".format(word))
        

hangman("cat")
