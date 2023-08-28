word = "monkey"
u_ipt = True
count = 0
guess_lim = 3

while u_ipt:
        
    if count<guess_lim:
        user_input = input("Guess the word: ").strip()
        count += 1
        
        if user_input == word:
            print("You won")
            u_ipt = False
    else:
        print("You're out of guess")
        u_ipt = False
        
