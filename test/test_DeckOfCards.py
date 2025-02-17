import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from DeckOfCards import DeckOfCards
from HandOfCards import HandOfCards

class TestDeckOfCards(unittest.TestCase):
    
    def setUp(self):
        # Opprett en ny kortstokk før hver test
        self.deck = DeckOfCards()
        
    def test_deck_initialization(self):
        # Test at en ny kortstokk inneholder 52 kort.
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_deck_str(self):
        # Test at __str__ returnerer en streng med 52 kort (forventet antall kommaer).
        deck_str = str(self.deck)
        # Dersom kortene er separert med ', ', skal det være 51 kommaer
        self.assertEqual(deck_str.count(','), 51)
    
    def test_deal_hand_valid(self):
        # Test at deal_hand returnerer en HandOfCards med korrekt antall kort.
        hand = self.deck.deal_hand(5)
        self.assertIsInstance(hand, HandOfCards)
        self.assertEqual(len(hand.cards), 5)
    
    def test_deal_hand_invalid(self):
        # Test at ugyldige input for deal_hand gir ValueError.
        with self.assertRaises(ValueError):
            self.deck.deal_hand(0)
        with self.assertRaises(ValueError):
            self.deck.deal_hand(53)

if __name__ == '__main__':
    unittest.main()
