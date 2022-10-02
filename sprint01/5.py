def toPostFixExpression(e):

    stack = []
    postfix_expression = []
    
    for item in e:
        if item.isalnum():
            postfix_expression.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            top = stack.pop()
            while top != '(':
                postfix_expression.append(top)
                top = stack.pop()
        else:
            stack.append(item)

    while stack:
        postfix_expression.append(stack.pop())
    return postfix_expression


print(toPostFixExpression(["20",
                            "+",
                            "3",
                            "*",
                            "(",
                            "5",
                            "*",
                            "4",
                            ")"]))
