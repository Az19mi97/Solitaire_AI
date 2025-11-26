from LogicDesign import GameLogic
from UserInterface import GameUI

gl = GameLogic()
gui = GameUI()
gui.focusOnEmulatorScreen()

while 1:
    #Program er i færd med at køre GameDesign klassen.
    print("Running LogicDesign class.")
    gui.UpdateGameState()

    #Nu forsøger programmet, at regne på spillet.
    print("Computing Operation class.")
    next_action = gl.GetNextAction(gui.gs, gui.gv)
    #print("Action: " + next_action.name)
    #print(next_action.cards)
    gui.ProcessAction(next_action)