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

        # Iterate over all variables
        for key in self.domains.keys():
            remove = [] # List of words to remove
            for word in self.domains[key]: # for each word in the domain
                if len(word) != key.length:
                    remove.append(word) # word is not node consistent
            for word in remove: # remove node inconsistent words
                self.domains[key].remove(word) #
        
        return


    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """

        overlap = self.crossword.overlaps[x, y] # Get the overlap

        if overlap is None: # If they don't overlap, return False
            return False
        
        i, j = overlap[0], overlap[1] # Get the indices of the overlap
        remove = [] # List of words to remove

        for word_x in self.domains[x]: # for each word in the domain x
            for word_y in self.domains[y]: # for each word in the domain y
                if word_x[i] == word_y[j]:
                    break # if the words overlap, break

                remove.append(word_x) # add the word to the list of words to remove
                
        for word in remove: # remove the words
            self.domains[x].remove(word)

        return True


    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        
        queue = [] # List of arcs to check

        if arcs is None: # no arcs given
            for x in self.domains.keys():
                for y in self.domains.keys():
                    if x != y:
                        queue.append((x, y)) # add all arcs to queue
        
        if arcs is not None: # arcs given
            for arc in arcs:
                queue.append(arc) # add all arcs to queue
        
        while queue is not None: # while there are arcs to check
            for x, y in queue: 
                arc = (x, y) # get an arc
                break

            if arc is not None:
                x, y = arc[0], arc[1] # get the variables
    
                if self.revise(x, y): # if the arc is revised
                    if len(self.domains[x]) == 0: # if the domain is empty
                        return False
                    
                    for z in self.crossword.neighbors(x): # for each neighbor of x
                        if z != y:
                            queue.append((z, x)) # add the arc to the queue
            break

        return True
    

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        for key in self.domains.keys(): # for each variable
            if key not in assignment.keys() or assignment[key] is None:
                # if the variable is not in the assignment or the value is None
                return False
        
        return True # if all variables are in the assignment


    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """

        values = [] # List of values in the assignment
        for key, value in assignment.items(): 
            # for each variable and value in the assignment
            if value in values: 
                # false if the value is already in the list of values
                return False

            if key.length != len(value): 
                # false if lengths are not equal
                return False
            
            values.append(value) # add the value to the list of values
            neighbours = self.crossword.neighbors(key) # get variable's neighbours
            
            for neighbour in neighbours: 
                # for each neighbour
                overlap = self.crossword.overlaps[key, neighbour] # get overlap
                
                if neighbour in assignment: 
                    # if the neighbour is in the assignment
                    if assignment[neighbour][overlap[1]] != value[overlap[0]]:
                        # if the overlap is not consistent
                        return False
            
        return True # if all values are consistent


    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        raise NotImplementedError


    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        raise NotImplementedError


    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """

        if self.assignment_complete(assignment):
            # if the assignment is complete, return the assignment
            return assignment
        

        

        
        raise NotImplementedError


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
