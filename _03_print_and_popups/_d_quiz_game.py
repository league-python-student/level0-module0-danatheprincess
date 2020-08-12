from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window=Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score=0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    book=simpledialog.askstring("Harry Potter","Who opened The Chamber of Secrets in book two?")
    #      // 3.  Use an if statement to check if their answer is correct
    if book=="Ginny Weasely":
        messagebox.showinfo("","You are CORRECT!")
    #      // 4.  if the user's answer was correct, add one to their score 
        score+=1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above
    history=simpledialog.askstring("History","What was Martin Luther King's speech called?")
    if history=="I Have A Dream":
        messagebox.showinfo("","You are CORECT!")
        score+=1

    math=simpledialog.askstring("Math","What is 15x15")
    if math=="225":
        messagebox.showinfo("","You are CORRECT!")
        score+=1
    #      // Option: Subtract a point from their score for a wrong answer
    messagebox.showinfo("score","Your score is"+str(score))
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
