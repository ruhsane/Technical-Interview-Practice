def convert(number):

    raindrop = ''
   
    # divide the number with every number (from 1 up to number)
    for i in range(1, number + 1):

        # if it is perfectly divided, means it's a factor
       if number % i == 0:

           # check the factor and concatinate appropriate return result
            if i == 3:
               raindrop += 'Pling'
            if i == 5:
                raindrop += 'Plang'
            if i == 7: 
                raindrop += 'Plong'
    
    # if nothing was concatinated, just return the number in string form
    if raindrop == '':
        return str(number)
    else: 
        return raindrop