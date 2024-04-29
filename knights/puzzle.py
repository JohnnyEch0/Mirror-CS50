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
    # TODO

    # BaseKnowledge
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(AKnight, AKnave),

    # specific Knowledge
    Implication(And(AKnight, AKnave), AKnight),
    Implication(Not(And(AKnight, AKnave)), AKnave),

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    # BaseKnowledge
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(AKnight, AKnave),

    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Or(BKnight, AKnave),

    # specific Knowledge
    Implication(And(AKnave, BKnave), AKnight),
    Implication(Not(And(AKnave, BKnave)), And(AKnave, BKnight))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    # BaseKnowledge
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(AKnight, AKnave),

    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Or(BKnight, BKnave),

    # specific Knowledge
    Implication(And(AKnave, BKnave), AKnight),
    Implication(And(AKnight, BKnight), AKnight),

    Implication(Not(And(AKnave, BKnave)), AKnave),
    Implication(Not(And(AKnight, BKnight)), AKnave),

    # B
    Implication(And(AKnave, Not(BKnave)), BKnight),
    Implication(And(AKnight, Not(BKnight)), BKnight),

    Implication(And(AKnave, BKnave), BKnave),
    Implication(And(AKnight, BKnight), BKnave),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    # BaseKnowledge
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(AKnight, AKnave),

    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight)),
    Or(BKnight, AKnave),

    Implication(CKnight, Not(CKnave)),
    Implication(CKnave, Not(CKnight)),
    Or(CKnight, AKnave),

    # specific knowledge



    Biconditional(CKnave, BKnight),  #B says "C is a knave."
    Biconditional(Not(CKnave), BKnave),

    Biconditional(AKnight, CKnight),  # C says "A is a knight."
    Biconditional(Not(AKnight), CKnave),


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
