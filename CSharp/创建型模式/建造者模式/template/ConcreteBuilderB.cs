// ConcreteBuilderB.cs
namespace Builder
{
    class ConcreteBuilderB : Builder
    {
        public override void BuildPartA()
        {
            product.PartA = "A2";
        }
        public override void BuildPartB()
        {
            product.PartA = "B2";
        }
        public override void BuildPartC()
        {
            product.PartA = "C2";
        }
    }
}