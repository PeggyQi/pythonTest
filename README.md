# pythonTest
学习python练习代码

## Numpy

## 创建数组 
N维数组对象ndarray,一系列同一类型的数据集合，以0开始  
```numpy.array(object,dtype=None,copy=True,order=None,subok=False,ndmin=0)    np.array([[1,2],[3,4]])  np.arange(12)```

名称|描述
-|-
object|数组或嵌套的数列
dtype|数组元素的数据类型，可选
copy|对象是否需要复制，可选
order|创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
subok|默认返回一个与基类类型一致的数组
ndmin|指定生成数组的最小维度

实例
详见day3 numpy_test.py

### 数据类型
numpy支持的数据类型比Pyhon内置的类型要多,numpy 的数值类型实际上是 dtype 对象的实例，并对应唯一的字符，包括 np.bool_，np.int32，np.float32  

名称|描述
-|-
bool_|布尔型数据类型（True 或者 False）
int_|默认的整数类型（C语言中的long int32 int64）
intc|int32 int64
intp|用于索引的整数类型，一般情况下是int32 int64
int8|字节（-128 to 127）
int16	|整数（-32768 to 32767）
int32	|整数（-2147483648 to 2147483647）
int64	|整数（-9223372036854775808 to 9223372036854775807）
uint8	|无符号整数（0 to 255）
uint16|无符号整数（0 to 65535）
uint32	|无符号整数（0 to 4294967295）
uint64	|无符号整数（0 to 18446744073709551615）
float_	|float64 类型的简写
float16	|半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32	|单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	|双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
complex_	|complex128 类型的简写，即 128 位复数
complex64	|复数，表示双 32 位浮点数（实数部分和虚数部分）
complex128	|复数，表示双 64 位浮点数（实数部分和虚数部分）

### 数组属性
数组的维数成为秩，每一个线性的数组是一个轴axis，第一个轴相当于是底层数组，第二个轴是底层数组里的数组。axis=0，表示沿着第0轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。

ndarray对象属性

属性|说明
-|-
ndarry.ndim|秩
ndarray.shape|维度
ndarray.size|元素总个数
ndarray.dtype|ndarray对象的元素类型
ndarray.itemsize|ndarray对象中每个元素的大小，以字节为单位
ndarray.flags|	ndarray 对象的内存信息
ndarray.real|ndarray元素的实部
ndarray.imag|	ndarray 元素的虚部
ndarray.data|	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

实例详见 numpy_test/numpy_array.py

