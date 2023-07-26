from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight,AKnave), # A character can be either a knight or a knave
    Not(And(AKnave,AKnight)), # A character cannot be both a knight and a knave
    # A says "I am both a knight and a knave."
    Implication(AKnight,And(AKnave,AKnight)), # If A is a knight, that implies that A is both a knight and a knave
    Implication(AKnave,Not(And(AKnave,AKnight))) # A is a knave, that implies that a is not both a knight and a knave
    # TODO
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), # A can be either a knight or a knave
    Not(And(AKnave, AKnight)), # A cannot be both a knight and a knave
    Or(BKnave, BKnight), # B is either a knight or a knave
    Not(And(BKnave, BKnight)), # B cannot be both a knight and a knave
    # A says "We are both knaves."
    Implication(AKnight, And(AKnave, BKnave)), # If A is a knight, that implies that both A and B are knaves
    Implication(AKnave, Not(And(AKnave, BKnave))) # If A is a knave, that implies that both A and B are not knaves
    # TODO
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnave, AKnight), # A can be either a knight or a knave
    Not(And(AKnight,AKnave)),  # A cannot be both a knight and a knave
    Or(BKnave, BKnight), # B is either a knight or a knave
    Not(And(BKnave, BKnight)), # B cannot be both a knight and a knave
    # A says "We are the same kind."
    Implication(AKnight, And(And(AKnight, BKnight), And(AKnave, BKnave))), # If A is a knight, that implies that both A and B are the same kind
    Implication(BKnave, And(And(AKnight, BKnight), And(AKnave, BKnave))), # If B is a Knave, that implies that both A and B are the same kind
    
    # B says "We are of different kinds."
    Implication(AKnave,Not(And(And(AKnight, BKnight),And(AKnave, BKnave)))), # If A is a Knave, that implies that both A and B are different kinds
    Implication(BKnight, Not(And(And(AKnight, BKnight),And(AKnave, BKnave))))# If B is a knight, that implies that both A and B are different kinds
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight,AKnave)),
    Or(BKnave, BKnight),
    Not(And(BKnave, BKnight)),
    Or(CKnave, CKnight),
    Not(And(CKnight,CKnave)),
    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, AKnight), # If A says 'I am a Kight' then A is a knight
    Implication(AKnave, And(AKnight, AKnave)), # If A says 'I am a knave' then A is both a knight and a knave (Contradiction)
    # B says "A said 'I am a knave'."
    Implication(BKnight, AKnave),
    Implication(BKnave, Not(AKnave)),
    # B says "C is a knave."
    Implication(BKnight, CKnave), # If B is a knight, then C is a knave
    Implication(BKnave, Not(CKnave)), # If B is a knave, then C is a knight
    # C says "A is a knight."
    Implication(CKnight, AKnight), # If C is a knight then A is a knight
    Implication(CKnave, Not(AKnight)) # If C is a knave then A is not  knight
    # TODO
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
