import turtle

#the turtle that will draw the main playing matrix and the numbers on it
drawer = turtle.Turtle()
drawer.pensize(10)
drawer.color("white")

#the turtle that will write who is the winner
shouter=turtle.Turtle()
shouter.penup()
shouter.pensize(5)
shouter.color("red")
shouter.goto(-50,-330)
shouter.hideturtle()

#screen set up
s = turtle.Screen()
s.bgcolor("black")
s.title("X , O game",)

#a methode for drawing the board
def DrawBoard():
      drawer.speed(10)
      
      #horizantally lines
      for i in range(2):
       drawer.penup()
       drawer.goto(-300,100-200*i)
       drawer.pendown()
       drawer.forward(600)
      
      drawer.left(90)
      
      #veritcally lines
      for i in range(2):
       drawer.penup()
       drawer.goto(100-200*i,-300)
       drawer.pendown()
       drawer.forward(600)

      # for writing the numbers
      number=1
      for i in range(3):
       for j in range(3):
            drawer.penup()
            drawer.goto(-260+j*200,250-i*200)
            drawer.pendown()
            drawer.write(number,font=15)
            number+=1
      drawer.hideturtle()
      
# method to draw X in the position x , y                
def DrawX(x,y):
      
      drawer.penup()
      drawer.goto(x,y)
      drawer.color("green")
      drawer.pendown()
      drawer.setheading(60)
      for i in range(2):
            drawer.forward(75)
            drawer.backward(150)
            drawer.forward(75)
            drawer.left(69)

# method to draw O in the position x , y
def DrawO(x,y):
      
      drawer.penup()
      drawer.goto(x+40,y)
      drawer.color("blue")
      drawer.pendown()
      drawer.circle(50)

# method to place O in a spacific position (Computer player)
def AddO():
      #block x from wining
      for i in range(3):
            for j in range(3):
                   if board[i][j]=="":
                         board[i][j]="x"
                         if win("x"): 
                               DrawO(-250+200*j,250-200*i)
                               board[i][j]="o"
                               return
                         else:board[i][j]=""
      for i in range(3):
            for j in range(3):
                   if board[i][j]=="o" or board[i][j]=="x":
                    continue
                   elif board[i][j]=="":
                         DrawO(-250+200*j,250-200*i)
                         board[i][j]="o"
                         return  

# method to place X in a spacific position that the player will decide (Human player)
def AddX(row,columns):
      shouter.clear() 
      #check if the spot is taken
      if board[row][columns]=="o" or board[row][columns]=="x":
            shouter.write("That spot is taken",font=55)
            s.update()
            
      else:
            DrawX(-200+200*columns,200-200*row) 
            board[row][columns]="x"
      # check if X win
            if win("x")==True:
                  shouter.write("X won",font=("arial",25,"bold"),)
                  s.update()
                  DeActivate()
            else: 
            # if X didn't win add O
             AddO()
            # check if O win
             if win("o")==True:
              shouter.write("O won",font=("arial",25,"bold"))
              s.update()
              DeActivate()
            
            
        
def Xsq1():
      AddX(0,0)
def Xsq2():
      AddX(0,1)
def Xsq3():
      AddX(0,2)
def Xsq4():
      AddX(1,0)
def Xsq5():
      AddX(1,1)
def Xsq6():
      AddX(1,2)
def Xsq7():
      AddX(2,0)
def Xsq8():
      AddX(2,1)
def Xsq9():
      AddX(2,2)

#array of the matrix spots 
#        |        |
#   Xsq1 |  Xsq2  |  Xsq3
#   ------------------------
#        |        |
#   Xsq4 |  Xsq5  |  Xsq6
#   ------------------------
#        |        |
#   Xsq7 |  Xsq8  |  Xsq9

X_list=[Xsq1,Xsq2,Xsq3,Xsq4,Xsq5,Xsq6,Xsq7,Xsq8,Xsq9]  

#method to activate the user buttons
def X_Activate(X_list):
      for i in range(9):
            s.onkey(X_list[i], str(i+1))
#method to deactivate the user buttons
def DeActivate():
      for i in range(9):
            s.onkey(None, str(i+1))

#array of the matrix and it starts empty 
board=[["","",""],["","",""],["","",""]]

#method to check if there is a winner
def win(w):
      #for horizantally and veritcally
      for i in range(3):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] == w and board[i][1] == w and board[i][0] == w:
                  return True
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] == w and board[1][i]==w and board[0][i] :
                   return True
      #diagonally down
      if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == w and board[1][1]==w and board[0][0]==w:
                   return True
      #diagonally up
      if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == w and board[1][1]==w and board[0][2]==w:
                   return True
      
      return False

#calling the drawing border method
DrawBoard ()

s.update()

#calling the activate the user buttons
X_Activate(X_list) 

s.listen()

turtle.done()