####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Harulius'
strategy_name = 'adapt'
strategy_description = '''\
tries to do its best to defend by using conditionals and does random when it doesn't know what to do
'''

import random
    
def move(my_history, their_history, my_score, their_score):
    
    if len(my_history)==0: # It's the first round; random.
        return random.choice(['b','c'])
        
    if 'c'/'b' in len(their_history) > 0.9: #if their history of colluding is over 90%
            return 'c'               # collude
    elif 'c'/'b' in len(their_history) > 0.6: # if their history of colluding is over 60%
            return 'b'               # betray.
    elif 'b'/'c' in len(their_history) > 0.75: #if their history of betraying is  over 75%
        return 'b'               # betray.
    else:
         return random.choice(['b','c']) # eh random