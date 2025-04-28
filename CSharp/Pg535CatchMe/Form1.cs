namespace Pg535CatchMe
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Congrats you win", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
        }

        private void button1_MouseEnter(object sender, EventArgs e)
        {
            int intindex = Random.Next(strCaption.Length);
        }
    }
}