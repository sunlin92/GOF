// Program.cs
using System;

namespace SimpleFactorSample
{
    class Program
    {
        static void Main(string[] args)
        {
            Chart chart = ChartFactory.GetChart("pie");//通过静态工厂方法创建产品
            chart.Display();
        }
    }
}