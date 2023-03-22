def endcode(string):
    int_list = [int(x) for x in string]
    int_list = [ x +3 for x  in int_list]


    print("Your password has been encoded and stored!\n")


    return int_list
    
    
def decode(string):
    orig  = [x - 3 for x in string]
    orig = "".join(str(x) for x in orig)
    string = "".join(str(x) for x in string)

    print('The encoded password is ', string, ', and the original password is ',orig,'.')
    
def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        inp = int(input('Please enter an option: '))
        if inp == 1:
            password = input("Please enter your password to encode: ")
            enc = endcode(password)

            
        elif inp ==2:
            decode(enc)
        elif inp ==3:
            quit()

if __name__ =='__main__':
    main()

