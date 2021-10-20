"""
Prints a alphabet rangoli
Input: Only one line of input containing size, the size of the rangoli.
constraints: 0< size< 27
"""
import string

def print_rangoli(size):
    if size > 26:
        print("There are only 26 alphabets.")
        quit()

    alphabets= string.ascii_lowercase
    breadth = (n*2 - 1) + (n*2 - 2)

    # top part
    alpha_slice = alphabets[:n]
    iterations = 1
    top_part = ""
    banana= ""

    while iterations<n:
        banana = banana + alpha_slice[-iterations]
        monkey = banana[iterations-2::-1]

        if iterations == 1 :
            mew_tow = banana  
        else:
            mew_tow = banana + monkey 
        iterations +=1

        mew_theer = ""
        loop_range = len(mew_tow)

        for m1 in range(loop_range):
            if m1 == loop_range-1:
                mew_theer = mew_theer + mew_tow[m1]
                break
            mew_theer = mew_theer + mew_tow[m1] + '-'

        top_part = top_part + mew_theer.center(breadth,'-') + "\n"

    # center
    mid_part = ""
    for i1 in range(1,n):
        mid_part = mid_part + alpha_slice[-i1] + '-'
    for i2 in range(n):
        if i2 == n-1:
            mid_part = mid_part + alpha_slice[i2]
            break
        mid_part = mid_part + alpha_slice[i2] + '-'

    # lower part
    bot_part = ""
    milk= ""

    while iterations>1:
        iterations -=1
        milk = banana[:iterations:]
        cheeze = milk[-2::-1]

        s_newer = milk + cheeze
        this_sstring = ""
        loop_range = len(s_newer)

        for m2 in range(loop_range):
            if m2 == loop_range-1:
                this_sstring = this_sstring + s_newer[m2]
                break
            this_sstring = this_sstring + s_newer[m2] + '-'

        if iterations == 1:
            bot_part = bot_part + this_sstring.center(breadth,'-')
            break
        bot_part = bot_part + this_sstring.center(breadth,'-') + "\n"

    print(top_part+ mid_part+ "\n"+ bot_part)

n = int(input())
print_rangoli(n)