"""
Maze Solver

This script uses a recursive algorithm to solve mazes.
"""
import csv
import os
import sys
import time
import random

def get_maze(file):
    f = open(file,'r')
    reader = csv.reader(f)
    maze = []
    for line in reader:
        maze.append(line)
    return maze

def display_maze(m, path):
    m2 = m[:]
    os.system('cls')

    for item in path:
        m2[item[0]][item[1]] = "🟩"

    m2[path[-1][0]][path[-1][1]] = "🐭"

    draw = ""

    for row in m2:
        for item in row:
            item = str(item).replace("1","⬜")
            item = str(item).replace("0","⬛")
            item = str(item).replace("2","🟥")
            item = str(item).replace("A","🟩")
            item = str(item).replace("B","🧀")
        
            draw += item
        draw += "\n"
    print(draw)
        
def move(path):
    time.sleep(0.2)
    cur = path[-1]
    display_maze(maze, path)
    possibles = [(cur[0], cur[1] + 1), (cur[0], cur[1] - 1), (cur[0] + 1, cur[1]), (cur[0] - 1, cur[1])]
    random.shuffle(possibles)

    for item in possibles:
        if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
            continue
        elif maze[item[0]][item[1]] in ["1","2"]:
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == "B":
            path = path + (item,)
            display_maze(maze,path)
            input("Cheese found!")
            os.system('clear')
            sys.exit()
        else:
            newpath = path + (item,)
            move(newpath)
            maze[item[0]][item[1]] = "2"
            display_maze(maze,path)
            time.sleep(0.2)

maze = get_maze('SelfSolvingMaze\Maze.csv')

move(((1,0),))