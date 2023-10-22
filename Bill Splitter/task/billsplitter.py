# write your code here
from random import choice

print('Enter the number of friends joining (including you):')
friends_num = int(input())

if friends_num <= 0:
    print('\nNo one is joining for the party')
else:
    friends_list = {}
    print('\nEnter the name of every friend (including you), each on a new line:')
    for i in range(friends_num):
        friend_name = input()
        friends_list[friend_name] = 0

    print('\nEnter the total bill value:')
    full_bill_val = int(input())
    one_bill_val = round(full_bill_val / friends_num, 2)

    for friend_name in friends_list:
        friends_list[friend_name] = one_bill_val

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    answer = answer.lower()
    if answer == 'yes':
        random_name = choice(list(friends_list.keys()))
        print(f'\n{random_name} is the lucky one!')
        one_bill_val = round(full_bill_val / (friends_num - 1), 2)
        friends_list = {name: one_bill_val for name in friends_list}
        friends_list[random_name] = 0
    else:
        print('\nNo one is going to be lucky')

    print(f'\n{friends_list}')
