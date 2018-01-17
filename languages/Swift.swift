import UIKit

//: Constants and Variables
let const = "a constant" // Can only be assigned once but does not need to be known at compile time
var varies = "variable";


//: Declaring type explicitly
var myName: String
myName = "Suyash"

let implicitInteger = 70
let implicitDouble = 70.0
let explicitDouble: Double = 70


//: Type Casting
let optionalInteger: Int?
let integer: Int
let string: String
let double: Double

optionalInteger = Int("45")
integer = Int(32.4)
string = String(43.5)
double = Double(35)

print (integer)
print (string)
print (double)


//: String Interpolation
let numOfStudents: Int = 26
let numOfTeachers = 2

let classSum: String = "There are \(numOfStudents) students and \(numOfTeachers) teachers in the class."
print (classSum)

//: Arrays
var array = [1,2,3,4,5]
array[2] = 10
print (array)

let varArray:[Any] = [1, "Suyash"]
let allowNilArray:[Int?] = [1, nil]

//: Dictionaries
var dict = [1:"Suyash", 2:"Shekhar", 3:"Haozhe"]

var diffTypeKeysDict: [AnyHashable:String] = [1:"Suyash", 2:"Shekhar", "key":"value"]

print (dict)
print (diffTypeKeysDict)

//: Initialising Empty Arrays and Dictionaries
var emptyArray = [String]()
var emptyDict = [Int:Int]()

//OR

emptyArray = []
emptyDict = [:]

//: Control Flow
let ints = [1,2,3,4,5,6]

for int in ints {
    if int > 3 {
        print(-1 * int)
    } else {
        print(int)
    }
}

var notNill: String
//notNill = nil => Gives Error


//: If Let
// This allows us to safely unwrap an optional. Here, num is sort of a temporary variable which is assigned the unwrapped value of the optionalNum if optionalNum is not nil.

var optionalNum: Int?
if let num = optionalNum {
    print ("I have a value of \(num)")
} else {
    print ("I am nil")
}


//: Guards
// They provide an early exit out of a function should something be nil. You use a guard statement to require that a condition must be true in order for the code after the guard statement to be executed.

func printTriple(num: Int?) {
    guard let num = num else {
        print("Exiting function")
        return
    }

    print("Tripled number is \(num * 3)")
}

printTriple(num: nil)
printTriple(num: 3)

// ANOTHER IMPLEMENTATION
//func printTriple(num: Int?) {
//    if let num = num {
//        print("Tripled number is \(num * 3)")
//    } else {
//        print("Exiting function")
//        return
//    }
//}


//: Force Unwrapping
// This should the last resort. If the value happens to be nil, the program will crash.

let maybeNil: Int?
//let unwrappedNil = maybeNil! => This will throw an error.

maybeNil = 5
let unwrappedNil = maybeNil! // This executes just fine.


//: Optional Chaining
struct Device {
    var type: String
    var cost: Float
    var color: String
}

var myPhone: Device?
let devicePrice = myPhone?.cost

// Here, devicePrice is automatically an optional as well
// let total = devicePrice + 8.99 => This will give an error.
// The right way to unwrap optionalPrice is how we unwrap any optional safely which is by using a if-let

if let price = devicePrice {
    let total = price + 8.99
} else {
    print ("Phone unset")
}



//: Nil Coalescing Operator
//The nil-coalescing operator (a ?? b) unwraps an optional a if it contains a value, or returns a default value b if a is nil. The expression a is always of an optional type. The expression b must match the type that is stored inside a.

//The nil-coalescing operator is shorthand for the code below:
//a != nil ? a! : b

// Example:
let defaultColorName = "red"
var userDefinedColorName: String?   // defaults to nil

var colorNameToUse = userDefinedColorName ?? defaultColorName
// userDefinedColorName is nil, so colorNameToUse is set to the default of "red"


//: Switch Case
let vegetable = "red pepper"
switch vegetable {
case "celery":
    print("Add some raisins and make ants on a log.")
case "cucumber", "watercress":
    print("That would make a good tea sandwich.")
case let x where x.hasSuffix("pepper"):
    print("Is it a spicy \(x)?")
default:
    print("Everything tastes good in soup.")
}


