# AdventOfCode
Solutions for [advent of code](https://adventofcode.com)

### Structure
Each solution is contained in `AOC-<YEAR>/day<N>/[1/2]`.
Each solution should have the following files:
- `input.txt` Input provided by AOC
- `main.py` The main python file, containing (in most cases) 
a print statement with the printed out solution as a comment at the bottom
- `puzzle.md` A copy of the puzzle description copied from AOC
- (optional) other files related to solving the puzzle 

Solutions should usually be pushed to GitHub the same or next day.

Although some inputs would be made easier to read if they had some manual 
preprocessing or some steps in the solution could be simplified if a human 
did that step, I try to not add any human work except for maybe removing a ".0"
from the solution if it is a float.

Each solution's `main.py` should include a commented out section near the top where
the example data is provided, with its respective solution as a comment on top of that.