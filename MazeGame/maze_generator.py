from random import randint

# working on bits, for example 10001 means the cell has been visited and has a path to north :)
north = 1
east = 2
south = 4
west = 8
visited = 16


def maze(width=10, height=10, display = False):
    Stack = []
    Maze = []
    for _ in range(height):
        Maze.append([0] * width)

    # generate starting point
    Stack.append((randint(0, height - 1), 0))
    Maze[Stack[-1][0]][Stack[-1][1]] = visited + west   # start
    Maze[randint(0, height - 1)][width - 1] += east     # end
    nrVisitedCells = 1

    while (len(Stack)):
        if nrVisitedCells < width * height:
            # creating a set of unvisited neighnours

            neighbours = []

            # north
            if Stack[-1][0] > 0 and Maze[Stack[-1][0] - 1][Stack[-1][1]] & visited == 0:
                neighbours.append(0)

            # south
            if Stack[-1][0] < height - 1 and Maze[Stack[-1][0] + 1][Stack[-1][1]] & visited == 0:
                neighbours.append(1)

            # east
            if Stack[-1][1] < width - 1 and Maze[Stack[-1][0]][Stack[-1][1] + 1] & visited == 0:
                neighbours.append(2)

            # west
            if Stack[-1][1] > 0 and Maze[Stack[-1][0]][Stack[-1][1] - 1] & visited == 0:
                neighbours.append(3)

            if len(neighbours) == 0:
                Stack.pop()
            else:
                i = neighbours[randint(0, len(neighbours) - 1)]  # chose a random neighbour
                if i == 0:
                    Maze[Stack[-1][0] - 1][Stack[-1][1]] += visited + south
                    Maze[Stack[-1][0]][Stack[-1][1]] += north
                    Stack.append((Stack[-1][0] - 1, Stack[-1][1]))
                elif i == 1:
                    Maze[Stack[-1][0] + 1][Stack[-1][1]] += visited + north
                    Maze[Stack[-1][0]][Stack[-1][1]] += south
                    Stack.append((Stack[-1][0] + 1, Stack[-1][1]))
                elif i == 2:
                    Maze[Stack[-1][0]][Stack[-1][1] + 1] += visited + west
                    Maze[Stack[-1][0]][Stack[-1][1]] += east
                    Stack.append((Stack[-1][0], Stack[-1][1] + 1))
                else:
                    Maze[Stack[-1][0]][Stack[-1][1] - 1] += visited + east
                    Maze[Stack[-1][0]][Stack[-1][1]] += west
                    Stack.append((Stack[-1][0], Stack[-1][1] - 1))

    ## add solution display to maze

    ############## display maze ####################
    if display:
        pathwidth = 3
        for _ in range(4 * width + 1):
            print('\033[91m' + "\u2588" + '\033[0m', end=" ")
        print()
        for x in range(height):
            for i in range(pathwidth):
                if Maze[x][0] & west:
                    print('\033[93m' + "\u2588" + '\033[0m', end=" ")
                else:
                    print('\033[91m' + "\u2588" + '\033[0m', end=" ")
                for y in range(width):
                    if Maze[x][y] & visited:
                        for i in range(pathwidth):
                            print('\033[93m' + "\u2588" + '\033[0m', end=" ")
                    else:
                        for i in range(pathwidth):
                            print('\033[92m' + "\u2588" + '\033[0m', end=" ")
                    if Maze[x][y] & east:
                        print('\033[93m' + "\u2588" + '\033[0m', end=" ")
                    else:
                        print('\033[91m' + "\u2588" + '\033[0m', end=" ")
                print()
            print('\033[91m' + "\u2588" + '\033[0m', end=" ")
            for y in range(width):
                for i in range(pathwidth):
                    if Maze[x][y] & south:
                        print('\033[93m' + "\u2588" + '\033[0m', end=" ")
                    else:
                        print('\033[91m' + "\u2588" + '\033[0m', end=" ")

                print('\033[91m' + "\u2588" + '\033[0m', end=" ")
            print()

    ################################################
    return Maze

#maze(2, 2, True)
