# CS-515_Project-2_Adventure_game


# Personal information
NAME : Girish Sai Varma Penumathsa

STEVENS LOGIN: ["gpenumat@stevens.edu"]

participant Members:Single




##  Repository URL
https://github.com/girishsaivarma/Project-2





##  Time Spent

I spent approximately 23 hours on the project. 





## Description of how you tested your code:

I tested the code by running it with various map files to ensure that it loads the map correctly.
I tested each command ('go', 'look', 'get', 'drop', 'inventory', 'help', 'quit') to ensure they produce the expected behavior.
I provided input variations and checked for error handling, such as entering invalid commands or incorrect file paths.





##  Bugs or issues you could not resolve:

The code seems well-structured, and I don't see any major bugs.





##  Example of a difficult issue or bug and how you resolved it:

One potential difficult issue could be handling unexpected user input. For instance, if a user enters a command that is not recognized or if the input format is incorrect. In such cases, I added appropriate checks and error messages to guide myself in vscode and project questions given by you.





##  List of extensions implemented with appropriate details:



 * Abbreviations for Verbs, Directions, and Items
   
Implemented abbreviations for verbs, directions, and items.
For example, 'go n' could be accepted as an abbreviation for go north etc but it should only work when unambiguous.
Considered potential ambiguity scenarios and ensured that abbreviations are only accepted when they have a clear interpretation.





* Help Verb:

Added a 'help' verb to the game.
When the player enters 'help,' the game provides information about the valid verbs. It helps players keep track of available commands.
Specifically, the help message lists the valid verbs and indicates those that expect a target 






* Drop Verb:

Implemented a 'drop' verb in addition to the existing 'get' verb.
The 'drop' verb allows the player to take an item from their inventory and place it in the current room.
Ensured that the 'drop' verb only works with items that the player already has in their inventory.
Like the 'get' verb, 'drop' considers the potential presence of multiple items with similar names and handles such scenarios appropriately.




















