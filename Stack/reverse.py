from stack import Stack

def reverse(input_string):

    s = Stack()

    print(input_string[::-1])
    for i in range(len(input_string)):
        s.push(input_string[i])

    reverse_string = ""

    while not s.is_empty():
        reverse_string += s.pop()

    return reverse_string


print(reverse("siddhartha"))