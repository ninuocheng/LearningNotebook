'''
方法重写
如果子类对继承自父类的某个属性或是方法不满意，可以在子类中对其（方法体）进行重新编写
子类重写后的方法中可以通过super().xxx()调用父类中被重写的方法
'''
# eg:
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('姓名：%s,年龄：%s' % (self.name,self.age))
        # print('姓名: {0},年龄: {1}'.format(self.name,self.age))
# 定义子类
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score
    def info(self):
        super().info()
        print('分数：%s' % (self.score))
        # print('分数:{0}'.format(self.score))
        # print(self.score)
# 测试
stu = Student('Jack',20,1001)
stu.info()