from BankAccount import print_balance
import BankAccount as BA

BA.check_balance()

print_balance()


input = BA.main_menu()

BA.menu_logic(input)

BA.deposit(600)
