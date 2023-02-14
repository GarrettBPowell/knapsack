import algs
import time
import optoSol as op

def print_menu():
    menu = """================================\n
           MENU\n
               ================================\n
               1 - Greedy by Weight            \n
               2 - Greedy by Value             \n
               3 - Greedy by Ratio             \n
               4 - All Greedy                  \n
               5 - Exhaustive w\ Prune         \n
               6 - Exhaustive Search           \n
               7 - Simmulated Annealing        \n
               9 - Exit                        \n
               ================================\n
           Enter a choice and press enter:"""
    print(menu)

def printAnswer(result, algType):
    print('With a maximum weight of {}. The {} algorithm recommends you take the following items:'.format(result[0], algType))
    result[1].sort(key=lambda a: a[0])

    totalWeight = 0
    totalValue = 0

    for row in result[1]:
        totalWeight += int(row[1])
        totalValue += int(row[2])
        print(row)

    print('\nWhich results in a total weight of {} and a total value of {}\n\n'.format(totalWeight, totalValue))




def menu():

    print_menu()
    user_input = 0

    while user_input != 9:
        
        user_input = int(input())
        #startTime = time.time()

        # Greedy by Weight
        if user_input == 1:
            print('Running the Greedy by Weight Algorithm')
            print("What is the name of the file in the cases folder that you want to use? (No extension)")
            user_input = input()
            printAnswer(algs.greedyByWeight(user_input), "Greedy by Weight")

        # Greedy by Value
        elif user_input == 2:
            print('Running the Greedy by Value Algorithm')
            print("What is the name of the file in the cases folder that you want to use? (No extension)")
            user_input = input()
            printAnswer(algs.greedyByValue(user_input), "Greedy by Value")

        # Greedy by Ratio
        elif user_input == 3:
            print('Running the Greedy by Ratio Algorithm')
            print("What is the name of the file in the cases folder that you want to use? (No extension)")
            user_input = input()
            printAnswer(algs.greedyByRatio(user_input), "Greedy by Ratio")

        # All 3 Greedy
        elif user_input == 4:
            print('Running All Algs')
            print("What is the name of the file in the cases folder that you want to use? (No extension)")
            user_input = input()
            printAnswer(algs.greedyByWeight(user_input), "Greedy by Weight")
            printAnswer(algs.greedyByValue(user_input), "Greedy by Value")
            printAnswer(algs.greedyByRatio(user_input), "Greedy by Ratio")

        # Exhaustive with Pruning
        elif user_input == 5:
            print('Running Exhaustive with Pruning')
            print("What is the name of the file in the cases folder that you want to use? (No extension)")
            user_input = input()
            printAnswer(algs.exhaustivePrune(user_input), "Exhaustive Search with Pruning")

        # Exhaustive
        elif user_input == 6:
            print('Running Exhaustive Search')
            print("What is the name of the file in the cases folder that you want to use? (No extension)")
            user_input = input()

            printAnswer(algs.exhaustiveSearch(user_input), "Exhaustive Search")

        # Annealing
        elif user_input == 7:
            print('Running Simmulated Annealing')
            print("What is the name of the file in the cases folder that you want to use? (No extension)")
            user_input = input()

            printAnswer(op.annealing(user_input), "Simmulated Annealing")

        # Exit
        elif user_input == 9:
            print('Exiting...')
        #endTime = time.time()
        #print("Time elapsed = {}".format(endTime - startTime))
        print("\nPress enter to continue...")
        clutter = input()
        print('\n\n\n\n\n\n')
        print_menu()

# Run Menu
menu()