# Aggregate Functions
a.sum()
a.min()
a.max()
a.mean()
np.median(a)
np.std(a)

a.reshape(x,y)
a.flatten() # Returns flattenend one dimentional array
a.ravel() # same as flatten, but flattens original array
a.transpose()
a.swapaxes()
a.flat - Not a function, jut an iterator for flattened version of array


#Joining
np.concatenate(x,y)
np.stack(a,b)
np.hstack(a,b)
np.vstack(a,b)

np.append(a,[...])

# Saving and Reading Files
np.save('myfile.npy', a) # Save in Numpy Format
#CSV Format
np.savetxt('myfile.txt', a)
a = np.loadtxt('myfile.txt')
a = np.loadtxt('myfile.csv', delimiter=';')
