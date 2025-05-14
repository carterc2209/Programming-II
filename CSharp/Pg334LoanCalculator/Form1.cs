namespace Pg334LoanCalculator
{
    using Microsoft.VisualBasic;
    public partial class Form1 : Form
    {
        const int intMIN_MONTHS = 6;
        const int intMAX_MONTHS = 48;
        const double sngMONTHS_YEAR = 12.0;
        const double dblNEW_RATE = 0.089;
        const double dblUSED_RATE = 0.095;
        double dblANNUAL_RATE = dblNEW_RATE;
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int intCount = 0;
            int intMonths = 0;
            double dblLoans = 0.0;
            double dblPayment = 0.0;
            double dblInterest = 0.0;
            double dblPrincipal = 0.0;

            try
            {
                intMonths = int.Parse(textBox3.Text);
                dblLoans = double.Parse(textBox1.Text) - double.Parse(textBox2.Text);
            } catch (Exception ex){
                MessageBox.Show("Please enter a numeric value");
                return;
            }

            dblPayment = Financial.Pmt(dblANNUAL_RATE / sngMONTHS_YEAR, intMonths, -dblLoans);

            listBox1.Items.Clear();

            for (intCount = 1; intCount <= intMAX_MONTHS; intCount++)
            {
                string Out = string.Empty;

                dblInterest = Financial.IPmt(dblANNUAL_RATE / sngMONTHS_YEAR,
                    intCount, intMonths, -dblLoans);

                dblPrincipal = Financial.PPmt(dblANNUAL_RATE / sngMONTHS_YEAR,
                    intCount, intMonths, -dblLoans);

                Out += "Month: " + intCount;
                Out += " Payment: " + dblPayment.ToString("$.00");
                Out += " Interest: " + dblInterest.ToString("$.00");
                Out += " Principal: " + dblPrincipal.ToString("$.00");
            }
        }
    }
}