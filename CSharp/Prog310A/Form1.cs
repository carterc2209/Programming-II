namespace Prog310A
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Random rand = new Random();
            for (int lcv = 0; lcv < rand.Next(5, 11); lcv++);
            double freq = rand.Next(0, 21) + rand.NextDouble();
            string msg = "";
            int starts = (int)Math.Round(freq);
            for (int i = 0; i < starts; i++)
                msg += "*";
            msg += " " + Math.Round(freq, 2);
            listBox1.Items.Add(msg);
        }
    }
}