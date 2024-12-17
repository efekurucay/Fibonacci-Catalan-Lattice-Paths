import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_3d_path(grid_size=20, path_length=50):
    # Seed for randomness
    np.random.seed(None)  # Different random path in each run
    
    # Starting point 0,0,0,0
    path_x = [0]
    path_y = [0]
    path_z = [0]
    
    # Follow the visited points
    visited = set([(0,0,0)])
    
    for _ in range(path_length):
        # Calculate neighbour coordinates (direct neighbours only)
        candidates = [
            (path_x[-1]+1, path_y[-1], path_z[-1]),   # Right
            (path_x[-1]-1, path_y[-1], path_z[-1]),   # Left
            (path_x[-1], path_y[-1]+1, path_z[-1]),   # Up
            (path_x[-1], path_y[-1]-1, path_z[-1]),   # Down
            (path_x[-1], path_y[-1], path_z[-1]+1),   # Forward
            (path_x[-1], path_y[-1], path_z[-1]-1)    # Backward
        ]
        
        # Find points within grid boundaries and unvisited points
        valid_moves = [
            (x,y,z) for x,y,z in candidates 
            if (0 <= x < grid_size and 
                0 <= y < grid_size and 
                0 <= z < grid_size and 
                (x,y,z) not in visited)
        ]
        
        # If there is nowhere to move, stop.
        if not valid_moves:
            break
        
        # Randomly select the next point
        next_x, next_y, next_z = valid_moves[np.random.randint(len(valid_moves))]
        
        # Add to path
        path_x.append(next_x)
        path_y.append(next_y)
        path_z.append(next_z)
        visited.add((next_x, next_y, next_z))
    
    # Visualisation
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Drive path
    ax.plot3D(path_x, path_y, path_z, color='black', marker='o')
    
    # Start and end points
    ax.scatter(path_x[0], path_y[0], path_z[0], color='green', s=200, label='Başlangıç')
    ax.scatter(path_x[-1], path_y[-1], path_z[-1], color='red', s=200, label='Bitiş')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Path on 3D Grid')
    plt.legend()
    plt.show()

generate_3d_path()