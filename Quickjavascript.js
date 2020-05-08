Check if a particular key exists in a JavaScript object

var obj = { key: undefined };
obj["key"] !== undefined // false, but the key exists!

"key" in obj // true, regardless of the actual value

!("key" in obj) // true if "key" doesn't exist in object
!"key" in obj   // ERROR!  Equivalent to "false in obj"

Or, if you want to particularly test for properties of the object instance (and not inherited properties), use hasOwnProperty:
obj.hasOwnProperty("key") // true

----------------------------------------------------------

