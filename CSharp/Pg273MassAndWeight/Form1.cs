namespace Pg273MassAndWeight
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            decimal mass = decimal.Parse(textBox1.Text);
            decimal weight = mass * (decimal)9.8;
            string word = "";
            if (weight >= 1000)
            {
                word = "This object is too heavy";
            } else if (weight <= 20)
            {
                word = "This object is too small";
            }
            label2.Text = weight.ToString() + "\n" + word;

        }
    }
}