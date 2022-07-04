import random
import words
import time


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    while index < len(template):
        if template[index:index + len('{{noun}}')] == '{{noun}}':
            output.append(random.choice(nouns))
            index += len('{{noun}}')
        elif template[index:index + len('{{verb}}')] == '{{verb}}':
            output.append(random.choice(verbs))
            index += len('{{verb}}')
        else:
            output.append(template[index])
            index += 1       
            
    # After the loop has finished, join the output and return it.
    return "".join(output)

# To see the results, we need to call the funtion and print what it returns:
while True:
    print(silly_string(words.nouns, words.verbs,
        words.templates))
    time.sleep(2)