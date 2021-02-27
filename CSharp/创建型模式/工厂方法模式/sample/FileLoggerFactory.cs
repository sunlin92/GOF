// FileLoggerFactory.cs
namespace FactoryMethodSample
{
    class FileLoggerFactory : LoggerFactory
    {
        public Logger CreateLogger()
        {
            Logger logger = new FileLogger();
            return logger;
        }
    }
}