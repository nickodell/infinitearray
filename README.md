An infinite and sparse array; automatically set to all zeros.

##Example

    from infinitearray import infarray
    
    a = infarray('B')
    a[5] = 42
    print a[5] # prints 42

##How do you put an infinite array into a finite amount of memory?

Array elements aren't created until you set them.

##Is this a drop-in replacement for array?

Nope. It's got `array[index]`, and that's it.

##Why'd you write this?

Kept wishing for a library like this.

##Dependencies?

Python 2.5
