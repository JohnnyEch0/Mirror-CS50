import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count
        self.mines = set()
        self.safes = set()

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """

        """ BUG:( Sentence.known_mines returns mines when conclusions possible
            expected "{(0, 1), (2, 3...", not "set()"
        """
        

        return self.mines


    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """

        """ BUG:( Sentence.known_safes returns mines when conclusion possible
            expected "{(0, 1), (2, 3...", not "set()"
        """
        if self.count == 0:
            return self.cells
        return self.safes


    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.mines.add(cell) #TODO: Dont know if this is necessary
            self.cells.remove(cell)
            self.count -= 1


    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.safes.add(cell)  #TODO: Dont know if this is necessary
            self.cells.remove(cell)



class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of ms about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.
        Gets a move ( the safe cell)
        and a count of nearby mines.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """


        """
            BUG:( MinesweeperAI.add_knowledge adds sentence in corner of board
            did not find sentence {(2, 3), (2, 4), (3, 3)} = 1
        """

        """
            BUG: :( MinesweeperAI.add_knowledge can infer mine when given new information
            expected "{(3, 4)}", not "set()"
        """

        """
            BUG: :( MinesweeperAI.add_knowledge combines multiple sentences to draw conclusions
            did not find (1, 0) in mines when possible to conclude mine
        """

        """
        1) + 2) mark cell as move and safe.
        """
        self.moves_made.add(cell)

        self.mark_safe(cell)

        """
        3) adda new sentence to knowledge
        a) grab all sourounding cells, that are not out of bounds
        """

        cells = set()

        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue
                """ BUG: maybe we shouldnt do this (or at least not here...)
                if (i,j) in self.safes:
                    continue
                """

                if (i, j) in self.mines:
                    count -= 1
                    continue
                

                # ignore out of bounds cells
                if i >= self.width or j >= self.height or i < 0 or j < 0:
                    continue
                else:
                    cells.add((i,j))

        # put them in a statement like {D,E;G} = 1
        if cells is not None:
            self.knowledge.append(Sentence(cells=cells, count=count))

        """
        4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
        """


        """knowledge processing"""

        while True:
            knowledge_changed = False

            for sentence_ in self.knowledge:

            # any sentence with a length of cells equal to its count is full of mines!
                if sentence_.count == len(sentence_.cells):
                    mine_cells = []
                    for cell in sentence_.cells:
                        mine_cells.append(cell)
                    
                    # mark the cells as bombs
                    for cell in mine_cells:
                        self.mark_mine(cell)

                    knowledge_changed = True

                # any sentence with a count 0 is fully safe :)
                elif sentence_.count == 0:
                    safe_cells = []
                    for cell in sentence_.cells:
                        safe_cells.append(cell)
                        # RuntimeError with the set being changed during iteration

                        
                        # TODO: do We Have to remove the sentence?

                    # Mark the cells as safe
                    for cell in safe_cells:
                        self.mark_safe(cell)

                    knowledge_changed = True


                """
                # filter out empty sentences
                if len(sentence_.cells) == 0:
                    self.knowledge.remove(sentence_)
                    
                """


                """ Check for conclusions based on subsets"""
                for sentence_2 in self.knowledge:
                    # ignore empty sentences
                    if len(sentence_2.cells) == 0:
                        continue

                    # ignore same sentences
                    if sentence_2 == sentence_:
                        continue


                    
                    if sentence_.cells.issubset(sentence_2.cells):
                        if self.subsentence_processing(sentence_, sentence_2) == 0:
                            knowledge_changed = True

                    
                    elif sentence_2.cells.issubset(sentence_.cells):
                        if self.subsentence_processing(sentence_2, sentence_) == 0:
                            knowledge_changed = True

                    
            # process known safes and known mines
            for cell in self.safes:
                for sentence in self.knowledge:
                    if cell in sentence.cells:
                        sentence.cells.remove(cell)
            
            for cell in self.mines:
                self.mark_mine(cell)

                
            # break if no new knowledge could be created
            if knowledge_changed == False:
                    break


    def subsentence_processing(self, s1, s2):
        """ Takes 2 Sentences where s1 is subset of s2, inferes new knowledge."""
        cells = set()

        # get every cell in S2 which isnt in S1.
        for cell in s2.cells:
            if cell not in s1.cells:
                cells.add(cell)
        
        nu_count = s2.count + s1.count

        breakp = False
        for sentence in self.knowledge:
            if sentence.cells == cells and sentence.count== nu_count:
                return 1 
        
        self.knowledge.append(Sentence(cells=cells, count=nu_count))
        return 0



    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """


        """
        BUG:( MinesweeperAI.make_safe_move makes safe move when possible
        move made not one of the safe options
        """
        # remove done moves from the safe cells we know about and convert to list
        safes_ls = [cell for cell in self.safes if cell not in self.moves_made]

        try:
            return random.choice(safes_ls)
        except IndexError:
            return None


    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        board = set()
        for i in range (self.width):
            for j in range(self.height):
                if (i, j) in self.moves_made:
                    continue
                elif (i, j) in self.mines:
                    continue
                else:
                    board.add((i,j))

        
        try:
            return random.choice(list(board))
        except IndexError:
            return None

    def clean_sentences(self, cell, type="safe"):
        """ This function takes a cell and a type safe/mine and updates all sentences in the knowledge
            However i think this is already done by the mark_sfe and mine methods...
        """


        for sentence in self.knowledge:
            if cell in sentence.cells:
                sentence.cells.remove(cell)
                if type == "mine":
                    sentence.count -= 1
            else:
                sentences_no_update += 1 #TODO: maybe we can return this value at some point to stop a while true loop?

        if sentences_no_update == len(self.knowledge):
            return 1 #return that nothing got changed
