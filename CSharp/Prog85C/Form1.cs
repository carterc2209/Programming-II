namespace Prog85C
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            label3.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int month = 0;
            string opt1 = textBox2.Text;
            if (opt1 == "January" || opt1 == "1")
            {
                month = 1;
            }
            else if (opt1 == "February" || opt1 == "2")
            {
                month = 2;
            }
            else if (opt1 == "March" || opt1 == "3")
            {
                month = 3;
            }
            else if (opt1 == "April" || opt1 == "4")
            {
                month = 4;
            }
            else if (opt1 == "May" || opt1 == "5")
            {
                month = 5;
            }
            else if (opt1 == "June" || opt1 == "6")
            {
                month = 6;
            }
            else if (opt1 == "July" || opt1 == "7")
            {
                month = 7;
            }
            else if (opt1 == "August" || opt1 == "8")
            {
                month = 8;
            }
            else if (opt1 == "September" || opt1 == "9")
            {
                month = 9;
            }
            else if (opt1 == "October" || opt1 == "10")
            {
                month = 10;
            }
            else if (opt1 == "November" || opt1 == "11")
            {
                month = 11;
            }
            else if (opt1 == "December" || opt1 == "12")
            {
                month = 12;
            }
            int day = int.Parse(textBox1.Text);
            int num = (((((month * 5) + 6) * 4) + 9) * 5) + day;
            int birthdate = (num - 165) / 100;
            label3.Text = num.ToString() + "\n" + birthdate.ToString() + "/" + day;
 
        }
    }
}