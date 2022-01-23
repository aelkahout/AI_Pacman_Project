class Stack:

    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

paren_string = input('Give the string')
s = Stack() 
balanced_paren = True 
index = 0
while index < len(paren_string) and balanced_paren:
    # main idea is that we put only the opening parentheses in the stack
    # and remove it once its closing pair is found
    paren = paren_string[index]
    if paren in "[{(":
        s.push(paren)
    else:
        if s.empty():
            balanced_paren = False
        else:
            top_item = s.pop()
            if (top_item + paren) not in ['()', '[]', r'{}']:
                #Checks if top_item + paren create a matching opening-closing parentheses.
                balanced_paren  = False
    index += 1

if s.empty() and balanced_paren:
    # we are checking if the stack is empty to include test cases ending in an opening parentheses
    print('Parentheses are balanced.')
else:
    print('Parentheses are not balanced.')
