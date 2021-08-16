def main():
    input_string = input()
    
    #print(len(input_string))
    kevin,stuart = 0,0
 
    vowels = ['A','E','I','O','U']
    for i in range(len(input_string)):
        if input_string[i] in vowels:
            #print("kEV",kevin+len(input_string) -i)
            kevin = kevin+len(input_string) -i
            
        else:
            #print("STU",stuart+len(input_string) -i)
            stuart = stuart+len(input_string) -i
            
    #print(stuart,kevin)
    if kevin>stuart:
        print("Kevin",kevin)
    elif stuart>kevin:
        print("Stuart",stuart)
    else:
        print("Draw")
        
        
main()