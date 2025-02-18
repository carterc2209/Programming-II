import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 452)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(185, 98)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(216, 452)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(185, 98)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(419, 452)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(185, 98)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.White
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(12, 112)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(185, 38)
        self._radioButton1.TabIndex = 3
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Section A"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.White
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(12, 205)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(185, 38)
        self._radioButton2.TabIndex = 4
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Section B"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.White
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(12, 301)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(185, 38)
        self._radioButton3.TabIndex = 5
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Section C"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(14, 35)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(288, 47)
        self._label1.TabIndex = 6
        self._label1.Text = "Enter # of tickets:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(301, 35)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(303, 49)
        self._textBox1.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(246, 112)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(343, 45)
        self._label2.TabIndex = 8
        self._label2.Text = "Ticket Cost:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(246, 301)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(343, 45)
        self._label3.TabIndex = 9
        self._label3.Text = "Total:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(246, 203)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(343, 45)
        self._label4.TabIndex = 10
        self._label4.Text = "Taxes:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(616, 562)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg435Tickets"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label2.Text = "Ticket Cost: "
        self._label4.Text = "Tax: "
        self._label3.Text = "Total: " 
        self._textBox1.Text = ""

    def Button1Click(self, sender, e):
        Price = 0
        Ticketnum = int(self._textBox1.Text)
        if self._radioButton1.Checked:
            Price = 20
        elif self._radioButton2.Checked:
            Price = 15
        elif self._radioButton3.Checked:
            Price = 10
        Ticketcost = Ticketnum * Price
        Tax = 0.06 * Ticketcost
        Total = Ticketcost + Tax
        self._label2.Text = "Ticket Cost: " + str(Ticketcost)
        self._label4.Text = "Tax: " + str(Tax)
        self._label3.Text = "Total: " + str(Total)