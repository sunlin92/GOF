// ConcreteFactoryA.cs
namespace FactoryMethod
{
    class ConcreteFactoryA : Factory
    {
        public Product FactoryMethod()
        {
            return new ConcreteProductA();
        }
    }
}