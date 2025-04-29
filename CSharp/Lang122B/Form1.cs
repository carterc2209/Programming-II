namespace Lang122B
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("Hours\t\tPay");
            int lcv = 1;
            while (lcv <= 40)
            {
                int pay = lcv * 4;
                int square = (int)Math.Pow(lcv, 2);
                double sqrt = Math.Sqrt(lcv);
                listBox1.Items.Add(lcv + "\t\t" + pay);
                lcv++;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}