import UIKit

/*:
 Give an array of integers, return an array of integers such that the value at index i of the output is the product of everything in the input except the element at i:

 input: [1,2,3,4]
 
 output: [24,12,8,6]
 
 input: [1,2,0,4]
 
 output: [0,0,8,0]
 */

//using higher order function
var input = [1,2,0,4]
var output = [Int]()

for i in 0...(input.count - 1) {
    var temp_array = input
    temp_array.remove(at: i)
    let product = temp_array.reduce(1) { $0 * $1 }
    output.append(product)
}

print(output)


// without higher order function
var start = [1,2,3,4]
var final = [Int]()

for i in 0...(start.count - 1) {
    var temp_arr = start
    temp_arr.remove(at: i)
    var prod = 1

    for i in temp_arr{
        prod = prod * i
    }
    
    final.append(prod)
}

print(final)


// without using temp variable
var array = [1,2,3,4]
var answer = [Int]()
var numToMultiply = 1

for i in 0...(array.count - 1) {
    var counter = 0
    var divideI = 1
    
    for i in array{
        numToMultiply = numToMultiply * i
//        print("counter:", counter)
//        print(numToMultiply)
//        print(divideI)
        
        counter += 1

    }
    
    divideI = numToMultiply/array[counter-1]

    answer.append(divideI)
}

print(answer)

//first function to multiple all of them
//seconf function to go in to each of the array, and divide it by the product of the whole thing; each time add to answer array
/*:
 implement a stack with the following methods:
 
 stack:
 
 function push: puts an item on top of the stack
 
 function pop: removes an element from the top of the stack
 
 function peek: return the top eleent on the stack
 
 function is_empty: returns true if elements are in the stack, else, return false
 
 function max: return the ax value in the stack
 
 */

