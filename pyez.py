import random , time
arr = ["surrounded by idiots" , "atomic habits" , "why do men love whores" , "The Subtle Art of Not Giving a F*ck" , "Think Again" , "Deep Work" , "The 7 Habits of Highly Effective People" , "The Power of Now"]
"""
def russianroullet(arr):
    if not arr:
        print("game over")
    index = random.randint(0,len(arr)-1)
    deleted_book = arr.pop(index)
    print(f"Bang , the book {deleted_book} was erased from the list")
    print(f"Remaining books: {arr}")
    return deleted_book
russianroullet(arr)
"""
def removeall(arr):
    
    while arr :
        deleted_bok = arr.pop(0)
        print(f"the book {deleted_bok} has been deleted !")
        time.sleep(1)
        if not arr :
            print("the list now is empty")
            return
    return deleted_bok
removeall(arr)

"""
for py in range (5):
    print(f"here is text number {py}")
    py += 1
c = 2
def add(a,b):
    return a+b
add(py,c)
"""