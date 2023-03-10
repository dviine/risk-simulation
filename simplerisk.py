from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init()

import random

def simulate_battle(num_attackers, num_defenders):
    """Simulates a battle between attackers and defenders in the game of Risk.
    Follows the standard rules for rolling dice:
    - Attackers roll up to 3 dice, defenders roll up to 2 dice
    - For each pair of dice, the highest roller wins. If there is a tie, the defender wins.
    - The loser removes one army for each loss.
    
    Returns:
        tuple: a tuple containing the number of remaining attackers and defenders
    """
    num_attack_dice = min(3, num_attackers - 1)
    num_defend_dice = min(2, num_defenders)
    initial = (num_attackers, num_defenders)
    
    attack_rolls = [random.randint(1, 6) for _ in range(num_attack_dice)]
    defend_rolls = [random.randint(1, 6) for _ in range(num_defend_dice)]
    
    attack_rolls.sort(reverse=True)
    defend_rolls.sort(reverse=True)
    
    while len(attack_rolls) > 0 and len(defend_rolls) > 0:
        if attack_rolls.pop(0) > defend_rolls.pop(0):
            num_defenders -= 1
        else:
            num_attackers -= 1
    
    a_difference = num_attackers - initial[0]
    a_difference = "-" + str(a_difference) if a_difference > 0 else str(a_difference)
    d_difference = num_defenders - initial[1]
    d_difference = "-" + str(d_difference) if d_difference > 0 else str(d_difference)
    difference = (a_difference, d_difference)

    return (num_attackers, num_defenders, difference)

def user_input(finalattackers, finaldefenders, win):
    if win == False:
        print(f"{Fore.BLACK}Current value is: " + str(finalattackers) + f", press enter to keep this value.{Style.RESET_ALL}")
    num_attackers = int(input("Enter number of attackers: ") or finalattackers)
    if win == False:
        print(f"{Fore.BLACK}Current value is: " + str(finaldefenders) + f", press enter to keep this value.{Style.RESET_ALL}")
    num_defenders = int(input("Enter number of defenders: ") or finaldefenders)
    if num_attackers <= 1:
        raise ValueError("Must have at least 2 attackers")
    if num_defenders <= 0:
        raise ValueError("Must have at least 1 defender")
    return (num_attackers, num_defenders)

def main():
    finalattackers = 0
    finaldefenders = 0
    win = False
    while True:
        try:
            num_attackers, num_defenders = user_input(finalattackers, finaldefenders, win)
        except ValueError as e:
            print(e)
            continue
        num_attackers, num_defenders, difference = simulate_battle(num_attackers, num_defenders)
        if num_attackers <= 1:
            print("Defender wins with {} units remaining!\n".format(num_defenders))
            win = True
            continue
        if num_defenders == 0:
            print("Attacker wins with {} units remaining!\n".format(num_attackers))
            win = True
            continue
        else:
            print(f"{Fore.RED}Attackers: {num_attackers} ({difference[0]}) Defenders: {num_defenders} ({difference[1]}){Style.RESET_ALL}\n")
            win = False
            finalattackers = num_attackers
            finaldefenders = num_defenders

if __name__ == "__main__":
    try:
        print("Risk Battle Simulator (Ctrl-C to exit)")
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
