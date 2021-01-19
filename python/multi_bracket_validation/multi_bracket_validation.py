def multi_bracket_validation(input):
    openstack = []
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    if len(input) % 2 != 0:
        return False
    for char in input:
        if char in opening:
            openstack.append(char)
        if char in closing:
            pope = openstack.pop()
            if not compare(pope, char):
                return False
        #         print(len(openstack))
        #         return False
            else:
                return True


def compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    if opening == '{' and closing == '}':
        return True  


if __name__ == "__main__":
    multi_bracket_validation("([{(})]")

