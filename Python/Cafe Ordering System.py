#Cafe Au Lait Coffee Order System
#Computer Science 2017
#Jai Castle
# Program to create a visual interface for a cafe ordering system

#Library import & fundamental setup
from tkinter import * #GUI elements
import time
prices = {}#Library to store the product names and their prices.

#Prices and product declaration. Products will be listed in the order shown here.
prices['Cappuccino'] = 3.00
prices['Espresso'] = 2.25
prices['Latte'] =  2.50
prices['Iced'] = 2.50
#Add new products here in the format given above. The program will automatically adapt to encorporate the new product.

#Shell explanation text
print('''\n                 ( (      \n                  ) )     \n               ........  \n               |      |] \n               \      /  \n                `----'   \n 
*** Welcome to Café Au Lait! ***
Please see the user interface window (python) to place and track orders over the current order period.
Press command-tab (Mac) or alt-tab (Windows) to access the interface.
Consult the user manual (see documentation) if help is required.
To add additional products, please see the source code - and add the new product(s) on line 15.
Please note that when the order period is reset, the statistics of that order period will be printed here for future reference.
''')

#GUI element initialisation
#GUI Initialisation and setting of defaults
defaultFont = "arial 14"
main = Tk() #main window
main.title("Café au Lait Ordering System")
main.option_add("*font", defaultFont)
main.geometry("600x550")

#Constants
numberOfProducts = len(prices) #Amount of products
gapLength = 4 #Gap (in rows) between the entry fields and the summary table
takeAwayTax = 1.1 #Tax on take away orders
takeAwayNo = 0 #Counter on the number of take away orders

#Initialisation - Histories of products, order prices and takeaway status
history = {} #Empty dictionary to store all histories
quantities = {} #Empty dictionary to store all of the variables holding the data from entry fields
for d in prices:
    history[d] = [] #Sets up arrays for histories of each product
    quantities[d] = IntVar()# Quantities dictionary, modelled of the prices dictionary. Variable to store entered data.
#End For
history["Orders"] = [] #Empty history for order prices
history["Take away"] = [] #Empty history for take away
takeAway = BooleanVar() #Variable to store the result of the checkbox

#Dictionaries storing static interface labels. All elemenets can be looked up within these dictionaries using the appropriate key.
labels = {} #Product labels in ordering section
entryFields = {} #Entry fields for each product
summaryLabels = {} #Product /statistic labels in summary section
summaryTitles = {} #Bold titles at the start of the summary section
summarySums = {} #Total orders, take away orders, order price
errorLabels = {} #Labels to indicate invalid input.
summaryNos = {}  #Labels to indicate total orders of a product over the order period.
histories = {} #Histories of product orders (label showing array)

#Starting row/columns (counters) for loops that iterate by product name
startingRow = 1
startingSumRow = 1
columnNo = 0

#Main title of the window
Title = Label(text = "Welcome to Café au Lait!")
Title.grid(row = 0,column=0, columnspan = 3)
Title.configure(font = ('Baskerville', 30, 'bold'), fg = "blue")

#Product labels, prices, entry fields and error fields - required interface elements for each product.
for y in prices:
    labels[y] = Label(main,text = y) #Main label next to entry field
    labels[y].grid(row = startingRow, column = 0, sticky = W)
    price = y + " price"
    labels[price] = Label(main, text = "(${:1,.2f} ea) ".format(prices[y])) #Product price
    labels[price].grid(row = startingRow, column = 1, sticky = W)
    entryFields[y] = Entry(main, textvariable = quantities[y]) #Entry field for product
    entryFields[y].grid(row = startingRow, column = 2)
    quantities[y].trace("w", lambda name, index, mode, y=y: setUncheckedOrder()) #Validity check/ subtotal generation when changed
    errorLabels[y] = Label(main, text = "") #Error label adjacent to entry field
    errorLabels[y].grid(row = startingRow, column = 3, columnspan = 2, sticky = W)
    summaryLabels[y] = Label(main, text = y) #Label for product in the summary section
    summaryRow = numberOfProducts+gapLength+startingRow #Row number for the summary section
    summaryLabels[y].grid(row = summaryRow, column = 0, sticky = W)
    summaryNos[y] = Label(main, text = "0") #Number of orders of that product
    summaryNos[y].grid(row = summaryRow, column = 1)
    histories[y] = Label(main, text = "") #Label displaying the array of the order history of the product
    histories[y].grid(row = summaryRow, column = 2, columnspan = 100, sticky = W)
    startingRow += 1 #Move to the next row down for the next product
#End For

#Subtotal label that automaticall recalculates upon any change in the entry fields
subtotal = Label(main,text = "Subtotal: ${:1,.2f}".format(0))
subtotal.grid(row = numberOfProducts+1, column = 0, columnspan = 3, sticky = W)
subtotal.configure(font = defaultFont + " bold") #Set bold text
    
#Takeaway checkbox
takeAwayEntry = Checkbutton(main, text = "Takeaway  ", variable = takeAway)
takeAwayEntry.grid(row = numberOfProducts+1, column = 2, sticky = E)
takeAway.trace("w", lambda name, index, mode, y=y: setUncheckedOrder()) #Validity check/subtotal generation when changed

#Gap between the order and history sections
gap = Label(main, text = "").grid(row = numberOfProducts+2, column = 0, columnspan = 100) #Gap between the current order section and the summary section

#Summary labels
for z in ["Past orders: ", "Total", "History of quantities/prices: "]: #Column headers
    summaryTitles[z] = Label(main,text = z) #Sets up a new label
    summaryTitles[z].grid(row = numberOfProducts + gapLength,column = columnNo, sticky = (N if z == "Total" else W)) #End If, places in correct location
    summaryTitles[z].configure(font = (defaultFont + " bold")) #Bold text
    columnNo += 1 #Move to the next column for the next title
#End For
    
for a in ["Total price of orders", "Orders", "Take away"]: #Summary statistic rows
    summaryLabels[a] = Label(main, text = a + ": ") #new label
    summaryLabels[a].grid(row = 2*numberOfProducts+gapLength+startingSumRow, column = 0, sticky = W) #position
    summarySums[a] = Label(main, text = ("${:1,.2f}" if a == "Total price of orders" else "{}" ).format(0)) #sum label
    summarySums[a].grid(row = 2*numberOfProducts+gapLength+startingSumRow, column =1, sticky = N) #position
    histories[a] = Label(main, text = "") #History array text
    histories[a].grid(row = 2* numberOfProducts+gapLength+startingSumRow, column = 2, columnspan = 100, sticky = W) #position
    startingSumRow += 1 #Next row for the next product
#End For
    
#Function definition
#Function to take quantities and convert to a total order price
def calculateOrderPrice():
    def productPrice(product):
        return prices[product]*quantities[product].get()
    tax = takeAwayTax if takeAway.get() else 1 #End If - determines whether to apply the T/Aw tax
    price = 0
    #End module
    for b in prices: #For each product
        price +=  productPrice(b)#Add the correspoding price multiplied by number of product
    #End For
    price *= tax #Tax modification
    return round(price,4) #Price to 4dp
#End module

#Function to calculate & display a subtotal
    
#Function to place the order and enter it into the records
def doPlaceOrder():
    def appendHistories(product):
        history[product].append(quantities[product].get()) #Add to the history
        histories[product].configure(text = str(history[product])) #Change the GUI text
        summaryNos[product].configure(text = str(sum(history[product]))) #Change the GUI sum
        entryFields[product].delete(0,END) #Clear the entry fields
        entryFields[product].insert(0,0)
    #End module
    global history, histories, summarySums, takeAwayNo
    #Add to the order histories, display these histories and resulting totals
    if takeAway.get(): takeAwayNo += 1 #End If
    #Order period statistics
    history["Take away"].append("Y" if takeAway.get() else "N") #End if, adding to t/aw history
    history["Orders"].append(calculateOrderPrice()) #Add order price to history
    #Sum/history calculation/display
    summarySums["Orders"].configure(text = str(len(history["Orders"])))
    summarySums["Total price of orders"].configure(text = "${:1,.2f}".format(sum(history["Orders"])))
    histories["Total price of orders"].configure(text = str(history["Orders"]))
    summarySums["Take away"].configure(text = str(takeAwayNo))
    histories["Take away"].configure(text = str(history["Take away"]))
    #Price histories for the order period
    for e in prices: #For each product, modify & display the history, then reset the entry fields to 0.
        appendHistories(e)
    takeAwayEntry.deselect() #Deselect take away by default
    subtotal.configure(text = "Subtotal: $--") #Reset the subtotal display
    #End For
#End module
        
#Function to reset the order period
def resetAll():
    def generateHistoryString(product):
        historyString = '' #Row of the summary table
        for historyEntry in history[l]: #Create an order by order history, in columns.
            historyString += "{:^8}".format(str(historyEntry) if l!="Orders" else "${:1,.2f}".format(historyEntry))# Add the title and contents of the row
        #End  for
        sumText = ""
        if l=="Orders": sumText = "${:1,.2f}".format(sum(history[l])) #Display in price format
        elif l!="Take away": sumText = str(sum(history[l])) #Display sum of orders
        else: sumText = str(takeAwayNo) #Display the takeaway count
        #End If
        return ("{:<35}: ".format("{:<14}".format(str(l)) + "({} total)".format(sumText))+ historyString) #Overall title : history format
    #End module
    def resetHistory(product):
        history[product] = []
        histories[product].configure(text = "")
        try: summarySums[product].configure(text = "0") #For the properties that store a history, if there is a summary sum, clear that as well
        except KeyError: pass
        #End Try
        try: #For the items that store a history and also have summary numbers and entry fields, clear them
            summaryNos[product].configure(text = "0") #Reset displays
            entryFields[product].delete(0,END) #Clear entry fields
            entryFields[product].insert(0,0)
        except KeyError: pass
        #End Try
    #End module
    global history, takeAwayNo
    if checkValidity(): #If there is a valid order not yet placed
        placeOrder() #Place the order before clearing everything
    #End if
    #Generate a readable output of the order period's data and associated statistics
    print("\n --- ORDER PERIOD SUMMARY --- ")
    print("{:<15}:  ".format("Generated at: ") + time.asctime()) #Print time of generation
    print("{:<15}:  ".format("Orders") + "{:^8}".format(str(len(history["Orders"])))) #Print the number of orders
    print("{:<15}  ".format("\nOrder history"))
    for l in history: #For each order period aspect:
        print(generateHistoryString(l)) #Print the history
        resetHistory(l) #Reset the history for the next order
    #End for
    print(" - END ORDER PERIOD SUMMARY - \n")
    #Reinitialise interface
    takeAwayNo = 0
    takeAwayEntry.deselect()
    setUncheckedOrder()
    summarySums["Total price of orders"].configure(text = "${:1,.2f}".format(0))
    histories["Total price of orders"].configure(text = "")
#End module
    
#Function to check that each of the entry fields only contain integers
def checkValidity():
    global valid
    valid = True
    #Module to set the order validity to false and display the error to the user
    def displayInvalid(product): #Parameter - determines which product is invalid
        global valid
        valid = False
        errorLabels[product].configure(text = "Enter a valid number.") #Displays the error message
    #End module
    def errorCheck(product):
        errorLabels[product].configure(text = "")
        #Set of conditions where input is invalid
        notWholeNumber = int(quantities[product].get()) != float(entryFields[product].get())
        notBlank = len(entryFields[product].get()) > 1
        startZero = entryFields[product].get()[0] == '0'
        negative = quantities[product].get() < 0
        if notWholeNumber or (notBlank and startZero) or negative:
            displayInvalid(product)
        #End if
    #End module
    #Check each field
    for c in prices:
        try: errorCheck(c)
        except TclError: displayInvalid(c) #If the input is not a number
        #End Try
    #End for       
    try:
        if calculateOrderPrice() == 0: valid = False #Ensures at least one product is ordered
    except: pass #in case the input is still invalid
    #End Try
    return valid #Boolean state of the order's validity
#End module
        
#Function to check the validity of the input, and hide the place order button whenever any input is changed
def setUncheckedOrder():
    if checkValidity(): #Check the order's validity
        placeOrderButton.configure(state = NORMAL) #Shows the place order button
        price = calculateOrderPrice() #calculate the price
        subtotal.configure(text = "Subtotal: ${:1,.2f}".format(price))
    else:
        subtotal.configure(text = "Subtotal: $--") #Hide the subtotal
        placeOrderButton.configure(state = DISABLED) #Hides the place order button
    #End if
#End module
    
#Function to manage the placing of the order
def placeOrder():
    doPlaceOrder() #Do the main check order module
    setUncheckedOrder() #Reset the order status to unchecked
#End module

#Function to output results and close the window
def closeWindow():
    resetAll() #Reset the statistics
    main.destroy() # close the window
#End module
        
#Main user interaction buttons and properties
placeOrderButton = Button(main, text="Place order", command = placeOrder, state = DISABLED)
placeOrderButton.grid(row = numberOfProducts+1, column = 3, sticky = W) #Gives the option to now place the order
resetButton = Button(main, text="Reset History", command = resetAll)
resetButton.grid(row = 2*numberOfProducts+gapLength+len(summarySums)+1, column = 0) #Resets order history
closeButton = Button(main, text="Close", command = closeWindow)
closeButton.grid(row = 2*numberOfProducts+gapLength+len(summarySums)+1, column = 2,sticky = E) #Closes the window
setUncheckedOrder() #Initialises the entry fields and subtotal
#Program loop begins (modules run prompted by data entry or button pressed)
