import sys

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        _, _, w, h = draw.textbbox((0, 0), letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for key, items in self.domains.items():
            items_to_remove = []
            for item in items:
                if len(item) != key.length:
                    items_to_remove.append(item)

            for wrong_word in items_to_remove:
                self.domains[key].remove(wrong_word)


        # revise test
        """
        words = []
        for variable in self.domains:
            words.append(variable)

        for i in range(5):
            print(self.revise(words[i], words[i+1]))
        """


    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        overlap = self.crossword.overlaps[x, y]
        if overlap is not None:
            words_remove = []
            for word in self.domains[x]:
                connection_found = False

                for wordy in self.domains[y]:
                    if word[overlap[0]] == wordy[overlap[1]]:
                        connection_found = True

                if connection_found == False:
                    words_remove.append(word)

            if words_remove is not None:
                for word_r in words_remove:
                    self.domains[x].remove(word_r)
                return True

        return False

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        # print(self.crossword.overlaps)
        count = 0

        if arcs == None:
            arcs = [arc for arc in self.crossword.overlaps if arc is not None]

        while arcs:

            try:
                x,y = arcs.pop(0)
            except IndexError:
                print("INDEXERROR",arcs)

            if self.revise(x, y):
                #print(self.domains[x])
                if len(self.domains[x]) == 0:
                    return False
                else:
                    # print(f"x neighbors are  {self.crossword.neighbors(x)}")
                    neighbors = [neighbor for neighbor in self.crossword.neighbors(x) if neighbor is not y]
                    for neighbor in neighbors:
                        arcs.append(   (neighbor, x)   )
                    # print(neighbors)

            """
            count +=1
            if count == 100:
                sys.exit("count 100, in dev")
            """
        return True


    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """
        # assignment is a dict of var:string
        # print(f"Debug, assignment(), asignment = {assignment}")
        for var in self.crossword.variables:
            try:
                if assignment[var] is None:
                    return False
            except KeyError:
                return False
        return True

    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        # all values are distinct
        # print(f"Debug, consistent(), asignment = {assignment}")
        values = set()
        for key, value in assignment.items():
            if value in values:
                return False
            values.add(value)

            # value has the correct length
            # print(f"Debug, consistent, {key}, {value}, len: {len(value)} , key.len: {key.length}")
            if len(value) != key.length:
                return False

        # no conflicts on intersecting variables
        if not self.check_intersections_consistent(assignment):
            return False

        return True

    def check_intersections_consistent(self, assignment):

        intersections = [arc for arc in self.crossword.overlaps if arc[0] in assignment and arc[1] in assignment]
        # print("Debug Intersections", intersections)

        while intersections:
            x,y = intersections.pop(-1)
            #print(f"x,y = {x,y}")
            #print(x, y)

            # print("debug overlaps", self.crossword.overlaps)
            overlap = self.crossword.overlaps[x, y]
            if overlap is None:
                continue
            else:
                pass  #print(overlap)
            # print(assignment[x], assignment[y], overlap)
            if assignment[x][overlap[0]] != assignment[y][overlap[1]]:
                return False

        return True




    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # TODO: Order.
        list = [word for word in self.domains[var]]


        def evaluate_word_outruling(wordx):
            neighbors = [neighbor for neighbor in self.crossword.neighbors(var)]
            conflict_count = 0

            for neighbor in neighbors:
                overlap = self.crossword.overlaps[var, neighbor]
                for wordy in self.domains[neighbor]:
                    # print(f"wordx = {wordx}, neighbor = {neighbor} , wordy = {wordy}, overlap = {overlap}")
                    if wordx[overlap[0]] != wordy[overlap[1]]:
                        conflict_count += 1
            return conflict_count


        list = sorted(list, key=evaluate_word_outruling)


        return list

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        # TODO: Try List.sorted()
        unass_vars = [var for var in self.domains if var not in assignment]
        # get lowest
        if not unass_vars:
            return None

        lowest_var = unass_vars[0]
        for var in unass_vars:
            if len(self.domains[var]) < len(self.domains[lowest_var]):
                lowest_var = var


        return lowest_var

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # print("backtrack called")
        if self.consistent(assignment) and self.assignment_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        if not var:
            return None

        for value in self.order_domain_values(var, assignment):
            assignment.update({var: value})
            result = self.backtrack(assignment)
            if not result:
                return None
            if self.consistent(result) and self.assignment_complete(result):
                return assignment
            del assignment[var]

        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
