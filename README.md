# Basic-Travel-Form-Tkinter

This is a simple travel form GUI application created using Python's tkinter module. 
The application allows users to enter their travel details, such as Name, Email, Phone, Address, and select their Gender. 
The entered information can be submitted, and it is saved to a text file named "data.txt" for future reference.


Here are the steps for the provided code:

Import the tkinter module to create a graphical user interface (GUI).
Create the main window using Tk() and set its title and initial size.
Set the background color of the window to "#ba7d99".
Create a label to display the heading "Dance Form" at the top of the window.
Create labels and entry widgets for capturing user information such as Name, Email, Phone, and Address.
Create variables (StringVar and IntVar) to store the values entered by the user in the entry widgets.
Create checkbuttons for capturing the user's gender selection.
Define the submit() function to display and store the user-entered information.
When the user clicks the "Submit" button, the submit() function is called.
The submit() function retrieves the values from the entry widgets and prints them on the console.
It also opens a file named "data.txt" in append mode, truncates the file to remove previous content, and writes the user information into the file, each value on a new line.
Create a "Submit" button that calls the submit() function when clicked.
Start the GUI event loop using window.mainloop() to handle user interactions and keep the window open until it is manually closed.
