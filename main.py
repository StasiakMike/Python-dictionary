from tkinter import *

#click function
def click():
    entered_text=textentry.get() #will catch text from textarea
    output.delete(0.0, END)#clears the output box
    try:
        definition = my_dictionary[entered_text]
    except:
        definition = "sorry unknown word, try any other Python related"
    output.insert(END, definition)

## main program
window = Tk()
window.title("Python Glossary Project")

##window features
window.configure(background="black")

##adding a photo
photo1 = PhotoImage(file="pyt.gif")
Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=W)

##create label
Label (window, text="Enter the word you lookign dedfiniton for:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
Label (window, text="like Python or syntax", bg="black", fg="white", font="none 10") .grid(row=2, column=0, sticky=W)

##create text entry area
textentry = Entry(window, width=50, bg="white")
textentry.grid(row=3, column=0, sticky=W)

##submit button
Button(window, text="SUBMIT", width=15, bg="red", command=click) .grid(row=4, column=0, sticky=W)

##answer board label
Label (window, text="Definition:", bg="black", fg="white", font="none 12 bold") .grid(row=5, column=0, sticky=W)

##answer board
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=6, column=0, columnspan=2, sticky=W)

##dictionary content
my_dictionary = {
    'python':'Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.',
    'syntax':'Python is meant to be an easily readable language. Its formatting is visually uncluttered, and it often uses English keywords where other languages use punctuation. Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are optional. It has fewer syntactic exceptions and special cases than C or Pascal'
    }

##exit button label
Label (window, text="To exit the dictionary:", bg="black", fg="white", font="none 12 bold") .grid(row=7, column=0, sticky=W)

##exit function
def close_window():
    window.destroy()
    exit()

##exit button
Button(window, text="EXIT", width=15, bg="white", command=close_window) .grid(row=8, column=0, sticky=W)

##exit button label
Label (window, text="2019 Mike Stasiak & MvdB Software Solutions", bg="black", fg="white", font="none 8") .grid(row=9, column=0, sticky=W)


###main loop run
window.mainloop()
