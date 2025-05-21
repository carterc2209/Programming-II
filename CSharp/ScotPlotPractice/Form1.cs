namespace ScotPlotPractice
{
    using System;
    using System.Windows.Forms;

    using OxyPlot;
    using OxyPlot.Series;
    using OxyPlot.WindowsForms;
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var plotModel = new PlotModel
            {
                Title = "Spending and Davings",
                Background = OxyColors.Olive
            };

            var barSeries = new BarSeries();
            barSeries.IsStacked = false;
            plotModel.Series.Add(barSeries);

            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);
            int num3 = int.Parse(textBox3.Text);


            barSeries.Items.Add(new BarItem(num1));
            barSeries.Items.Add(new BarItem(num2));
            barSeries.Items.Add(new BarItem(num3));

            plotView1.Model = plotModel;
        }
    }
}