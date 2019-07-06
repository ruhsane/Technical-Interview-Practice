import UIKit

/*:
given 2d array of ones and zeros, where ones represents represent islands and zeros represent water, find the height of the island if there can only be one island

[[0, 0, 0, 0],
 
[0, 1, 1, 1],
 
[0, 1, 1, 1],
 
[0, 1, 1, 1]]
 

The question was to find "islands" in the nested arrays
The "islands" are the adjacent zeros
You need to return the location of the islands (coordinates) as well as the height and the width
*/

let nested = [[0, 0, 0, 0, 0, 0, 0, 0],
              
              [0, 1, 1, 1, 0, 0, 0, 0],
          
              [0, 1, 1, 1, 0, 0, 0, 0],
          
              [0, 1, 1, 1, 0, 0, 0, 0],
    
              [0, 0, 0, 0, 0, 0, 0, 0],

]

var height = 0
var haveOne = Bool()
var width = 0

func findWidthHeight() -> String {
    for row in nested {
        width = 0

        for element in row {
            if element == 1 {
                haveOne = true
                width += 1
            }
        }
        
        if haveOne == true {
            height += 1
        }
    }
    return("Height:" + String(height) + ", Width:" + String(width))
}


print(findWidthHeight())
