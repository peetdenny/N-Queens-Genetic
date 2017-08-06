class Board:
    def __init__(self, initial_state):
        size = len(initial_state)
        if size < 4:
            print("N-Queens has no solution for board sizes smaller than 4x4. Please try a bigger board")
            exit(1)
        self.state = initial_state
        self.dimensions = (size, size)
        self.rows = {}
        self.cols = {}
        self.diagonals = {}

        def add_to_row(r, c):
            if r not in self.rows:
                self.rows[r] = []
            self.rows[r].append(c)

        def add_to_col(r, c):
            if c not in self.cols:
                self.cols[c] = []
            self.cols[c].append(r)

        def add_to_diag(r, c):
            pass

        for col, row in enumerate(initial_state):
            row = int(row)
            add_to_row(row, col+1) # TODO - No, there are diagonals all over the place! :(. Not just two.
            add_to_col(row, col+1)
            add_to_diag(row, col+1)

    def count_attacking_pairs(self):
        # rows - check if the same number appears more than once in config
        # cols - this configuration type doesn't allow attacking within a column
        # diags - check
        count = 0
        for row in self.rows:
            if len(self.rows[row]) > 1:
                count += len(self.rows[row])-1

        for col in self.cols:
            if(len(self.cols[col])) > 1:
                count += len(self.cols[col])-1

        return count
