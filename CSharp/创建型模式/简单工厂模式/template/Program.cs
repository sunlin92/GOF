// Program.cs
namespace SimpleFactor
{
    class Program
    {

        static void Main(string[] args)
        {
            Product product;
            product = Factory.GetProduct("A");// 通过工厂类创建产品对象
            product.MethodSame();
            product.MethodDiff();
        }
    }
}