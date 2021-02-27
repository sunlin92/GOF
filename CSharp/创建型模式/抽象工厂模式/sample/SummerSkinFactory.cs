//SummerSkinFactory.cs
namespace AbstractFactorySample
{
    class SummerSkinFactory : SkinFactory
    {
        public Button CreateButton()
        {
            return new SummerButton();
        }
        public TextField CreateTextField()
        {
            return new SummerTextField();
        }
        public ComboBox CreateComboBox()
        {
            return new SummerComboBox();
        }
    }
}