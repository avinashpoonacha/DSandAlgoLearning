from random.stackimpl import stackimpl as stackAvi


stk = stackAvi()
print(stk.description)
stk.push('1')
stk.push(2)
stk.push(79)
print(stk.size())
print(stk.peek())
print(stk.size())

stk.clear()

print(stk.size())