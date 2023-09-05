'''fullName = input("ingresa tu nombre : \n ")
print(f"saludo : {fullName}")'''
##########################################
##                                      ##
##########################################
# This program selects a number between 1 and
# 10 and allows a user (player) to guess what
# it is.


choice = 7  # Número que el jugador debe adivinar

while True:  # Bucle que se ejecuta indefinidamente1
    playerchoice = int(input("Guess the number: "))  # Solicita la suposición del jugador

    if choice == playerchoice:
        print("\t************")
        print("\t* You win! *")  # El jugador gana y el bucle termina
        print("\t************")
        
        
        break  # Sale del bucle while
    else:
        print("Sorry, try again.")  # El jugador no adivinó, se le pide que intente nuevamente
