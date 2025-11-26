import os

class GameVals: #Values
    cards = {}
    sliced_cards = {}
    borders = []

    # Variables related to screen size
    ScreenSize = "FullScreen"

    def __init__(self):

        if self.ScreenSize == "FullScreen":
            self.imageFolderName = 'card'
            self.drawDeckArea = [300, 50, 800, 300]
            self.deckArea = [850, 50, 1600, 300]
            self.columnsStart = 325
            self.columnWidth = 175
            self.columnOffset = 182

        for i in range(1, 5):
            borderName = 'border' + str(i) + '.png'
            self.borders.append(borderName)

        for i in range(1, 14):
            for ch in ['c', 'd', 'h', 's']:
                card = ch + str(i)
                cardpath = os.path.join(os.getcwd(), self.imageFolderName, card + '.png')
                sliceCardPath = os.path.join(os.getcwd(), self.imageFolderName, 'parts', card + '.png')
                self.cards[card] = cardpath
                self.sliced_cards[card] = sliceCardPath

class GameState:    #GameDesign
    deck_cards_top = []
    draw_deck_top_card = []
    column_cards = []
    new_cards_in_column = []
    column_all_cards = []
    empty_column_indices = []

    ui_components_to_render = {}
    def __init__(self):
        self.ui_components_to_render['draw_deck'] = []
        self.ui_components_to_render['top_deck'] = []
        self.ui_components_to_render['columns'] = [1,2,3,4,5,6,7]
        return

class Action:  #Operation
    name = ''
    cards = []

    def __init__(self):
        self.name = ''
        self.cards = []

class Card: #CardExertion
    name = ''
    path = ''
    cost = 1
    pos = []

    def __init__(self):
        name = 'test1'