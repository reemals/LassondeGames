# LassondeGames2020ProgrammingChallenge

Programming Challenge Starter Code README

## Initialization
Open the command prompt and locate the project folder location

Go to: _LassondeGames2020ProgrammingChallenge\Backend Module_
Run the following command: *npm install*

The installation should create the required node modules for the project to run

To run the code, from the directory _LassondeGames2020ProgrammingChallenge\BackendModule_ 
In the command prompt type: *node main.js*
Open _http://127.0.0.1:8081/_ in a web browser

### Java Front End Initialization (If coding in Java)
Create a Java project to hold the source code
Go to the downloaded files given and add the files from _LassondeGames2020ProgrammingChallenge\FrontEndDemoJava\src_ into the project src folder
Drag and drop both files: **MainClass.java** and **Request.java** into the src of your project

Left click on project folder and go to **Build Path**
Then go to **Configure Build Path**, then click on **Add External JARs…**
Once there, find the _JSON simple_ JAR that you should have downloaded previously (http://www.java2s.com/Code/Jar/j/Downloadjsonsimple11jar.htm) and add it.
Click **Apply and Close **
Finally, run the **MainClass.java** 

### Python Front End Initialization (If coding in Python)
Go to the following directory in your command prompt: _LassondeGames2020ProgrammingChallenge\FrontEndDemoPython_
Type the following command in:
**pip install requests**
**python mainClass.py**

## Function API
The following API requests can be made to interact with the simulation software:

**createInstance()**

This function MUST be the first connection to the simulation, it sets up the connection and allows for requests to be made
Return: This will return the base instance information, including data about the rocket

**getData()**

This function can be used to return significant information about the rocket and the elements within the space.

This return includes the following information:

_location:_ Current rocket location

_direction_: Current direction the rocket is facing

_finished:_ Has the rocket successfully landed on Mars

_timeSpent:_ Amount of time the rocket has taken so far on the trip

_fuelAmount:_ Amount of fuel the rocket currently has

_didYouGoBoom:_ If the rocket has exploded from a collision the mission has failed

_ROOM_DIMENSIONS:_ Constants depicting the size of the flyable space of the rocket

_mapData:_ Contains a JSON object with additional information

    -The location of Mars
    
    -The location of the two recharging stations
    
    -The location of all asteroids within the asteroid belt
    
**finish()**

This request will trigger the rocket to land, and is only successful when done at the location of Mars
This should be the final step in your journey and without it, there will be a point detriment

**turn(String direction)**

Direction must be one of the following "N", "S", "E", or "W"

There is a fuel and time cost associated with doing this. It costs 1 time and 1 fuel to do a successful turn regardless of direction and orientation. However, if you are currently facing a direction and attempt to turn to the same direction (ie currently N and turn N) there is no time or fuel loss of doing so

**move(int amount)**

This function will allow your rocket to move in the current direction it is facing.

The cost of any movement will be equal to the number of steps successfully moved. Please note that an error will be thrown if you attempt to move outside of the bounded space region, and no warning will be given about upcoming asteroids. Hitting an asteroid will cause your rocket to explode and your mission to fail.

**refuel()**

The refuel action can only be successfuly completed at the two recharge stations. The cost of refuelling is expensive and so should also be taken into account when optimizing your solution. The cost of refuelling is equal to the amount of fuel needed to reach max fuel within your ship, which is 30 units. For example, if you are currently at 12/30 fuel remaining, and you decide to refuel, the timeSpent will be incremented by 18. There is no way to stop the rocket from fully refuelling, so knowing when to refuel and when not to, could be a vital part of an ideal solution.

Also, it is important to note that running out of fuel will not result in the rocket exploding, nor will it stop the ability to move. However, you will go into the negatives, and doing so will result in an immediate point deduction regardless of how far into the negatives your rocket goes.

## Good luck on your mission!




