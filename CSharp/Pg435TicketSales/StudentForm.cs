using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSales
{
    public partial class StudentForm : Form
    {
        private Form myParent;
        public StudentForm(Form myParent)
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int tickets =  int.Parse(textBox1.Text);
            decimal cost = tickets * 6;
            decimal tax = (decimal)cost * 0.06M;
            decimal total = tax + cost;
            label2.Text = "Ticket cost: " + cost.ToString();
            label3.Text = "Tax cost: " + tax.ToString();
            label4.Text = "Total: " + total.ToString();

        }
    }
}
