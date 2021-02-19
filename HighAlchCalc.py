
def main():
    intro()
    calc()
    restart()
    
def intro():
   print('This will predict the profit made from high-alching.')
   print('To start, please see the indicated prompts below.')
   print('---------------------------------------------------') 
def calc():
    try:
        nature_cost = int(input('Please enter the price of Nature Runes at this time: '))
    
        item_cost = int(input('Please enter the price of a item from when you bought it: '))

        highalch = int(input('Please enter the high-alch price of the item: '))

        amount = int(input('How many items are there?: '))

        total_item_price = (item_cost * amount)
        highalch_profit = (highalch * amount)
        nature_price = (nature_cost * amount)

        margin = (highalch_profit - (total_item_price + nature_price))

        cast_time = (amount / 20)
        total_time = cast_time
                 
        if margin < 0:
            print()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('This will not make a profit, sell back to G.E immediately.')
        else:
            print()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('The total profit is', margin, 'GP,')
            print('and takes about', total_time, 'minutes to fully alch.')
    except:
        print('This will occur if you add something that isnt a number')
        print('Restarting the program...')
        import time
        time.sleep(2)
        restart(calc())
        
def restart():
    try:
        prompt = input("Restart program? Type yes/no or y/n: ")
        
        if prompt == 'yes' or prompt == 'y':
            restart(main())
        if prompt == 'n' or prompt == 'no':
            import time
            print('Ending program...')
            time.sleep(1)
 
    except:
        print('This will happen if a key that isnt the prompt is used.')
        print('This will also happen if the IDLE Editor is used to run this program.')
        print('Restarting the program...')
        import time
        time.sleep(2)
        restart()
       
main()
    

