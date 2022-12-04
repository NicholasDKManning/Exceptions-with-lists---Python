names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

try:
    
    if index in range(-10, -1):
        
        print(f'Name: {names[index]}')    
    
    
    if index in range(0, 9):
        
        print(f'Name: {names[index]}')

    if index > 9:
        
        raise IndexError('The closest name is: Johnny')
        
        
    if index < -10:
        
        raise IndexError('The closest name is: Ryley')
        
        
except IndexError as excpt:
    
    print(f'Exception! list index out of range')
    
    print(excpt)
    
    