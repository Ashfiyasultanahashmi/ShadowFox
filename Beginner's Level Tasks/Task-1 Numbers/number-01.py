#1. Write a function that takes two arguments, 145 and 'o', and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used.
def format_representation(num):
    return format(num,'o')
answer=format_representation(145)
print(f'The answer is: {answer}')  
