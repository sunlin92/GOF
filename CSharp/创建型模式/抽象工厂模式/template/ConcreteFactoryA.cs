// AbstractFactoryA.cs
namespace AbstractFactory
{
    class ConcreteFactoryA : Factory
    {
        // 工厂方法一
        public override AbstractProductA CreateProductA()
        {
            return new ConcreteProductA1();
        }
        // 工厂方法二
        public override AbstractProductB CreateProductB()
        {
            return new ConcreteProductB1();
        }
    }
}