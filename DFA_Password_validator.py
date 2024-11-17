from automata.fa.dfa import DFA

"""
The Goal of this code is to 
create a simple DFA that validates 
passwords based on specific criteria.

The password must have the following criteria: 
- At least 8 characters long 
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit 
- May contain special characters like: $%@^#@!

1. (S0) Start State: Initial state before any character is read.
2. (S1) Length Check State: Indicates that the password has at least 8 characters.
3. (S2) At least one Uppercase letter is found.
4. (S3) At least one Lowercase letter is found.
5. (S4) At least one Digit is found.
6. Accept state (SA): The final state indicating a valid password.
7. Reject state (SR): Indicates that the password is invalid.
"""

# Define states
states = {
    'S0': 'Start State',
    'S1': 'Length Check State',
    'S2': 'Upper Case Check State',
    'S3': 'Lowercase Check State',
    'S4': 'Digit Check State',
    'SA': 'Accept State',
    'SR': 'Reject State'
}

# Define transitions
transitions = {
    'S0': { 'length_check': 'S1' },
    'S1': { 'upper_case': 'S2', 'lower_case': 'S3', 'digit': 'S4', 'invalid_input': 'SR' },
    'S2': { 'digit': 'S4', 'valid_input': 'SA' },
    'S3': { 'digit': 'S4', 'valid_input': 'SA' },
    'S4': { 'valid_input': 'SA', 'invalid_input': 'SR' },
    'SA': {},  # Accept state (no transitions)
    'SR': {}    # Reject state (no transitions)
}

# Create DFA instance
dfa = DFA(
    states=set(states.keys()),
    input_symbols=set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'),
    transitions=transitions,
    initial_state='S0',
    final_states={'SA'},
    dead_state='SR'
)

# Function to determine character type
def character_type(c):
    if c.isupper():
        return 'upper_case'
    elif c.islower():
        return 'lower_case'
    elif c.isdigit():
        return 'digit'
    else:
        return 'valid_input'  # Special characters treated as valid input

# User input handling
while True:
    input_string = input("Enter a password to validate (or type 'exit' to quit): ")
    if input_string.lower() == 'exit':
        break

    # Check length first
    if len(input_string) < 8:
        print(f"The input '{input_string}' is rejected due to insufficient length.")
        continue
    
    current_state = 'S0'
    for char in input_string:
        char_type = character_type(char)
        if char_type in transitions[current_state]:
            current_state = transitions[current_state][char_type]
        else:
            current_state = 'SR'  # Transition to reject state for invalid input
            break

    # Final state check
    if current_state in dfa.final_states:
        print(f"The input '{input_string}' is accepted.")
    else:
        print(f"The input '{input_string}' is rejected.")
