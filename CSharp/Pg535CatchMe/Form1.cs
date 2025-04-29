namespace Pg535CatchMe
{
    public partial class Form1 : Form
    {
        private string[] strCaption = { "Click Here!", "Try Harder!", 
            "Try Again!", "Not Even Close!", "Where Are You?", "I'm Over Here!", "Slow, Aren't You?" };
        private Random rand = new Random();
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Congrats you win", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();
        }

        private void button1_MouseEnter(object sender, EventArgs e)
        {
            int intindex = rand.Next(strCaption.Length);
            button1.Text = strCaption[intindex];
            button1.Left = rand.Next(this.Width - button1.Width);
            button1.Top = rand.Next(this.Height - 30);
        }
    }
}