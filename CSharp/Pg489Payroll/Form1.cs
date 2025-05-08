using Microsoft.VisualBasic;

namespace Pg489Payroll
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
        const int intMAX_EMPLOYEES = 5;
        const decimal decHOURLY_PAY_RATE = 6.0M;
        private void button1_Click(object sender, EventArgs e)
        {
            // Clac & display gross pay earned by employees
            int[] intHours = new int[intMAX_EMPLOYEES]; // array
            // <type>[] varName = new <type>[capacity]
            int Count = 0;
            int EmpHours = 0;
            decimal EmpPay = 0.0M;

            for (Count = 0; Count < intMAX_EMPLOYEES; Count++)
            {
                while (int.TryParse(Interaction.InputBox("Enter Number of Hours Worked by Employee #"
                    + (Count + 1).ToString(), "Need hours worked"), out EmpHours) == false) ;
                {
                    MessageBox.Show("Please Enter an Integer for Hours Worked");
                }
                intHours[Count] = EmpHours;
            }
            listBox1.Items.Clear();
            for (Count = 0; Count < intMAX_EMPLOYEES; Count++)
            {
                EmpPay = intHours[Count] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Employee " + (Count + 1).ToString() +
                " Earned " + EmpPay.ToString("$.00"));
            }
        }
    }
}