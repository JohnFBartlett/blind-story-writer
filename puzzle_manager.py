

class Puzzle:
    """
    - title is the title of the puzzle; it's a string
    - blanks is a list of tuples which are (story_index, POS)
        - POS gets replaced by a word string when the blank is filled
    - story is a list of string tokens which make up the story
    """

    def __init__(self, title, blanks, story):
        self.title = title
        self.blanks = blanks
        self.story = story
        self.completed = False

    def fill_blank(self, blank_index, inpt):
        # note that the blank_index is the index within the
        # blank list, not in the story list
        blank = self.blanks[blank_index]
        blank[1] = input
        self.story[blank[0]] = "<"+inpt+">"


class PuzzleManager:

    def __init__(self, puzzles_list='games.txt'):
        self.puzzles = []
        with open(puzzles_list, 'r') as games_file:
            for line in games_file:
                if line.rstrip() != '':
                    title, story = line.split('\t')
                    puzzle = Puzzle(title, [], [])
                    for i, word in enumerate(story.split(' ')):
                        if '[' in word and ']' in word:
                            # it's a blank
                            puzzle.blanks.append([i, word[1:len(word)-1]])
                        puzzle.story.append(word)
                    self.puzzles.append(Puzzle(puzzle.title, puzzle.blanks, puzzle.story))

    def get_puzzle(self, number):
        return self.puzzles[number]
