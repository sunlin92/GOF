// Program.cs
namespace AbstractFactory
{
    class Program
    {
        static void Main(string[] args)
        {
            Factory factory = new ConcreteFactoryA();
            Product productA = factory.CreateProductA();
            Product productB = factory.CreateProductB();
        }
    }
}
