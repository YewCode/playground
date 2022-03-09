def garys_hike(s):
   """Q18: Gary's Hike [*****]"""

   pass


if __name__ == '__main__':
   import textwrap

   print('\n', garys_hike.__doc__.upper(), '\n')

   print('---------------[ Test Case 1 ]---------------')
   print('Expected output:')
   print(textwrap.dedent(r'''
   _/\      _
      \    /
      \/\/'''))

   print('\nActual output:\n')
   garys_hike('UDDDUDUU')

   print('---------------[ Test Case 2 ]---------------')
   print('Expected output:')
   print(textwrap.dedent(r'''
   _                     
   \                    
   \                   
      \/\                
         \               
         \            /\_
         \    /\    /  
            \/\/  \  /   
                  \/'''))

   print('\nActual output:\n')
   garys_hike('DDDUDDDDDUDUUDDDUUUUD')

   print('---------------[ Test Case 3 ]---------------')
   print('Expected output:')
   print(textwrap.dedent(r'''
                           _
                        /
               /\      / 
               /  \  /\/  
               /    \/     
            /            
            /             
   _        /              
   \      /               
   \    /                
      \/\/'''))

   print('\nActual output:\n')
   garys_hike('DDDUDUUUUUUUUUDDDUUDUUU')

   print('---------------[ Test Case 4 ]---------------')
   print('Expected output:')
   print(textwrap.dedent(r'''
                     /\
                  /  \
                  /    \
                  /      \    /\
               /        \  /  \      _
               /          \/    \  /\/
               /                  \/
   _          /
   \        /
   \      /
      \/\  /
         \/'''))

   print('\nActual output:\n')
   garys_hike('DDDUDDUUUUUUUUUUUUDDDDDDUUUDDDDUUDU')

   print('---------------[ Test Case 5 ]---------------')
   print('Expected output:')
   print(textwrap.dedent(r'''
      /\                                                          
      /  \                                                         
   /    \                                                        
   _/      \                                                       
            \/\/\/\                      /\                        
                  \/\/\                /  \                       
                        \              /    \                      
                        \            /      \                     
                        \/\        /        \                    
                           \      /          \              /\   
                              \/\/\/            \            /  \  _
                                                \/\        /    \/
                                                   \      /       
                                                   \    /        
                                                      \  /         
                                                      \/'''))

   print('\nActual output:\n')
   garys_hike('UUUUDDDDDUDUDUDDUDUDDDDUDDDUDUDUUUUUUUDDDDDDDDUDDDDDUUUUUUUDDDU')
