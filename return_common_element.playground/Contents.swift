import UIKit

/*:
 return common elements between two lists (sorted)
 
 linear time efficiency O(n)
 
 constant space efficiency O(1)
 
 */

let first = [1, 3, 5, 7, 9]
let second = [9, 10, 11, 12, 15, 18]
var commonElements = [Int]()

var int = 0
var int2 = 0

func find() {

    while int < first.count {
        
        if first[int] > second[int2] {
            "Move second index"
            int2 = int2+1
            find()
            
        } else if first[int] < second[int2] {
            "Move first index"
            int = int+1
            find()

        } else {
            commonElements.append(first[int])
            int = int+1
            int2 = int2+1
            find()

        }
    }
}

find()

print(commonElements)
