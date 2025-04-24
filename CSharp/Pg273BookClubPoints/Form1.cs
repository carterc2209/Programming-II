namespace Pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num = int.Parse(textBox1.Text);
            if (num == 0)
            {
                label2.Text = "You earned 0 points this month!";
            }else if (num == 1)
            {
                label2.Text = "You earned 5 points this month!";
            }else if (num == 2)
            {
                label2.Text = "You earned 15 points this month!";
            }else if (num == 3)
            {
                label2.Text = "You earned 30 points this month!";
            }else if (num >= 4)
            {
                label2.Text = "You earned 60 points this month!";
            }
        }
    }
}