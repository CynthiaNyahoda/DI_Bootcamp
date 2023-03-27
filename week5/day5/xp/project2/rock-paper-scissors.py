from game import Game

def get_user_menu_choice():
    while True:
        choice = input("Enter choice: (N)ew game, (S)how scores, (Q)uit: ").lower()
        if choice in ['n', 's', 'q']:
            return choice

def print_results(results):
    print("Game summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'n':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == 's':
            print_results(results)
        else:
            print_results(results)
            break

if __name__ == '__main__':
    main()
