# Game Theory App2
 A desktop app that determines some game theory's notions in mixed strategies games and **zero-sum** games

# Description

This second application considers two players games with a maximum of three strategies for each player. It allows to :

* Find all the pure and mixed strategy Nash equilibriums.
* Calculate the value in a **zero-sum** Game.


# Technologies
To run this app, install:

* Python 3.*
* PyQt5
* Itertools
* Numpy
* Sympy
* QDarkStyle : is a dark stylesheet for Python and Qt applications. 

# Usage

To lunch the application, run _**Application.py**_ file:

![interface](/README_images/app.png)

1. The user can change the strategies number for each player (maximum three strategies), which will update the payoffs matrix (add / remove rows or columns).

2. If the user checks the **_Zero-Sum Game_ box**, this will adapt the payoffs matrix to a **zero-sum** game.

3. The user must fill the payoffs matrix (He can also change the strategies names if desired).

4. The **_Reset Game_ button**  allows you to reset the game's parameters (the strategies number and payoffs matrix).

5) The **_Start Game_ button** validates the game's parameters entered beforehand and starts calculating Nash equilibriums.

6) In the case of a zero sum game, the user will be able to visualize Nash equilibriums and the value. Otherwise, only Nash equilibriums will be displayed.

7) This area displays the results of the calculations performed.

# Exemple

Let's consider the case of a non zero-sum game, where both players have three strategies, to which we match the payoffs table and results below.

![interface](/README_images/table.jpg)


Now let's move on to the case of a zero-sum game, where both players have three strategies.

![interface2](/README_images/table2.jpg)

![value](/README_images/value.jpg)
