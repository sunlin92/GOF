// Program.cs
namespace AbstractFactorySample
{
    class Program
    {
        static void Main(string[] args)
        {
            SkinFactory skinFactory = new SpringSkinFactory();// 通过配置文件+反射可以避免修改源代码

            Button button = skinFactory.CreateButton();
            TextField textField = skinFactory.CreateTextField();
            ComboBox comboBox = skinFactory.CreateComboBox();

            button.Display();
            textField.Display();
            comboBox.Display();
        }
    }
}