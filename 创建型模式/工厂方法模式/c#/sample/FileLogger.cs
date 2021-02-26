// FileLogger.cs
using System;
namespace FactoryMethodSample
{
    class FileLogger : Logger
    {
        public void WriteLog()
        {
            Console.WriteLine("文件日志记录");
        }

    }
}