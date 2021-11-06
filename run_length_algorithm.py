#import numpy as np

def run_length(input):
    output = ''
    count = 1
    char = input[0]
    for i in range(1, len(input)):
        if input[i] == char:
            count = count + 1
        else:
            output = output + char + str(count)
            char = input[i]
            count = 1
    output = output + char + str(count)
    return output