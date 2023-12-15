'''defining basic functions to implement stack(LIFO) using linked list'''

class Empty(Exception):
    '''Error raised while attempting to access an element from an empty container'''
    pass

class LinkedStack:
    '''LIFO stack implementation using a singly linked list'''

    ########nested Node Class
    class Node:
        '''class for storing a singly linked node'''
        __node__=['_element','_next']           #streamline memory usage

        def __init__(self, element, next):      #initialize node's field
            self._element = element             #reference to element
            self._next=next                     #reference to next node

    ########Stack Methods
    def __init__(self):
        '''create an empty stack'''
        self._head=None                         #reference to head node
        self._size=0                            #size of empty stack is 0

    def is_empty(self):
        '''returns True if the stack is empty'''
        output= (self._size==0)
        return output

    def top(self):
        '''Return but not remove the element at the top of the stack'''
        if self.is_empty():                     #Raise Empty exception if the stack is empty
            raise Empty('Stack is empty')
        '''top of stack is at the head of the list'''
        return self._head._element              

    def push(self,data): 
        '''adds elements data to the top of the stack by creating and linking a new node'''       
        self._head= self.Node(data,self._head)
        self._size+=1                           #size of stack increases by 1

    def pop(self):
        '''Remove and return the element at the top of the stack'''
        if self.is_empty():                             #Raise Empty exception if the stack is empty
            raise Empty('Stack is empty')
        output = self._head._element                    #top of stack is at head of list
        self._head = self._head._next                   #bypass the current node
        self._size -=1                                  #size of stack decreases by 1
        return output

############################

def findPositionandDistance(P):
    '''
    takes a string P as input and return a list [x,y,z,d] of four numbers
    where (x,y,z) is the final position of the drone afterexecuting program P
    and d is total distance travelled by the drone in this process
    '''

    n = len(P)                                          #calculate the length of input string P in O(1)
    x=y=z=0
    d = 0
        
    stack = LinkedStack()                               #create empty stack
    stack.push(1)                                       #push element 1 into the stack
    i = 0

    while(i < n):
        '''
        traverse over each element of string until it reaches end and calculate coordinates (x,y,z) and distance d by index slicing of string and comparing the duo of sign 
        and character until an integer or bracket comes. For integer, j(another variable initially equal to i) traverse till open bracket is encountered and the index [i:j] 
        contains the number which is in multiple of string(drone program) in bracket after it in string form which is converted into integer and push into the 
        stack and in case of continous multiples the string of multiple is converted into integer and then multiplied by the last member of stack and then push into the stack
        (to calculate the total times the operation is performed). Stack stores the number of times the operations(duo of sign and character/drone program) is performed so 
        during calculation for x/y/z the last element of stack which represents the number of times the operation occurred is added to the previous values of x/y/z. And whenever 
        closed bracket,i.e.,')' is encounter the last element of stack is popped out to eliminate the multiples whose values have been added 
        '''
        '''
        for example, when P='+X+Z9(5(+Y))' : iterations will be
        initially x=y=z=d=0 and stack contains only 1 element that is 1 in form of linked list (for representation here I write it as stack=[1]. In code stack is implemented using linked lists)
        i=0     satisfies '+X' condition                        i=0+2=2 & x=0+1=1 & d=0+1=1                     [1,0,0,1] & stack=[1]
        i=2     satisfies '+Z' condition                        i=2+2=4 & z=0+1=1 & d=1+1=2                     [1,0,1,2] & stack=[1]
        i=4     encounters number 9 else part is executed       j=i=4->j=j+1 till'('->j=5->i=j+1=6              [1,0,1,2] & stack=[1,9] 
        i=6     encounters number 5 else part is executed       j=i=6->j=j+1 till'('->j=7->i=j+1=8              [1,0,1,2] & stack=[1,9,45]
        i=8     satisfies '+Y'condition                         i=8+2=10 & y=0+45=45 & d=2+45=47                [1,45,1,47] & stack=[1,9,45]
        i=10    satisfies ')' condition                         i=i+1=11 & last element of stack is popped      [1,45,1,47] & stack=[1,9]
        i=11    satisfies ')' condition                         i=i+1=12 & last element of stack is popped      [1,45,1,47] & stack=[1]
        i=12    i is not less than n(n=12), thus loop ends
        '''

        if (P[i:i+2] == "+X"):                                              #comparing duo of sign and character 
            i += 2                                                          #increase by 2 because 2 elements sign and character have been traversed
            x+=stack.top()                                                  #calculation of x coordinate by adding the multiple of that particular operation
            d += stack.top()                                                #distance is net sum of all absolute values of steps drone took
                
        elif(P[i:i+2] == "-X"):
            i += 2
            x+=(-stack.top())                                               #for coordinates it is subtracted because of movement in negative x axis
            d += stack.top()
                        
    #Similarly for +Y,-Y,+Z,-Z
       
        elif(P[i:i+2] == "+Y"):
            i += 2
            y+=(stack.top())
            d += stack.top()
                        
        elif(P[i:i+2] == "-Y"):
            i += 2
            y+=(-stack.top())
            d += stack.top()
        
        elif(P[i:i+2] == "+Z"):
            i += 2
            z+=(stack.top())
            d += stack.top()

                
        elif(P[i:i+2] == "-Z"):
            i += 2
            z+=(-stack.top())
            d += stack.top()
        
        elif(P[i] == ')'):                  
            '''the last element of stack is popped out to eliminate the multiples whose values have been added '''
            stack.pop()
            i += 1
        
        else:
            j = i                                                           #assigning value of i to j
            while(P[j] != '('):
                '''traversing over integers'''
                j += 1

            num = 1                                                         #initializing num to 1 for base case

            if(i != j):
                '''when there is some integer in multiple of some operation, convert that into integer via string slicing'''
                num = int(P[i:j])
            
            '''pushing multiple of operation into stack after calculating net value of multiple by multiplying it to the previous value in stack'''
            stack.push(num*(stack.top()))                                   
            i = j + 1                                                       #reassigning i to j+1 for further traversing

    '''return list of four elements that gives the final coordinates of drone (x,y,z) and total distance d covered by the drone in the process'''            
    return([x,y,z,d])
        
print(findPositionandDistance(input()))