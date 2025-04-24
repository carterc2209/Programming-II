namespace Pg266LargeSmall
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double num1 = double.Parse(textBox1.Text);
            double num2 = double.Parse(textBox2.Text);
            if (num1 > num2)
            {
                label2.Text = "Smallest Number: " + num2 + "\n" + "Biggest Number: " + num1;
            }
            else
            {
                label2.Text = "Smallest Number: " + num1 + "\n" + "Biggest Number: " + num2;
            }
        }
    }
}