import minesweeper
cells = set( [(1,1), (2,2), (3,3)] )
count = 1
s1 = minesweeper.Sentence(cells,count)
print(s1.cells)