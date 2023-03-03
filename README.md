# BTC-Price-Tracker

This Python script uses the tkinter and PIL libraries to display the current price of Bitcoin in US dollars on a GUI window. The script also uses the requests and json libraries to retrieve and parse data from a public API.

To use this script, make sure that you have installed the required libraries (tkinter, PIL, requests, and json) on your system.

The script works by first creating a GUI window using the tkinter library. The window has a title, dimensions, and background color, which can be customized as needed.

The script then defines a function called "btc" that retrieves the current price of Bitcoin in US dollars from a public API. It formats the price as a string and updates a label in the GUI window with the new value every second.

The script also defines the layout of the GUI window using frames and labels. It loads an image of the Bitcoin logo using the PIL library and displays it in the top left corner of the window. It also displays a title label and a price label using customized fonts and colors.

To run the script, simply execute it in a Python environment or IDE. The GUI window should appear and display the current price of Bitcoin in US dollars, which will be updated every second. You can customize the appearance of the window and the API endpoint used to retrieve the data by modifying the relevant code sections.
