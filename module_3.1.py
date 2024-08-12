calls = 0
def count_calls():
   global calls
   calls = calls + 1
def string_info(string):
    count_calls()
    return(len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return(string.lower() in [a.lower() for a in list_to_search])
print(string_info('Pokoloko'))
print(string_info('Elbrus'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)