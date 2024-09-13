# EXERCISE 4 - SECRET CODE LANGUAGE
# Problem Statement: Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.
  # Coding Rules --> If the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and at the end; else, simply reverse the string.
  # Decoding Rules --> If the word contains less than 3 characters, reverse it; else, remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.
  # Your program should ask whether user want to encode or decode.



from time import sleep

ask1 = int(input("Press 1 to encode, Press 2 to decode: "))

#encoding
if (ask1 == 1):
  sleep(1)
  a1 = str(input("Enter a word to encode: "))
  if (len(a1)>=3):
    x = a1.removeprefix(a1[0])
    y = x + a1[0]
    z = "sit" + y + "sat"
    print(" ")
    sleep(1)
    print("Your encoded word:", z)
  else:
    print(a1[::-1])

#decoding
elif (ask1 == 2):
  sleep(1)
  a2 = str(input("Enter a word to decode: "))
  if (len(a2)>=3):
    l = a2.removeprefix(a2[0:3])
    # print(l)
    m = l.removesuffix(l[len(l)-3:len(l)])
    # print(m)
    n = m.removesuffix(m[-1])
    # print(n)
    o = m[-1] + n
    print(" ")
    sleep(1)
    print("Your decoded word:", o)
  else:
    print(a2[::-1])

else:
  print(" ")
  sleep(1)
  print("Invalid Input!")