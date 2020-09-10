import random as r

def random_word():
    with open("snowpods.txt",'r') as f:
        list1=f.readlines()
        randword=(r.choice(list1)).strip()
    return randword

def play():
    str1=random_word()
    attempt=6
    list1=list(str1)
    set1=set(list1)
    size=len(set1)

    # print(str1)
    display_list=list('_'*len(str1))
    print ("The word is :\n")
    print("".join(display_list))


    while size > 0 and attempt > 0:
        val=input("Guess the Word!!\n").upper()

        if val in list1:
            # i=list1.index(val)
            # list1[i]='_'
            temp=[i for i in range(len(list1)) if list1[i]==val]
            for j in temp:
                display_list[j]=val
            print("".join(display_list))
            size-=1
        else:
            attempt-=1
            print("you have {} attempt left".format(attempt))

    print("The word was : ",str1)

    if not size:
        print("You won!!")
    else:
        print("Please try again!!")




def main():
    print("Welcome to Hangman word game!!\n")
    print("---"*10)

    play()

if __name__ == '__main__':
    main()
