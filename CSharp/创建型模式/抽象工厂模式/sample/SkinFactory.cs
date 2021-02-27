// SkinFactory.cs
namespace AbstractFactorySample
{
    interface SkinFactory
    {
        Button CreateButton();
        TextField CreateTextField();
        ComboBox CreateComboBox();
    }
}