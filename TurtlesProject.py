# program that creates and manages a FIFO queue of strings. The user can add a string to the queue,
# or remove the head of queue. They can also remove a string from the front of the queue and place it at
# the back fo the queue. 

# My initial list which is empty
import turtle #imports turtle
wn = turtle.Screen() #creates the turtle screen
wn.setup(550,500)

queue = [] #y initial empty queue
myset = {"A","N","L","P","Q"} #only these options will be accepted in the menu selection




turtles = [] #my empty queue for new turtles.
#colour list
colors = ["red", "orange","yellow", "green", "blue", "pink", "tomato", "lawngreen", "saddlebrown", "lightcoral", "teal", "gold", "ivory", "lightseagreen", "lime", "navy", "slateblue", "teal", "magenta", "purple", "darkred", "tan", "dodgerblue", "crimson", "darkorange", "forestgreen", "aqua", "hotpink", "thistle", "orchid", "black", "grey", "peru", "darkviolet", "skyblue", "palegoldenrod", "rosybrown", "silver", "limegreen", "bisque", "darkgreen", "slateblue", "mediumorchid", "deeppink", "aquamarine", "olivedrab", "orangered", "darkgoldenrod", "wheat", "springgreen"]
#X coordinates(fixed)All coordinates are fixed, only colors change.
coordx = [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Y cooridnates(fixed)
coordy = [200, 150, 100, 50, 0, -50, -100, -150, -200, -250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250, 200, 150, 100, 50, 0, -50, -100, -150, -200, -250]


#This prints the menu
print("Please select an option from the Menu \n A - Add a string to the Queue. \n N - Remove the head of the Queue. \n L - The chosen string leaves the queue and rejoins the back of the Queue. \n P - Prints the current Queue. \n Q - Quits the program. ")


#adding elements to the queue
def Append(the_list):
    gz = input("Enter a string: ")
    if gz == "": # checks if the user string is empty, if it is, it asks the user to re-enter a string.
        Append(queue)
    else:
        the_list.append(gz) #appends the user input to the back of the queue
        turtles.append(turtle.Turtle()) #Adds a new turtle object to turtle list.
        visualise(queue, turtles, colors, coordy, coordx) # starts to visualise the queue of turtles.
    for i in the_list:
        if i == '':
            print("You have entered an empty string")
            the_list.remove('')
            Append(queue)

def visualise(wordlist, turtles, colors, coordy, coordx): # function to viualise the turtle queue
    length = len(turtles) 
    if length == 0: #if there is only 1 tutrtle in the queue, it clears the screen if 'N' is chosen. 
        nextvisualise(wordlist, turtles, wn)
    for i in range(length):
        gz = i
        turtles[gz].speed(0) #creates the queue of turtles on the screen. 
        turtles[gz].color(colors[gz]) #chooses the color of the turtle.
        turtles[gz].shape("turtle") # chages the shape to that of a 'turtle'
        turtles[gz].penup() # so the turtle doesn't leave a trail
        turtles[gz].goto(coordy[gz], coordx[gz]) # sets the coordinates of the turtle(these are always fixed)This prevents overlapping. 

def nextvisualise(wordlist, turtles, wn):#this was needed for if there was only one turtle left. 
    wn.clear()
            
    
# This allows the user to access functions of the menu
def function():
    return input("Enter a menu selection ")
    
#remove the first element in the queue
def Next(the_list, turtles, colors, coordy, coordx, wn):
    length = len(turtles)
    if length > 1:
        del the_list[0]
        del turtles[0]
        z = colors[0]
        del colors[0]
        colors.append(z)
        visualise(queue, turtles, colors, coordy, coordx)
    elif length == 0:
        #I'm not sure what would happen if it got here...
            


        nextvisualise(queue, turtles, wn)
    elif length == 1:
        the_list.pop(0)
        turtles.pop(0)
        z = colors[0] #recyles the colour list.
        colors.pop(0) #removes the first colour in the colour list.
        colors.append(z) #places the stored colour at the end of the queue.
        nextvisualise(queue, turtles, wn)
    elif the_list == "":
        function()
            
               

# The user inputs a string, if the string is in the queue, it is removed from the front.
def Leave(the_list, turtles, colors, wn):
    sz = input("Enter a string ")
    if sz == "":
        Leave(queue, turtles, colors, wn)

    for i in the_list:
        if sz == "":
            Leave(queue, turtles, colors, wn)
    
        elif i == sz:
            pe = sz
            index = the_list.index(pe)
            gz = index
            the_list.remove(sz)
            cg = colors[gz] #to recycle the colours
            del turtles[0] # added this, as the original function was leaving a turtle stamp on the screen.
            colors.pop(index)
            colors.append(cg)
            visualise(queue, turtles, colors, coordy, coordx)
            break
    
# This is my infinite loop. It will loop until the user inputs "Q". Otherwise
# it will ask for new user inputs for the menu.
while True:   
    menu = function()
    if menu == "Q": # Quits the program
        print("Goodbye")
        break
    
    elif menu == "A":
        if len(queue) > 50:
            print("Queue is full, please remove one of the elements first")
            function() 
        else:
            Append(queue) # Adds a new string to the queue.
        
    elif menu == 'N': Next(queue, turtles, colors, coordy, coordx, wn) # Removes the head of the queue
        
    elif menu == "L": # User inputs a string, if element in queue, it will be removed. 
        Leave(queue, turtles, colors, wn)
    
    elif menu == "P": print(' '.join(queue)) # Prints the queue, with no brackets or commas.

    elif menu == "": print("Please choose a correct option.") #For if user enters an empty string on the menu selection. 

    elif menu not in myset: print("Please choose a correct option.")#If the user enters anything other than the menu options. 




    