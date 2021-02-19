#program will calculate the theoretical profitability of tanning dragonhides
def main():
    intro()
    calc()
    restart()


def intro():
    print('This is a calculator that calculates the total profitablity')
    print('of tanning dragonhides per hour.')
    print()

def calc():
    try:
        bp_of_hides = int(input('What is the buying price of hides currently?: '))
    
        sp_of_hides = int(input('What is the selling price of hides?: '))

        amount = int(input('How many items are there?: '))

        cost_of_hides = (amount * bp_of_hides)
        profit_of_leathers = (amount * sp_of_hides)
        #per inventory (25 hides)
        tanning_fee = (amount * 20)
        
        total_profit = (profit_of_leathers - cost_of_hides) - tanning_fee
        if total_profit < 0:
            print('No profit')
            import time
            print('Restarting...')
            time.sleep(2)
            restart(calc())
        else:
            print('The total profit is', total_profit, 'GP per hour.')
    except:
        print('This occurs when something wrong is inputted')
        print('Restarting...')
        import time
        time.sleep(2)
        restart(calc())

def restart():
    try:
        prompt = input('Restart program? Type yes/no or y/n: ')
        if prompt == 'yes' or prompt == 'y':
            restart(main())
        if prompt == 'no' or prompt == 'n':
            import time
            print('Ending Program...')
            time.sleep(1)
    except:
        print('This happens when some key is inputted that isnt prompted.')
        print('This will also happen when the IDLE editor is used.')
        print('Restarting...')
        import time
        time.sleep(2)
        restart()
        
main()
        

    
                
    
