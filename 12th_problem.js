// Reverse a string

let some_str = 'Hello';

// Place algorithm in a function

function reverse_string(string_item) {

// Define start and end of the string and temporary variable
// for keeping the first character
    let start = 0, end = string_item.length - 1;
    let tmp;
// Make string an array to avoid problems with string
    string_item = string_item.split('');
    while (start<end) {
        tmp = string_item[start];
        string_item[start]=string_item[end];
        string_item[end] = tmp;
        start++;
        end--;
        }
// Make array back to string
    string_item = string_item.join('');
    console.log(string_item);
}

reverse_string(some_str)