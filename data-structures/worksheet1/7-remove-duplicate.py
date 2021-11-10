stack = __import__("2-stack")
# Implement an algorithm that
#   removes duplicate letters
#   from an input string until there are no more
#
# e.g.
#
# "abbccd"      -->     "ad"
# "dsallasg"    -->     "dg"
# "abccbadd"    -->     ""


def remove_duplicates(string: str):
    output = stack.Stack()
    output.push(string[0])

    for i in string[1:]:
        if not output.is_empty():
            if i == output.peek():
                output.pop()
            else:
                output.push(i)
        else:
            output.push(i)
    return output.items
