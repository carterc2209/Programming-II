import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from Form1 import *

class MainForm(Form):
    def __init__(self):
        self.opt1 = False
        self.opt2 = False
        self.opt3 = False
        self.price = 0
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._label5 = System.Windows.Forms.Label()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._label7 = System.Windows.Forms.Label()
        self._textBox8 = System.Windows.Forms.TextBox()
        self._label8 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button4 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 357)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(202, 109)
        self._button1.TabIndex = 0
        self._button1.Text = "Select Conference Options"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(393, 357)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(132, 109)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(567, 357)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(202, 109)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(184, 40)
        self._label1.TabIndex = 3
        self._label1.Text = "Name"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(88, 9)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(299, 40)
        self._textBox1.TabIndex = 4
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(124, 55)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(263, 40)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(108, 101)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(279, 40)
        self._textBox3.TabIndex = 8
        self._textBox3.TextChanged += self.TextBox3TextChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 55)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(184, 40)
        self._label2.TabIndex = 5
        self._label2.Text = "Company"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 101)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(184, 40)
        self._label3.TabIndex = 7
        self._label3.Text = "Address"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 147)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(184, 40)
        self._label4.TabIndex = 9
        self._label4.Text = "City"
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(74, 147)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(313, 40)
        self._textBox4.TabIndex = 10
        # 
        # textBox5
        # 
        self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox5.Location = System.Drawing.Point(466, 15)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(302, 40)
        self._textBox5.TabIndex = 12
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(393, 15)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(184, 40)
        self._label5.TabIndex = 11
        self._label5.Text = "Phone"
        # 
        # textBox6
        # 
        self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox6.Location = System.Drawing.Point(466, 58)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(302, 40)
        self._textBox6.TabIndex = 14
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(393, 58)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(184, 40)
        self._label6.TabIndex = 13
        self._label6.Text = "Email"
        # 
        # textBox7
        # 
        self._textBox7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox7.Location = System.Drawing.Point(167, 230)
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(181, 40)
        self._textBox7.TabIndex = 16
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(98, 230)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(116, 40)
        self._label7.TabIndex = 15
        self._label7.Text = "State"
        # 
        # textBox8
        # 
        self._textBox8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox8.Location = System.Drawing.Point(451, 230)
        self._textBox8.Name = "textBox8"
        self._textBox8.Size = System.Drawing.Size(174, 40)
        self._textBox8.TabIndex = 19
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(393, 230)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(184, 40)
        self._label8.TabIndex = 18
        self._label8.Text = "Zip"
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.White
        self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(12, 298)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(756, 40)
        self._label10.TabIndex = 22
        self._label10.Text = "Total Cost: "
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(233, 357)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(132, 109)
        self._button4.TabIndex = 23
        self._button4.Text = "Calc"
        self._button4.UseVisualStyleBackColor = False
        self._button4.Click += self.Button4Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(789, 478)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._textBox8)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._textBox7)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._textBox6)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox5)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg479Conference"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        from Form1 import *
        form1 = Form1(self)
        self._label10.Text = str(self.price)
        form1.Show()
        self.Hide()
        pass
        

    def MainFormLoad(self, sender, e):
        pass

    def TextBox3TextChanged(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button4Click(self, sender, e):
        self._label10.Text = str(self.price)
        pass

    def Button2Click(self, sender, e):
        pass