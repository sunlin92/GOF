// Program.cs
using System;

namespace Builder
{
    class Program
    {
        static void Main(string[] args)
        {
            Builder builder = new ConcreteBuilderA();// 通过配置文件+反射可以避免修改源代码

            Director director = new Director(builder);
            Product product = director.Construct();
        }
    }
}
