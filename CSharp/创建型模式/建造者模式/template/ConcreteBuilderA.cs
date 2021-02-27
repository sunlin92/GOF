// ConcreteBuilderA.cs
namespace Builder
{
    class ConcreteBuilderA : Builder
    {
        public override void BuildPartA()
        {
            product.PartA = "A1";
        }
        public override void BuildPartB()
        {
            product.PartA = "B1";
        }
        public override void BuildPartC()
        {
            product.PartA = "C1";
        }
    }
}