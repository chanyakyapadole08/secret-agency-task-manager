# Uses colors to make the game attractive in terminal

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create empty board
board = [" " for _ in range(9)]

# Function to print stylish board
def print_board():
    print()
    print(Fore.YELLOW + "     TIC TAC TOE 🎮")
    print()
    print(f"  {board[0]} {Fore.YELLOW}|{Style.RESET_ALL} {board[1]} {Fore.YELLOW}|{Style.RESET_ALL} {board[2]}")
    print(Fore.YELLOW + " ---+---+---")
    print(f"  {board[3]} {Fore.YELLOW}|{Style.RESET_ALL} {board[4]} {Fore.YELLOW}|{Style.RESET_ALL} {board[5]}")
    print(Fore.YELLOW + " ---+---+---")
    print(f"  {board[6]} {Fore.YELLOW}|{Style.RESET_ALL} {board[7]} {Fore.YELLOW}|{Style.RESET_ALL} {board[8]}")
    print()

# Check winner
def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Start game
current_player = "X"

while True:
    print_board()

    # Show colored turn message
    if current_player == "X":
        print(Fore.RED + "Player X Turn ❌")
    else:
        print(Fore.BLUE + "Player O Turn ⭕")

    move = int(input("Choose position (1-9): ")) - 1

    # Validate move
    if move < 0 or move > 8 or board[move] != " ":
        print(Fore.RED + "❌ Invalid move! Try again.")
        continue

    # Place symbol with color
    if current_player == "X":
        board[move] = Fore.RED + "X" + Style.RESET_ALL
    else:
        board[move] = Fore.BLUE + "O" + Style.RESET_ALL

    # Check winner
    if check_winner(board[move]):
        print_board()
        print(Fore.GREEN + f"🎉 Player {current_player} Wins the Game!")
        break

    # Check draw
    if is_draw():
        print_board()
        print(Fore.CYAN + "🤝 It's a Draw!")
        break

    # Switch player
    current_player = "O" if current_player == "X" else "X"
