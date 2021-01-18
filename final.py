"""def main():
    fizzbuzz(15)

if __name__ == '__main__':
    main()
"""

#2.3############################################
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print ("Buzz")
    elif number % 3 == 0:
        print ("Fizz")
################################################

#2.4############################################
def prime(n):
    my_list = []
    for i in range(n):
        if ((n % n == 0) & (n % 1 == 0))
            my_list.append(n)    
    print(my_list)
################################################

#2.5############################################
"""def prime_factorization (whole number  n as an input)
    list return_list = ()
    and returns its prime factorization: a list of prime numbers whose product is n.  
    There may be repetitions in the list. For instance, prime_factorization(120) should return [2,2,2,3,5]"""
#################################################

#2.6 Without using the built-in sorting functions in Python, write a my_sort function that takes a list and returns a sorted version.  For instance, my_sort([3,1,2]) should return the list [1,2,3].  Your function can work just like the built-in sorted function mentioned in tutorial 2-4, but the challenge is to implement it yourself!

#2.7#############################################
def tobits(s):
    text = input("Enter text:")
    print("Text is: " + text)
    result = []
    for c in text:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    #input text, in binary form
    b = result
    #print("Your plain-text in binary form") TEST
    #print(b)


    #Using length of result, fill array of equal size, with al 1s. This array will be used to XOR against b.
    #I chose XOR becuase you can easily undo the encryption.
    #def xor_array()
    i = 0
    all_ones = []
    while i < len(result):
        all_ones.append(1)
        i = i + 1
    a = all_ones
    #print("Your XOR key in binary form")
    #print(a)

    #####XOR the two lists#####
    #def xor_strings
    c =[str(int(a[i])^int(b[i])) for i in range(len(a))]
    c =''.join(c)
    print("Your text XOR'd with key")
    #print(c)
    #create new file and fill with encrypted bits
    f = open("encrypted.txt","w+")
    f.write(c)
    f.close()


    ########now decrypt########
    #password = input("Enter deccrypt key:")
    #if password.lower == "paul":
    #####Step 1 : Re-create the binary version of our oringinal word#####
    d =[str(int(a[i])^int(c[i])) for i in range(len(a))]
    d =''.join(d)
    print("here is your decrypted text in binary form: ")
    #print(d)
    #####Step 2 : convert the binary into a readable string#####
    a = ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(d)]*8))
    f = open("decrypted.txt","w+")
    f.write(a)
    f.close()
#################################################


#2.8Save this list of English words to a text file. #############################################
#Use it to write an unscramble function in Python that takes a string of letters and returns a list of English words from the list which consist of exactly the letters from the string.  For instance, unscramble("eilnst") could return ["enlist","listen","silent","inlets","tinsel"].  (I did not test it, so there could be other possibilities!)



