# MaGame

MaGame is a package currently involving two maze games: Mappy and Pac-man. In the game Mappy, a mouse cop is searching for the criminal cat in the maze, while in the other game Pac-man, the character is trying to eat all dots in the maze. 
<br/><br/>

<div style='height: 250px; width: 450px;display:table-cell;vertical-align: middle'>
<img src="https://github.com/XiongPengNUS/test/blob/master/mappy1.gif?raw=true" width=400px style="float:left"/>
</div>

<div style='height: 250px; width: 450px;display:table-cell;vertical-align: middle'>
<img src="https://github.com/XiongPengNUS/test/blob/master/pacman1.gif?raw=true" width=400px style="float:left"/>
</div>

<br/><br/>
Once you installed the package with the <code>pip</code> command, you may follow steps below to run the game. 
**Step 1: import the game and mazes from the MaGame package**


```python
from magame import mappy    # Import the Mappy game
from magame import pacman   # Import the Pac-man game
from magame import mazes    # Impor the pre-defined mazes
```

    pygame 2.0.0.dev6 (SDL 2.0.10, python 3.7.4)
    Hello from the pygame community. https://www.pygame.org/contribute.html


The variable <code>mazes</code> is a tuple, containing four nested lists representing the mazes, where:
- Maze wall is indicated by "1".
- Open path is indicated by "0".
- The target in the Mappy game is indicated by "-1". It is treated as "0" in the Pac-man game.

One example is given below, and you may create your own maze following the same format. 


```python
mazes[0]
```




    [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
     [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
     [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 1, 0, 1, 1, 0, 1, 1, 1, 0],
     [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
     [1, 1, 0, 0, 0, 1, 0, 0, -1, 1]]



**Step 2: create your own function that determines the movement in the maze**

The user-defined function must follow the format below.


```python
def maze_move(maze, position, memory):
    
    """
    Your code here
    """
    
    return move, memory
```

The input arguments of the function are:
- <code>maze</code> as a nested list representing the maze.
- <code>position</code> is a <code>tuple</code> with two integers: <code>h_index</code> and <code>v_index</code>. The first integer <code>v_index</code> indicates the horizontal index, and the second integer <code>v_index</code> indicates the vertical index, as shown by the picture below.
- <code>memory</code> can be any data type. Users may use it to keep a track of all previous steps or previous moves. The initial value of memory is given as <code>None</code>.

The outputs are:
- <code>move</code> is a <code>tuple</code> with two integers: <code>h_move</code> and <code>v_move</code>. It is used to indicate how the character moves in the maze, as shown by the following picture. 
- <code>memory</code> is the updated memory, such as all previous steps or previous moves of the character in the maze. 

<img src="https://github.com/XiongPengNUS/test/blob/master/Screen%20Shot%202020-07-25%20at%2011.57.26%20PM.png?raw=true" width=650>

The function receives the maze information, the current position in the maze, and previous step, moves, or other forms of memory; then decide the next move and update the memory. 

**Step 3: apply your function to play the game**

The game can be played by simply calling the <code>play()</code> function of the <code>mappy</code> or <code>pacman</code> 


```python
mappy.play(maze, maze_move)
pacman.play(maze, maze_move)
```

There are two input arguments for the <code>play()</code> function:
- <code>maze</code> is the nested list as the maze information.
- <code>maze_move</code> is the name of the function you created. It can be any valid Python function name. 

If your function works correctly, you will find the character moving in the maze.
