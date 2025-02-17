import unittest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):
    
    def test_valid_card(self):
        # Test at et gyldig kort opprettes riktig.
        card = PlayingCard('H', 7)
        self.assertEqual(card.get_suit(), 'H')
        self.assertEqual(card.get_face(), 7)
        self.assertEqual(card.get_as_string(), "H7")
    
    def test_invalid_suit(self):
        # Test at en ugyldig farge gir ValueError.
        with self.assertRaises(ValueError):
            PlayingCard('X', 7)
            
    def test_invalid_face(self):
        # Test at en ugyldig verdi gir ValueError.
        with self.assertRaises(ValueError):
            PlayingCard('H', 14)
            
    def test_equality(self):
        # Test at __eq__ fungerer ved å sammenligne like og ulike kort.
        card1 = PlayingCard('S', 12)
        card2 = PlayingCard('S', 12)
        card3 = PlayingCard('H', 12)
        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)
    
    def test_hash(self):
        # Test at hash-funksjonen fungerer, slik at like kort har samme hash.
        card1 = PlayingCard('C', 3)
        card2 = PlayingCard('C', 3)
        self.assertEqual(hash(card1), hash(card2))

if __name__ == '__main__':
    unittest.main()
