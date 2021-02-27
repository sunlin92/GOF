// DatabaseLoggerFactory.cs
namespace FactoryMethodSample
{
    class DatabaseLoggerFactory : LoggerFactory
    {
        public Logger CreateLogger()
        {
            Logger logger = new DatabaseLogger();
            return logger;
        }
    }
}