# DMPROJECT: Fibonacci and Catalan Paths on a Wall

    <p align="center">
      <img src="https://raw.githubusercontent.com/burakyalcin10/DMPROJECT/main/images/fibonacci.jpg" alt="Fibonacci Path" width="400"/>
      <img src="https://raw.githubusercontent.com/burakyalcin10/DMPROJECT/main/images/walltilling.jpg" alt="Wall Tiling" width="400"/>
    </p>

    <p align="center">
      <img src="https://raw.githubusercontent.com/burakyalcin10/DMPROJECT/main/images/dyckpath.jpg" alt="Dyck Path" width="400"/>
      <img src="https://raw.githubusercontent.com/burakyalcin10/DMPROJECT/main/images/motzkin.jpg" alt="Motzkin Path" width="400"/>
    </p>

    This repository contains the code and resources for a combinatorial study of lattice paths constrained by a wall. The project explores the connections between these paths and classical sequences such as Fibonacci, Catalan, and Motzkin numbers.

    ## Overview

    This project uses Python-based algorithms and visualizations to analyze lattice paths systematically. It incorporates generating functions, kernel methods, and combinatorial mappings to provide both visual demonstrations and computational insights. The goal is to bridge theoretical enumeration with practical modeling in discrete mathematics and algorithmic design.

    ## Key Features

    - **Path Generation:** Algorithms to generate lattice paths with specific movement rules (N, S, E1, E2) constrained by a wall.
    - **Path Transformation:** Scripts to transform generated paths into Dyck and Motzkin paths.
    - **Generating Functions:** Implementation of generating functions to enumerate paths and analyze their combinatorial properties.
    - **Kernel Method:** Application of the kernel method to solve recurrence relations arising from generating functions.
    - **Visualizations:** Tools to visualize wall tilings, lattice paths, Dyck paths, and Motzkin paths.
    - **Exploration of Alternate Grids:** Preliminary work on paths in parallelogram and 3D grids.

    ## Project Structure

    ```
    DMPROJECT/
    ├── 3dGridwithPath.py
    ├── altıgenUcgenGridMove.py
    ├── convert_to_dyck.py
    ├── convert_to_motzkin.py
    ├── decompositionFromGeneratingFunction.py
    ├── draw_wall_tiling.py
    ├── fibonnaci_paths.py
    ├── parallelogramGridMove.py
    ├── randommixed.py
    ├── randomParallelogramGridMove.py
    ├── README.md
    └── images/
        ├── 3dpath.jpg
        ├── decomposition.jpg
        ├── dyckpath.jpg
        ├── fibonacci.jpg
        ├── motzkin.jpg
        ├── parallelogram.png
        └── walltilling.jpg
    ```

    - **Python Scripts:**
        - `3dGridwithPath.py`: Generates and visualizes random paths on a 3D grid.
        - `altıgenUcgenGridMove.py`: Draws paths on a hexagonal grid.
        - `convert_to_dyck.py`: Transforms lattice paths into Dyck paths.
        - `convert_to_motzkin.py`: Transforms lattice paths into Motzkin paths.
        - `decompositionFromGeneratingFunction.py`: Implements generating functions for path enumeration.
        - `draw_wall_tiling.py`: Creates a wall tiling grid for path visualization.
        - `fibonnaci_paths.py`: Generates Fibonacci-style lattice paths.
        - `parallelogramGridMove.py`: Visualizes paths on a parallelogram grid.
        - `randommixed.py`: Generates and visualizes random Catalan paths.
        - `randomParallelogramGridMove.py`: Generates random paths on a parallelogram grid.
    - **`images/`:** Contains images used in the README and the paper.

    ## Getting Started

    To run the Python scripts, you need to have Python 3.6 or higher installed. You can execute the scripts directly using the Python interpreter.

    ```bash
    python3 <script_name>.py
    ```

    ## Usage

    Each script is designed to perform a specific task, such as generating paths, transforming them, or visualizing them. You can modify the parameters within the scripts to explore different path configurations and grid sizes.

    ## Contributing

    Contributions to this project are welcome. If you have any suggestions or improvements, feel free to submit a pull request.

    ## License

    This project is licensed under the MIT License.

    ## Team

    - Elif Buse Cinar
    - Musa Talat Demir
    - Burak Yalcin
    - Mustafa Guvez
    - Yahya Efe Kurucay
    - Hüseyin Bardakci

    ## Acknowledgements

    This project was supported by the Department of Computer Science at Akdeniz University.
