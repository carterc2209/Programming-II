namespace Pg435TicketSales
{
    public partial class Form1 : Form
    {
        private Form myParent;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form frm = new StudentForm(this);
            frm.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form frm = new GeneralForm(this);
            frm.Show();
            this.Hide();

        }
    }
}