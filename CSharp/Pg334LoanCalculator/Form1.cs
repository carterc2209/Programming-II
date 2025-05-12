namespace Pg334LoanCalculator
{
    public partial class Form1 : Form
    {
        const int min_months = 6;
        const int max_months = 48;
        const float year = 12.0f;
        const double New = 0.089;
        const double old = 0.095;
        double annual = New;
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int count = 0;
            int months = 0;
            double loans = 0.0;
            double payment = 0.0;
            double interest = 0.0;
            double principal = 0.0;

            try
            {
                months = int.Parse(textBox3.Text);
                loans = double.Parse(textBox1.Text) - double.Parse(textBox2.Text);
            } catch (Exception ex)
            {
                MessageBox.Show("Please enter a numeric value");
                return;
            }

            payment = Financial.Pmt(annual / year, months, -loans);

            listBox1.Items.Clear();
        }
    }
}