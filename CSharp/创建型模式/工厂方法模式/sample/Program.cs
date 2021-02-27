// Program.cs
using System;

using System.Configuration;
using System.Reflection;
namespace FactoryMethodSample
{
    class Program
    {
        static void Main(string[] args)
        {
            LoggerFactory factory = new FileLoggerFactory(); // 通过配置文件+反射可以避免修改源代码
            Logger logger = factory.CreateLogger();
            logger.WriteLog();
        }
    }
}
