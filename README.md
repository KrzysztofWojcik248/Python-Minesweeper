# Python-Minesweeper

This is my project about recreating minesweeper in python.


# My procject features:


-Choosing any size of map between 2x2 and 15x29

-Changable difficulty

-Random minesweeper expierience

-GUI created using TKinter
# How it works:

I used TKinter to make game-area. It is based on layers of interface elemenents placed on grid. Before the area generates, list of every square generates and every bomb is laid, then based on that list every square gets a name. Depending on the name or being a bomb, every square gets an icon which is covered by the next layer - blank buttons. You can interact with button by right-click or left-click and these mechanics are designed to match orignal game experience.
