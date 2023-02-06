# potential-field-method
This project is for solve problem of local minimums in  the potential field method. 

On branch "dev" is implemented classic potential field method without solve problem of local minimum.

On  branch "book_solver"  is implemented method with 'trace of path'. The main thing in this method is leave positive charg in last "n" positions. 
The force of this  charges increse with evry move 10%  and it disappery after 6 steps. Thanks of this 
field configuration has gona changed and witch allows avoid minimum.


On branch "book_solver2" is implemented method with "additional negative charges". When minimum is deteced the force of the main goal is desactive on "n" steps. 
After this is  add tepmorary target on a straight line perpendicular to the line on which he retreated and again after "n" steps new target is added but in this case the line
should goes through the point witch minumum was detected. After "n" steps the main target is active agian.

This methods have implemented and tested in ROS. My prestntations form study classes and tests in ROS you can see in this link: 

Technology:
Python, ROS, Matplotlib


Execute:
Just clone repository and move to choose branch. Run "python main.py" command in console.
You can see the path of the robot on green points, obstacles as red points and target as blue point.



