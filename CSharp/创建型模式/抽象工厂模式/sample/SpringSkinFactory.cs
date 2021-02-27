//SpringSkinFactory.cs
namespace AbstractFactorySample
{
    class SpringSkinFactory : SkinFactory
    {
        public Button CreateButton()
        {
            return new SpringButton();
        }
        public TextField CreateTextField()
        {
            return new SpringTextField();
        }
        public ComboBox CreateComboBox()
        {
            return new SpringComboBox();
        }
    }
}