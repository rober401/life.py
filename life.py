# Generation

import os
import string
import random
import names

# We want are program to have a person to get to this
expected_values = [1, 2, 3, 4, 5]

generation = 0

# Population System
class Person:
    def __init__(self, name, A, B, C, D, E, score):
        self.name = name
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.score = score

# create a list to store Person objects
people = []
bestTry = []

def mutation():
    global expected_values
    for i in range(len(people)):
        if people[i].A != expected_values[0]:
            people[i].A = random.randint(1, 5)

        if people[i].B != expected_values[1]:
            people[i].B = random.randint(1, 5)

        if people[i].C != expected_values[2]:
            people[i].C = random.randint(1, 5)

        if people[i].D != expected_values[3]:
            people[i].D = random.randint(1, 5)

        if people[i].E != expected_values[4]:
            people[i].E = random.randint(1, 5)
    scoring()


def filterScore():  # Function finds who has the best score
    global bestTry
    bestTry = []
    tempList = []                                   # Temp list
    tempIndex = 0                                   # Temp Index
    for i in range(len(people)):
        tempList.append(people[tempIndex].score)
        tempIndex += 1

    maxScore = max(tempList)
    index = tempList.index(maxScore)
    print(index)
    print(people[index].name)


    bestTry.append(people[index].A)
    bestTry.append(people[index].B)
    bestTry.append(people[index].C)
    bestTry.append(people[index].D)
    bestTry.append(people[index].E)

    print(bestTry)
    if bestTry == expected_values:
        print(f"\n\n\ngenerations {generation}")
        print("100% Completed")
        input("")
        quit()
    else:
        copyCat()

def copyCat():
    global expected_values, score, people, bestTry, generation
    generation += 1
    people = []

    person1 = Person(names.get_first_name(), bestTry[0], bestTry[1], bestTry[2], bestTry[3], bestTry[4], 0)
    people.append(person1)

    person2 = Person(names.get_first_name(), bestTry[0], bestTry[1], bestTry[2], bestTry[3], bestTry[4], 0)
    people.append(person2)

    person3 = Person(names.get_first_name(), bestTry[0], bestTry[1], bestTry[2], bestTry[3], bestTry[4], 0)
    people.append(person3)

    person4 = Person(names.get_first_name(), bestTry[0], bestTry[1], bestTry[2], bestTry[3], bestTry[4], 0)
    people.append(person4)

    person5 = Person(names.get_first_name(), bestTry[0], bestTry[1], bestTry[2], bestTry[3], bestTry[4], 0)
    people.append(person5)
    mutation()

# Scoring System
def scoring():
    global expected_values, score, people     # Vars and lists
    personindex = 0
    for i in range(len(people)):                # Loop for the amount of people to check there scores

        score = 0                               # Score
        x = 0                                   # Temp Index

        List = []                               # Temp List

        # Take in persons list
        List.append(people[personindex].A)
        List.append(people[personindex].B)
        List.append(people[personindex].C)
        List.append(people[personindex].D)
        List.append(people[personindex].E)

        print(people[personindex].name)
        print(List)

        for i in range(len(expected_values)):   # Loop for the length of chars in expected values
            if List[x] == expected_values[x]:   # if the index of the list is == to the index of expected value
                score += 5                      # give score +5
            else:
                score -= 1                      # give score -1
            x += 1                              # change index +1

        people[personindex].score = score
        print(score)                            # score for that list
        personindex += 1
    filterScore()











# Needs function to add people based on a number

# Adding to Population
person1 = Person(names.get_first_name(), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 0)
people.append(person1)

person2 = Person(names.get_first_name(), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 0)
people.append(person2)

person3 = Person(names.get_first_name(), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 0)
people.append(person3)

person4 = Person(names.get_first_name(), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 0)
people.append(person4)

person5 = Person(names.get_first_name(), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), random.randint(1, 5), 0)
people.append(person5)

scoring()
