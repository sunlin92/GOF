// Program.cs
using System;

namespace SimpleFactorSample
{
    class Program
    {
        static void Main(string[] args)
        {
            Chart chart = ChartFactory.GetChart("pie");//通过配置文件+反射可以避免修改源代码
            chart.Display();
        }
    }
}