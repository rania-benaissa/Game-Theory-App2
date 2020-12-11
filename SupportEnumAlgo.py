from Player import Player

import itertools as iter

import numpy as np

import sympy as sp


class SupportEnumAlgo:

    def __init__(self, players):

        self.players = players

# Is called in game's function to launch the algorithm
    def supportEnumAlgo(self):

        players = self.players
        self.nashs = []

        # symboles utilisés
        x = sp.symbols('x1, x2,x3')
        v = sp.symbols('v')

        # ce sont mes matrices A et B
        self.a = np.copy(players[0].gain)

        self.b = np.copy(players[1].gain)
        # je transpose B pour pouvoir parcourir par ligne
        self.b = self.b.transpose()

        # n = nbr strategies j1 et m = nbr strategies j2
        n = len(self.a)
        m = len(self.a[0])

        # represente le nombre d'elements possibles dans un ensemble( I J )
        kMax = min(len(self.b), len(self.a))

        # pour tous les k possibruh aka k = 1 , 2 ,3 (au max)
        for k in range(1, kMax + 1):

            # player 1 set
            setI = list(map(list, iter.combinations(
                np.arange(1, len(self.a) + 1), k)))

            # player 2 set
            setJ = list(map(list, iter.combinations(
                np.arange(1, len(self.b) + 1), k)))

            for elementI in setI:

                for elementJ in setJ:

                    self.elementI = elementI
                    self.elementJ = elementJ

                    # get I equations
                    equationsI = self.getEquations(elementI, elementJ, self.b)

                    # get I solutions and adjust them
                    solusI = list(sp.linsolve(
                        equationsI, (x[0], x[1], x[2], v)))

                    solusI = self.adjust(solusI, n)

                    # # get J equations
                    equationsJ = self.getEquations(elementJ, elementI, self.a)

                    # get J solutions and adjust them
                    solusJ = list(sp.linsolve(
                        equationsJ, (x[0], x[1], x[2], v)))
                    solusJ = self.adjust(solusJ, m)

                    self.isEquilibrium(solusI, solusJ)

        return self.nashs

# returns the equations
    def getEquations(self, element1, element2, matrix):

        equations = []

        # these are symbols
        x = sp.symbols('x1, x2,x3')
        v = sp.symbols('v')

        for i in element2:
            # on reecupere la ligne de la matrice
            row = matrix[i - 1]

            equation = - v

            for j in element1:

                equation = equation + row[j - 1] * x[j - 1]

            equations.append(equation)

        equation = -1

        for j in element1:

            equation = equation + x[j - 1]

        equations.append(equation)

        return equations

# ajuste les resultats des sys des equas lineaires
    def adjust(self, solutions, dim):

        sols = []

        x = sp.symbols('x1, x2,x3')

        for tup in solutions:

            # enleve la val de "v"
            tup = tup[: len(tup) - 1]
            l = []

            for i in range(0, dim):

                # les valeurs inconnues sont mises a 0 les autres sont recopiées

                if(tup[i] != x[1] and tup[i] != x[0] and tup[i] != x[2]):

                    l.append(sp.nsimplify(tup[i]))

                else:
                    l.append(0)

            sols.append(tuple(l))

        return sols

# verifie si les solutions constituent un equilibre de NASH
    def isEquilibrium(self, solusI, solusJ):

        # si les solutions existent et sont positives
        if(solusI and solusJ and self.isPositive(solusI) and self.isPositive(solusJ)):

            # best response condition
            if(self.verifiesBRCond(solusI[0], solusJ[0])):

                # si la solution n'existe pas deja
                if([solusI[0], solusJ[0]] not in self.nashs):

                    self.nashs.append([solusI[0], solusJ[0]])

# verifie si la liste de  tuples ne contient pas de valeurs negatives
    def isPositive(self, solus):

        for tup in solus:
            for val in tup:
                if(val < 0):
                    return False

        return True

# verifies best response condition
    def verifiesBRCond(self, soluI, soluJ):

        maxSoluI, productsI = self.getMax(soluJ, self.a)

        maxSoluJ, productsJ = self.getMax(soluI, self.b)

        for i in self.elementI:

            if soluI[i - 1] > 0:

                if(sp.nsimplify(productsI[i - 1]) != sp.nsimplify(maxSoluI)):

                    return False

        for j in self.elementJ:

            if soluJ[j - 1] > 0:

                if(sp.nsimplify(productsJ[j - 1]) != sp.nsimplify(maxSoluJ)):

                    return False

        return True

# return the max of solu * A
    def getMax(self, solu, matrix):

        products = []

        for row in matrix:

            products.append(np.dot(row, solu))

        return max(products), products
