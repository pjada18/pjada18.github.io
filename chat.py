from random import *
joke=["Only a Genius can say these four words, four times really fast without getting tongue twisted. EYE, YAM, STEW, PEE"]

def intro():
    print("Hey, name is Andre. I am your new best friend")

def sayhi(name):
    print("What's up " + name)
def main():
  while True:
      user = input("What is your name?")
      sayhi(user)
      intro()
      print("Hi " + user)
      answer = input("Do you want to hear a joke? ")
      if "yes" in answer:
        print("That's cool!")
        aRandomIndex = randint(0, len(joke)-1)
        print(joke[aRandomIndex])
        again = input("Do you want to hear another joke?")
      else:
          print("awww, welllll... I am going to talk to someone who actually wants to talk to me, BYE!!")
          break

      if "yes" in again:
        print("AWESOME!!")
        aRandomIndex = randint(0, len(joke)-1)
        print(joke[aRandomIndex])
      else:
        print("ohhhh, well... Let's play truth or dare")
        game=input("Truth or dare? ")
      if "truth" in game:
          Tru=input("What is the silliest thing you have an emotional attachment to?" )
          print("WOW!!! LOLOL!!")
          print("Thanks for spending time with me, come back soon.")
      else:
          Dar=input("Tell me about your most awkward date." )
          print(ohhhh, I have no words.")
          print("I love talking to you, I work to finish, talk to you later, bye/")
      break


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
