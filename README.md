 # 设计模式的核心套路
 
## _**频繁使用**_

**开闭原则**（Open-Close Principle, OCP)
软件实体应当对扩展开放，对修改关闭。

**里氏替换原则**(Liskov Substitution Principle, LSP)
所有引用基类的地方必须能够透明地使用其子类的对象。

**依赖倒转原则**(Dependence Inversion Principle, DIP)
高层模块不应该依赖底层模块，他们都应该依赖抽象，抽象不应该依赖于细节，细节应该依赖于抽象。 
针对接口编程，不要针对实现编程。

## _**常用**_

**单一职责原则**(Single Responsibility Principle, SRP)
一个对象应该只包含单一的职责，并且该职责被完整地封装在一个类中。
控制类的粒度大小，避免对象过于复杂。

**合成复用原则**(Composite Reuse Principle, CRP)
优先使用对象组合，而不是继承来达到复用的目的。

## _**偶尔**_

**接口隔离原则**(Interface Segregation Principle, ISP)
客户端不应该依赖那些它不需要的接口。

**迪米特法则**(Law of Demeter, LoD)
每一个软件单位对其他的单位都只有最少的知识，而且局限于那些与本单位密切相关的软件单位。
