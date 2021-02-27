// Factory.cs
namespace SimpleFactor
{
    class Factory
    {
        //静态工厂方法
        public static Product GetProduct(string arg)
        {
            Product product = null;
            if (arg.Equals("A"))
            {
                product = new ConcreteProductA();
                // 初始化设置 product
            }
            else if (arg.Equals("B"))
            {
                product = new ConcreteProductB();
                // 初始化设置 product
            }
            return product;
        }
    }
}