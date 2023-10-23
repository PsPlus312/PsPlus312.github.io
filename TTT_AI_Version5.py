import tkinter as tk
from tkinter import messagebox
import random

current_player = "X"
board = [" " for _ in range(9)]
ai_enabled = False 
ai_names = ["AlphaShow", "BetaPlayer", "AidenPearce"]
ai_name_index = 0

def check_winner(player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def button_click(index):
    global current_player
    global ai_name_index

    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player)
        if check_winner(current_player):
            if current_player == "O":
                messagebox.showinfo("TIc-Tac-Toe", f"Player {ai_names[ai_name_index]} wins!")
                ai_name_index = (ai_name_index + 1) % len(ai_names)
            else:
                messagebox.showinfo("TIc-Tac-Toe", f"Player {current_player} wins!")
            root.quit()
        elif " " not in board:
            messagebox.showinfo("Tic-Tac-Toe", "Its a draw!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"
            if current_player == "O" and ai_enabled:
                root.after(1000, ai_move)

def ai_move():
    empty_indices = [i for i, val in enumerate(board) if val == " "]
    if empty_indices:
        ai_choice = random.choice(empty_indices)
        button_click(ai_choice)

def toggle_ai():
    global ai_enabled
    ai_enabled = not ai_enabled 
    ai_button.config(text="AI: " + ("On" if ai_enabled else "Off"))

root = tk.Tk()
root.title("TIc-Tac-Toe")

buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=" ", font=("normal", 20), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=row, column=col)
    buttons.append(button)

ai_button = tk.Button(root, text="Ai: Off", command=toggle_ai)
ai_button.grid(row=3, column=1, columnspan=2)

root.mainloop()

