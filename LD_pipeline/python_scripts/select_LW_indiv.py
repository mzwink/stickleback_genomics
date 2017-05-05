import random

#Select 10, 15 individuals to go through LD pipeline

def random_indiv_generator(number_individuals):
    output = open("LW_" + str(number_individuals) + "_populations.txt" , 'w')
    selected_indivs = {}

    while len(selected_indivs.keys()) < number_individuals:
        rand_indiv = random.randint(1,20)
        indiv = "LW_" + str(rand_indiv)

        if indiv in selected_indivs.keys():
            continue
        else:
            selected_indivs[indiv] = "selected"

    for key in selected_indivs.keys():
        output.write(str(key) + "\n")


random_indiv_generator(15)
