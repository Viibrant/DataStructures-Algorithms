stack = __import__("2-stack")

# Implement an algorithm that
#   returns whether the brackets in a string
#   are valid or not if they're closed
#
# e.g.
#
# (abc)         -->     True
# [ds](alg)     -->     True
# [a{b]}        -->     False


def check_brackets(string: str):
    open_br = ["[", "(", "{"]
    close_br = ["]", ")", "}"]

    output = stack.Stack()
    output.push(string[0])
    for i in string[1:]:
        # Check if character is a bracket
        if not output.is_empty() and i in "{}[]()":
            if i in open_br:
                output.push(i)
            elif i in close_br:
                # If valid then bracket in stack should match i
                index = open_br.index(output.pop())
                if close_br[index] != i:
                    return False
    if not output:
        return False
    return True


print(check_brackets("(abc)"))
print(check_brackets("[ds](alg)"))
print(check_brackets("[a{b]}"))
