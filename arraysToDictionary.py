states_shortform = ["CA", "NJ", "RI", "NY"]
states = ["California", "New Jersey", "Rhode Island", "New York"]  
answer = {}
for i in range(len(states)): 
    answer[states_shortform[i]] = states[i] 
print(answer)