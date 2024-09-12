'''
Create a program capable of displaying questions to the user like KBC

use List data type to store the questions and their correct answers

Display the final amount the person is taking home after playing the game.
'''

# KBC Game Simulation

# List of questions and corresponding correct answers
questions = [
    {"question": "Who is the current President of the USA?", "options": ["A) Joe Biden", "B) Donald Trump", "C) Barack Obama", "D) George Bush"], "answer": "A"},
    {"question": "What is the capital of France?", "options": ["A) Rome", "B) Paris", "C) Madrid", "D) Berlin"], "answer": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"], "answer": "C"},
    {"question": "Who wrote 'Hamlet'?", "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"], "answer": "C"},
    {"question": "What is the chemical symbol for water?", "options": ["A) O2", "B) CO2", "C) H2O", "D) H2"], "answer": "C"},
]

# Prize money for each correct answer
prizes = [1000, 2000, 5000, 10000, 50000]

# Function to run the KBC game
def play_kbc():
    total_winnings = 0
    for i, q in enumerate(questions):
        print(f"\nQuestion {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        answer = input("Enter your answer (A/B/C/D): ").upper()
        
        if answer == q["answer"]:
            total_winnings += prizes[i]
            print(f"Correct! You have won Rs. {prizes[i]} so far.")
        else:
            print("Wrong answer! The game ends here.")
            break
    
    print(f"\nThank you for playing! You are taking home Rs. {total_winnings}.")

# Start the game
play_kbc()
