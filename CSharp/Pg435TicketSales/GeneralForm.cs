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
    public partial class GeneralForm : Form
    {
        private Form myParent;
        public GeneralForm(Form myParent)
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        private void GeneralForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int ppt = 0;
            if (radioButton1.Checked)
            {
                ppt = 20;
            }
            else if (radioButton2.Checked)
            {
                ppt = 15;
            }
            else if (radioButton3.Checked)
            {
                ppt = 10;
            }
            else
            {
                MessageBox.Show("Invalid Selection");
            }
            int tickets = int.Parse(textBox1.Text);
            decimal cost = tickets * ppt;
            decimal tax = (decimal)cost * 0.06M;
            decimal total = tax + cost;
            label2.Text = ("$" + cost.ToString() + ".00");
            label3.Text = ("$" + tax.ToString());
            label4.Text = ("$" + total.ToString());

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}
