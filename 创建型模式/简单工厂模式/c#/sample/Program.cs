// Program.cs
using System;

namespace SimpleFactorSample
{
    class Program
    {
        static void Main(string[] args)
        {
            Chart chart = ChartFactory.GetChart("Pie");//通过静态工厂方法创建产品
            chart.Display();
            Console.Read();
        }
    }
}