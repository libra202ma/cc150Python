/*
Design a deck of cards that support shuffle and draw.
 */

enum Suit {...};
enum Value {...};

class Card {
private:
    Suit s;
    Value v;

public:
    Card(Suit s, Value v);
};

class DeckCards {
private:
    Card cards[52];
    int top; // indicate top of the deck
    int seed; // seed of random number generator

public:
    DeckCards(int seed);
    DeckCards() {
        top = 51;
        for (int s = 0; s < 4; s++) {
            for (int v = 0; v < 13; v++) {
                cards[s * 13 + v] = Card(s, v);
            }
        }
        shuffle();
    }

    Card draw() {
        return cards[top--];
    }

    void shuffle() {
        for (int i = 0; i <= top; i++) {
            int r = rand(0, i); // generate random numbers between 0 and i, inclusive
            swap(cards[i], cards[r]);
        }
    }
};
