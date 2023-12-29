
#C:\Users\Cameron\Desktop\CS1120\CoreyChristmas>python -m PyInstaller main.py

quiz_data = [
    {
        "question": "I'm a Goofy Goober...",
        "choices": ["Sock", "Clock", "Rock", "Mock"],
        "answer": "Rock"
    },
    {
        "question": "You're a Goofy Goober...",
        "choices": ["Rock", "Glock", "Shock", "Lock"],
        "answer": "Rock"
    },
    {
        "question": "WERE ALL GOOFY GOOBERS!!!...",
        "choices": ["Stock", "Rock", "Block", "Dock"],
        "answer": "Rock"
    },
    {
        "question": "Goofy Goofy Goofy Goober...",
        "choices": ["Cock", "Brock", "Flock", "Rock"],
        "answer": "Rock"
    },
    {
        "question": "Run for dem life when you step into the...",
        "choices": ["Costco", "Jungle", "Bathroom", "Grand Canyon"],
        "answer": "Jungle"
    },
    {
        "question": "I remember you was...",
        "choices": ["Lucy", "Missing", "My Friend", "Conflicted"],
        "answer": "Conflicted"
    },
    {
        "question": "Beaver Island Girls...",
        "choices": ["They Don't Agree With Us", "There's Only 3 Of Us", "We're Unforgettable", "We're undeniable"],
        "answer": "There's Only 3 Of Us"
    },
    {
        "question": "Baddadan Baddadan...",
        "choices": ["Baddadan", "Batman", "Barbacoa", "Bastion"],
        "answer": "Baddadan"
    },
    {
        "question": "Good Faith...",
        "choices": ["Never", "Only on Fridays", "Sometimes", "Forever"],
        "answer": "Forever"
    },
    {
        "question": "An Object in Motion Will Remain in Motion Unless...",
        "choices": ["it gets eepy", "it neebys to go sleeby", "go bedby casue eeby and sleeby", "Acted Upon by a Force"],
        "answer": "Acted Upon by a Force"
    },
    {
        "question": "In 2023 The Average Price of a Chicken Ball was...",
        "choices": ["$524.04", "$207.88", "$476.62", "$654.39"],
        "answer": "$476.62"
    },
    {
        "question": "Andy is a...",
        "choices": ["Pterodactyl", "Proctologist", "Polyrizzler", "Polydactyl"],
        "answer": "Polydactyl"
    },
    {
        "question": "xibu uzqf pg djqifs jt vtfe up btl uijt rvftujpo?",
        "choices": ["qjhqfo", "dbftbs", "sbjm gfodf", "bvuplfz"],
        "answer": "dbftbs"
    },
    {
        "question": "だめだね だめよ だめなのよ あんたが 好きで好きすぎて どれだけ 強いお酒でも 歪まない思い出が...",
        "choices": ["馬鹿みたい", "バスケットボール", "トースター", "ハンバーガー"],
        "answer": "馬鹿みたい"
    }
    
    
    # Add more questions here
]





import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style


# Function to display the current question and choices
def show_question():
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        if score < len(quiz_data):
        # If all questions have been answered, display the final score and end the quiz
            messagebox.showinfo("Quiz Completed",
                                "Try again, go for a perfect score!! Trust me its worth it ;) Final score: {}/{}".format(score, len(quiz_data)))

            root.destroy()
        else:
            messagebox.showinfo("Quiz Completed",
                                 "Congratulations and Merry Christmas! You won a key to play Lethal Company on Steam!! Final score: {}/{}".format(score, len(quiz_data)))
            root.destroy()

# Create the main window
root = tk.Tk()
root.title("Merry Christmas")
root.geometry("1920x1080")

style = Style(theme="vapor")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Terminal", 50))  
style.configure("TButton", font=("System", 30))  

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=1400,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
