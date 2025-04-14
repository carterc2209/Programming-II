namespace Prog54B_CSHARP
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string num1 = label1.Text;
            string num2 = label2.Text;  
            string num3 = label3.Text; 
            string num4 = label4.Text;
            int sum = int.Parse(num1 + num2 + num3 + num4);
            int avg = sum / 4;
            label5.Text = "Sum: " + sum;
            label6.Text = "Average: " + avg;
        }
    }
}