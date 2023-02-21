# Solve-the-Balls 
This is a web application developed to solve the **Ball Sort Puzzle**

The application was developed using: CSS, Django, HTML, JavaScript and Python

# Warning
As this program is developed using the backtracking algorithm, which is inefficient and might not be able to solve a few complicated puzzles. In such cases, an error ```RecursionError: maximum recursion depth exceeded in comparison``` might show up.
If this situation occur, please refresh your website, redirect to the home page, and set up a less complicated puzzle.

I know, it's disappointing! But it's the best solution I could do right now :(

# How to use the program

1. Access the website at http://k2nguyen.pythonanywhere.com
2. On the home page, select the desired tube size (In this example, I will choose 2) and click the **Save Tube Size** button
   
   _Question:_ What is tube size?
   
   _Answer:_ 
    - Tube size indicates the maximum number of balls that a tube may hold.
     
    - A tube is considered **completed** if the numbers of ball in the tube equal the tube size value that you set, and all of the balls in the tube have the same color.  
    
    - This information is crucial to the program to determine whether or not your game is solvable. Hence, please make sure you entered the correct tube size for your game
             
   **_IMPORTANT:_** You must click the **Save Tube Size** button, otherwise, the program will operate with the default tube size of 0, which might not always be suitable for your game
    
   _If you saved the tube size correctly, the tube size value would be updated on the line below the heading ("Tube Size: 2" is displayed in this example). Also, the dropbox value would be reset to 0 after you saved the tube size, DO NOT WORRY ABOUT IT!_
    
    <p align="center">
        <img width="471" alt="image" src="https://user-images.githubusercontent.com/75595156/212800316-cca4f90c-0060-4011-a1d2-7dd5b96f7022.png">
    </p>
  
3. Click the button **Add A Tube**
4. This button would take you to a page to add a new tube to the game
5. Select the number of balls you want for the tube (In this case, I chose 2)
6. Select the color for each balls and click **Submit** to save the tube <br/>
**_IMPORTANT:_** **Ball #1** denotes the ball at the **top of the tube**, and the **last ball** on the list would be the ball at the **bottom of the list.**
   
   Look at the below example for clarity
   
   <p align = "center">
    <img width="1405" alt="image" src="https://user-images.githubusercontent.com/75595156/212800819-d099ff17-f442-4eef-b9ed-701b82ae24a3.png">
   </p>
   
   <p align = "center">
      <img width="488" alt="image" src="https://user-images.githubusercontent.com/75595156/212800941-539d56fd-6ff6-4fe1-8e2d-632d5ad092a5.png">
   </p>
   
   Note how Ball #1 is set to the color Blue and the Blue ball is at the top of the list. Also, note how Ball #2 is set to the color Red, and the Red ball is at the bottom of the list
7. Repeat step 3 - 6 until you have reached the desired puzzle configuration. In this example, below is my puzzle configuration
   
   <p align = "center">
      <img width="517" alt="image" src="https://user-images.githubusercontent.com/75595156/212801406-077a4136-d5bb-4adf-8029-ae7ec61ca821.png">
   </p>
   
   
    **Note:** If you made a mistake when setting up the puzzle, please click the **Reset** button and restart the process.
8. Once you have finished setting up the puzzle, click the **Solve!** button to generate the solution for the puzzle
9. The **Solve** button would redirect you to the solution page (This could take one to a few minutes depends on the complexity of your puzzle)
10. If a solution does not exist, a text would be displayed indicating this condition. In such cases, please navigate back to the index page by clicking on the logo in the navigation bar and hit **Reset** and set up a new puzzle
11. If a solution exists, the program would display specific steps to solve the puzzle. Use the <img width="102" alt="image" src="https://user-images.githubusercontent.com/75595156/212802203-b70ae000-25ef-49d7-a7e3-015e1267e946.png"> buttons to navigates through these steps
12. Enjoy the satisfaction of solving the game! You did it! HAVE FUN!!!

   
   
