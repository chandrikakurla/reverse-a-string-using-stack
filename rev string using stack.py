def createStack():
    stack=[]
    return stack
def isEmpty(stack):
    if len(stack)==0:
        return True
def push(stack,data):
    stack.append(data)
def pop(stack):
    if not isEmpty(stack):
        return stack.pop()
def rev(string):
    n=len(string)
    stack=createStack()
    for i in range(n):
        push(stack,string[i])
    string=""
    for i in range(n):
        string=string+pop(stack)
    return string
if __name__=="__main__":
    string=input("enter string")
    string=rev(string)
    print(string)
        

