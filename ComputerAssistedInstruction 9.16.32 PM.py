
import random

diff = int(input ("Enter difficulty level (1 to 2) :"))

def numbers ():

    if diff == 1:
        x = random.randint (0, 9)
    elif diff == 2:
        x = random. randint (10, 99)
    return x

numbers ()

def right ():

    a = {1: 'Nice work!', 2: 'Very good!',3: 'Keep up the good work!'}
    a2 = print (a[random.randint (1,3)])
    
right()

def wrong():
    
    b = {1: 'Wrong. Please try again.',2: 'No. Try once more.',3: 'No. Keep trying. '}
    b2 = print (b[random.randint (1,3)])
    
wrong()

def game():

    score = 0
    count = 0
    
    while True:
    
        print ("\nl = addition")
        print ("2 = subtraction")
        print ("3 =  multiplication")
        print ("4 = division")
        print ("5 =  random operation")
        
        selection = int (input ("\nEnter the operation 1 to 5:"))

        var1 = numbers()
        var2 = numbers ()
        
        if selection == 1:
            print ("How much is", var1,"+", var2,"?")
            x = int (input ("Enter your answer (-1 to exit): "))
            y = var1 + var2
            if x == -1:
                print ("\nNumber of correct answers:", +score)
                print ("Number of wrong answers:",+count)
                print ("Thanks for playing!")
                break
            elif x == y:
                right ()
                score=score + 1
            else:
                while x != y:
                    wrong ()
                    count = count + 1
                    x = int(input ("\nEnter your answer(-1 to exit):"))
                right ()
                score = score + 1
                
        elif selection == 2:
            a = ( (var1, var2) )
            if var1 < var2:
                a = ((var2, var1))
            else:
                a = ((var1, var2) )
            print ("How much is" +str (a[0]) +" - " +str(a[1])+ "?")
            x = int (input ("Enter your answer (-1 to exit) :"))
            if x == -1:
                print ("\nNumber of correct answers:", +score)
                print ("Number of wrong answers:", +count)
                print ("Thanks for playing!")
                break
            elif x ==(a[0]-a[1]) :
                right ()
                score = score + 1
            else:
                while x != (a[0]-a[1]) :
                    wrong ()
                    count = count + 1
                    x = int (input ("\nEnter your answer (-1 to exit) :") )
                rignt()
                score = score + 1
                
        elif selection == 3:
            print ("How much is", var1, "*", var2,"?")
            x = int (input ("Enter your answer (-1 to exit) :"))
            y = var1 * var2
            if x == -1:
                print ("\nNumber of correct answers:", +score)
                print ("Number of wrong answers:",+count)
                print ("Thanks for playing!")
                break
            elif x == y:
                right()
                score = score + 1
            else:
                while x != y:
                    wrong()
                    count = count + 1
                    x = int (input ("Enter your answer (-1 to exit) :"))
                right()
                score = score + 1
        elif selection == 4:
            if var2 == 0:
                var2 = 1
            print ("How much is", var1, "/", var2, "?")
            x = int (input ("Enter your answer(-1 to exit):" ))
            y = var1 // var2
            if x == -1:
                print ("\nNumber of correct answers:",+ score)
                print ("Number of wrong answers:",+ count)
                print ("Thanks for playing!")
                break
            elif x == y:
                right()
                score = score + 1
            else:
                while x != y:
                    wrong()
                    count = count + 1
                    x = int (input ("Enter your answer (-1 to exit) :"))
                right()
                score = score + 1
        elif selection == 5:
            choice = random. randint (1, 4)
            if choice  == 1:
                print ("How much is", var1, "+", var2, "?")
                x= int (input ("Enter your answer(-1 to exit): "))
                y = var1 + var2
                if x == -1:
                    print ("\nNumber of correct answers:",+score)
                    print ("Number of wrong answers:"+count)
                    print ("Thanks for playing! ")
                    break
                elif x == y:
                    right()
                    score = score + 1
                else:
                    while z != y:
                        wrong()
                        count = count + 1
                        x = int (input ("Enter your answer (-1 to exit) :"))
                    right()
                    score = score +1
            elif choice == 2:
                a = ((var2, var1))
                if var1 < var2:
                    a = ((var2, var1))
                else:
                    a = ((var2, var1))
                print ("How much is" +str(a[0]) + " - " +str(a[1])+ "?")
                x = int (input ("Enter your answer (-1 to exit) :"))
                if x == -1:
                    print ("/nNumber of correct answers:", +score)
                    print ("Number of wrong answers:",+count)
                    print ("Thanks for playing!")
                    break
                if x == (a[0] -a[1]) :
                    right ()
                    score = score + 1
                else:
                    while x != (a[0]-a[1]) :
                        wrong ()
                        count = count + 1
                        x = int (input ("(nEnter your answer (-1 to exit): "))
                    right ()
                    score = score + 1
            elif choice == 3:
                print ("How much is", var1, "*", var2,"?")
                x= int (input ("Enter your answer (-1 to exit): "))
                y = var1 * var2
                if x == -1:
                    print ("\nNumber of correct answers:", +score)
                    print ("Number of wrong answers:",+count)
                    print ("Thanks for playing!")
                    break
                elif x == y:
                    right()
                    score = score + 1
                else:
                    while x != y:
                        wrong()
                        count = count + 1
                        x = int (input ("Enter your answer (-1 to exit): "))
                    right()
                    score = score + 1
            elif choice == 4:
                if var2 ==0:
                    var2 =1
                print ("How much is", var1,"/",var2,"?")
                x = int (input ("Enter your answer (-1 to exit) :"))
                y = var1 // var2
                if x == -1:
                    print ("\nNumber of correct answers:",+score)
                    print ("Number of wrong answers:",+count)
                    print ("Thanks for playing!")
                    break
                elif x == y:
                    right ()
                    score = score + 1
                else:
                    while x != y:
                        wrong()
                        count = count + 1
                        x= int(input("\nEnter your answer (-1 to exit):"))
                        right ()
                        score = score + 1
game()
                                  

