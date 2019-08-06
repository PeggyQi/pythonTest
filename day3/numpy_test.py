import numpy as np
#数组创建
ar=np.array([1,2,3]) #[1 2 3]
ar=np.array([[1,2,3],[3,4,5],[6,7,8]])
'''[[1 2 3]
 [3 4 5]
 [6 7 8]]'''
ar=np.array([1,2,3],dtype=str) #['1' '2' '3']
ar=np.array([1,2,3],ndmin=3) #[[[1 2 3]]]

#dtype规定数据类型
student = np.dtype([('name','S2'), ('age', 'i1'), ('marks', 'f4')])
ar = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
# print(ar)
# print(ar['name'])
# [(b'ab', 21, 50.) (b'xy', 18, 75.)]
# [b'ab' b'xy']