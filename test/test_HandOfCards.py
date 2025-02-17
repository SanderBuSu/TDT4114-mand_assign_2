import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from PlayingCard import PlayingCard
from HandOfCards import HandOfCards

class TestHandOfCards(unittest.TestCase):
    
    def setUp(self):
        # Oppretter en liste med kort for testing:
        # 5 Hjerter-kort for en flush
        self.cards_flush = [PlayingCard('H', i) for i in range(1, 6)]
        # En hånd med blandede farger
        self.cards_not_flush = [
            PlayingCard('H', 1),
            PlayingCard('S', 2),
            PlayingCard('H', 3),
            PlayingCard('H', 4),
            PlayingCard('H', 5)
        ]
    
    def test_is_flush_true(self):
        # Test at is_flush returnerer True for en flush (alle kort har samme farge).
        hand = HandOfCards(self.cards_flush)
        self.assertTrue(hand.is_flush())
        
    def test_is_flush_false_due_to_mixed_suits(self):
        # Test at is_flush returnerer False når kortene ikke alle er av samme farge.
        hand = HandOfCards(self.cards_not_flush)
        self.assertFalse(hand.is_flush())
    
    def test_is_flush_false_if_less_than_5(self):
        # Test at is_flush returnerer False dersom hånden inneholder færre enn 5 kort.
        hand = HandOfCards(self.cards_flush[:4])
        self.assertFalse(hand.is_flush())
    
    def test_str_method(self):
        # Test at __str__ returnerer en riktig formatert streng.
        hand = HandOfCards(self.cards_flush)
        expected = ', '.join(card.get_as_string() for card in self.cards_flush)
        self.assertEqual(str(hand), expected)

if __name__ == '__main__':
    unittest.main()
