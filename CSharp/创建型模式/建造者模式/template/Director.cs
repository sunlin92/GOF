namespace Builder
{
    class Director
    {
        private Builder builder;
        public Director(Builder builder)
        {
            this.builder = builder;
        }

        public void SetBuilder(Builder builder)
        {
            this.builder = builder;
        }
        // 产品构建与组装方法
        public Product Construct()
        {
            builder.BuildPartA();
            builder.BuildPartB();
            builder.BuildPartC();
            return builder.GetResult();
        }

    }
}