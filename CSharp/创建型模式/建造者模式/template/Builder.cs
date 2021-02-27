namespace Builder
{
    abstract class Builder
    {
        // 创建产品对象
        protected Product product = new Product();

        public abstract void BuildPartA();
        public abstract void BuildPartB();
        public abstract void BuildPartC();


        // 返回产品对象
        public Product GetResult()
        {
            return product;
        }
    }
}