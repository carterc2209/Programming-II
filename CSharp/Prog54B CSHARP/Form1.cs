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
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);  
            int num3 = int.Parse(textBox3.Text); 
            int num4 = int.Parse(textBox4.Text);
            int sum = num1 + num2 + num3 + num4;
            double avg = (double)sum / 4;
            label5.Text = "Sum: " + sum.ToString();
            label6.Text = "Average: " + avg.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
            label5.Text = "Sum:";
            label6.Text = "Average: ";
        }
    }
}