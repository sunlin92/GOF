// AbstractFactory.cs
namespace AbstractFactory
{
    // 工厂抽象类
    abstract class Factory
    {
        public abstract AbstractProductA CreateProductA(); // 工厂方法一
        public abstract AbstractProductB CreateProductB(); // 工厂方法二
    }
}