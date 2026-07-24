# syntax
st = set()
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
# syntax
st = {'item1', 'item2', 'item3', 'item4'}

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)


# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True


# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')


fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)


fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
