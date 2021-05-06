# CSC520_Project
To run this project you will need to install pandas and pypng. You can do this by pip install pypng / pip install pandas.

To run the project you will need to modify the setup.txt file. The first line should be 'Y' or 'N', which will tell the program wheter or not you want it to be a 
randomly generated map or if you want to read in from a csv file. The next three lines represent the weights of each 'cost'. This will just be a multiplier between 0 and 1. 
The cost order is economic, social, environmental. So if you wanted them all weighted equally it would be as follows.  
1  
1  
1  
If you want environmental to be twice as important as the others you would do as follows.  
.5  
.5  
1  
The final line is optional for if you want to read the board in from a file. For example for our tests we used the file Board_Summary.csv. You can create your own csv file
to represent a board. Each row in the file represents the x coordinate, the y coordinate, and the terrain id for the tile at that postion.

The program should be executed from the main.py file. From the project directory run: python main.py

If you have any questions reach out to bjlayko@ncsu.edu
