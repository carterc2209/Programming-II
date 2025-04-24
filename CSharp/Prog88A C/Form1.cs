namespace Prog88A_C
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            label3.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int ans = num1 + num2;
            label3.Text = ans.ToString();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int ans = num1 - num2;
            label3.Text = ans.ToString();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int ans = num1 * num2;
            label3.Text = ans.ToString();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            double ans = (num1 + num2) / 2;
            label3.Text = ans.ToString();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int ans = Math.Abs(num1 - num2);
            label3.Text = ans.ToString();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int small = 0;
            if (num1 > num2)
            {
                small = num2;
            }
            else
            {
                small = num1;
            }
            int ans = small;
            label3.Text = ans.ToString();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int big = 0;
            if (num1 > num2)
            {
                big = num1;
            }
            else
            {
                big = num2;
            }
            int ans = big;
            label3.Text = ans.ToString();
        }
    }
}