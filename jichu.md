### 基础知识点

```python
单例模式：一种常用的软件设计模式，该模式主要目的是确保某一个类只有一个实例的存在。当你希望整个系统中，只有一个实例的时候，单例就能派上用场。
比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。
python中实现单例的模式：
	#使用模块
    #使用__new__
    #使用装饰器
    #使用元类
1 使用模块
	Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做
#mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass
my_singleton=My_Singleton()

这样使用：
from mysingleton import my_singleton
my_singleton.foo()

2.使用__new__
为了使类只能出现一个实例 ，我们可以使用__new__ 来控制实例的创建过程 代码如下：
	class Singleton(object):
        _instance = None
        def __new__(cls,*args,**kw):
            if not cls._instance:
                cls._instance = super(Singleton,cls).__new__(cls,*args,**kw)
            return cls._instance
     class MyClass(Singleton):
        a = 1
在上面的代码中，我们将类的实例和一个类变量 _instance 关联起来，如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance。
执行情况：
>>> one = MyClass()
>>> two = MyClass()
>>> one == two
True
>>> one is two
True
>>> id(one), id(two)
(4303862608, 4303862608)

3.使用装饰器
我们知道，装饰器（decorator）可以动态地修改一个类或函数的功能。这里，我们也可以使用装饰器来装饰某个类，使其只能生成一个实例，代码如下：
from functools import wraps
def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args,**kw):
        if cls not in instances:
            instance[cls] = cls(*args,**kw)
        return instances[cls]
    return getinstance

@singleton()
class MyClass(object):
    a = 1
在上面，我们定义了一个装饰器 singleton，它返回了一个内部函数 getinstance，该函数会判断某个类是否在字典 instances 中，如果不存在，则会将 cls 作为 key，cls(*args, **kw) 作为 value 存到 instances 中，否则，直接返回 instances[cls]。

4.使用元类 metaclass
元类主要（metaclass）可以控制类的创建过程，它主要做三件事：
	#拦截类的创建
    #修改类的定义
    # 返回修改后类的定义
使用元类实现单例模式的代码如下：
class Singleton(type):
    _instance = {}
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            cls._instance[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]
 #python2
class Myclass(object):
    __metaclass__ = Singleton

#python3
class MyClass(metaclass=Singleton):
    pass
```

```python
共享属性
创建实例时把所有的__dict__指向同一字典这样它们就友相同的属性和方法
class Borg(object):
    _state = {}
    def __new__(cls,*args,**kw):
        ob = super(Blog,cls).__new__(cls,*args,**kw)
		ob.__dict__ = cls.state
        return ob
class MyClass2(org):
    a = 1    
```

```python
装饰器版本
def singleton(cls,*args,**kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instznces[cls] = cls(*args,**kw)
        return getinstance
@singlenton
class MyClass:
    ...
```

```python
Python 中的作用域
python中，一个变量的作用域总是在代码中被赋值的地方所决定
当python遇到一个变量的话会按照这样的顺序进行搜索：
本地作用域（local）-> 当前作用域被嵌入的本地作用域（Eeclosing locals）-> 全局/模块（Global）-> 内作用域（Built in）
```

```python
GLI纤尘全局锁
即为了保证线程安全而采取的独立线程运行的限制，说白了就是一个核只能在同一时间运行一个线程，对于io密集型任务，pyhton的多线程起到作用，但对于cpu密集型的任务，python多线程几乎占不到任何的优势，还可能因为争夺资源而变慢。
解决办法就是协程（协程是单cpu，但能减少切换代价提升性能）
说协程是进程和线程的升级版,进程和线程都面临着内核态和用户态的切换问题而耗费许多切换时间,而协程就是用户自己控制切换的时机,不再需要陷入系统的内核态.Python里最常见的yield就是协程的思想
```

