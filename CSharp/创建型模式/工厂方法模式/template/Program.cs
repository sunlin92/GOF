// Program.cs
using System;

namespace FactoryMethod
{
    class Program
    {
        static void Main(string[] args)
        {
            Factory factory = new ConcreteFactoryA();
            Product product = factory.FactoryMethod();
        }
    }
}
