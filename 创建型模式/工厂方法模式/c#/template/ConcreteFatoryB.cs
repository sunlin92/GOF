// ConcreteFactoryA.cs
namespace FactoryMethod
{
    class ConcreteFactoryB : Factory
    {
        public Product FactoryMethod()
        {
            return new ConcreteProductB();
        }
    }
}