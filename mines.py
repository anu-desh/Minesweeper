import tkinter as tk
import random
import tkinter.messagebox
import os,sys

#contains mine location
s = set()
# main window
win = tk.Tk()
win.title("Mines")

board = [[None]*8 for _ in range(8)]
cell = [[None]*8 for _ in range(8)]
visited = [[False]*8 for _ in range(8)]


# placement of mines
while(len(s)<10):
    x = random.randint(0,63)
    board[x//8][x%8] = '*'
    s.add(x)

# for i in board:print(i)
#updating mine neighbours
def increment_neighbours(m,n):
    for x in range(m-1,m+2):
        for y in range(n-1,n+2):
            if(x<8 and x>=0 and y<8 and y>=0):
                if board[x][y] != '*':
                    if board[x][y] is None:
                        board[x][y] = 1
                    else:
                        board[x][y] += 1

# calculating mines
for i in range(8):
    for j in range(8):
        if(board[i][j] == '*'):
            increment_neighbours(i,j)

def flag(r,c):
    def right(event):
        if visited[r][c] == False:cell[r][c].config(text ='|>')
    cell[r][c].bind('<Button-3>',right)

#creates a grid
for r in range(8):
    for c in range(8):
        m = 0
        cell[r][c] = tk.Button(win,text =" ",bg="grey",height=3,width=6,command=lambda x=r,y=c:open(x,y))
        cell[r][c].grid(row = r,column= c)
        flag(r,c)

def bfs(r,c):
    q = [(r,c)]
    while(len(q) != 0):
        temp = q.pop(0)
        cell[temp[0]][temp[1]].config(text = board[temp[0]][temp[1]],bg="white")
        visited[temp[0]][temp[1]] = True

        x = [0,-1,0,1,1,-1,1,-1]
        y = [1,0,-1,0,1,-1,-1,1]

        for m,n in zip(x,y):
            i = temp[0]+m
            j = temp[1]+n
            if(i<8 and i>=0 and j<8 and j>=0):
                #if(board[i][j] == "|>"):board[i][j] = ""
                cell[i][j].config(text = board[i][j],bg="white")
                visited[i][j]=True
                if(board[i][j] is None and not visited[i][j]):
                    q.append((i,j))
                # if(not visited[i][j]):
                #     print(board[i][j])

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#function to open a cell
def open(r,c):
    m = 0
    if(board[r][c] is None):
        bfs(r,c)
    else:
        cell[r][c].config(text = board[r][c],bg="white")
        if(board[r][c] == "*"):
            result = tkinter.messagebox.askquestion("Game over","You Lost!, Do you want to restart the game?")
            if result == "yes":
                restart_program()
            else:
                win.destroy()
    visited[r][c] = True
    
    for i in visited:
        # print(i)
        for j in i:
            if j is False:
                m+=1
    # print(m)
    
    if m == 10:
        won = tkinter.messagebox.askquestion("YOU WON!!","Play again?")
        if won == "yes":
            restart_program()
        else:
            win.destroy()
        
win.mainloop()