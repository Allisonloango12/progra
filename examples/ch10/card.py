# card.py
"""Card class that represents a playing card and its image file name."""
import random
import os

class Card:
    FACES = ['ace', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', 'jack', 'queen', 'king']
    SUITS = ['hearts', 'diamonds', 'clubs', 'spades']

   def _init_(self, face, suit):
        """Initialize a Card with a face and suit."""
        self._face = face
        self._suit = suit
        self.DECK = []


    @property
    def face(self):
        """Return the Card's self._face value."""
        return self._face

    @property
    def suit(self):
        """Return the Card's self._suit value."""
        return self._suit

    @property
    def image_name(self):
        """Return the Card's image file name."""
        return str(self).replace(' ', '_') + '.png'

    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}')"     

    def __str__(self):
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""
        return f'{str(self):{format}}'

    def generador_cartas(self):
        face = random.choice(Card.FACES)
        suit = random.choice(Card.SUITS)
        return Card(face,suit)
        
    def baraja_de_cartas(self, cantidad_cartas):
        for k in range(cantidad_cartas):
           card = self.generador_cartas()
           self.DECK.append(f"{card.face}_de_{Card.suit}")
        return self.DECK

    def iterador(self):
        for k in self.DECK:
           yield k

%matplotlib

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from pathlib import Path
path = Path('.').joinpath('card_images')

from deck import DeckOfCards
deck_of_cards = DeckOfCards()
deck_of_cards.shuffle()
#deck_of_cards.deal_card()

card = deck_of_cards.deal_card()
str(card)
card.image_name


#Muestra las cartas
figure, axes_list = plt.subplots(nrows=4, ncols=5)

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

figure.tight_layout()




##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
