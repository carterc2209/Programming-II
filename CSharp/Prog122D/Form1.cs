namespace Prog122D
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double x = -12;
            for (; ;x++)
            {
                double y = Math.Pow(x, 6) - (3 * Math.Pow(x, 5)) - (93 * Math.Pow(x, 4))
                    + (87 * Math.Pow(x, 3)) + (1596 * Math.Pow(x, 2)) - (1380 * x) - 2800;
                listBox1.Items.Add(y);
            }
        }
    }
}