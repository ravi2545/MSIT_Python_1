def fun(items):
    if not items:
        return

    
    print(items)
    fun(items[1:])


fun([0,1,2])
