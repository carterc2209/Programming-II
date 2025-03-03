
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent, opt1, opt2, opt3):
        self.myparent = parent
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Location = System.Drawing.Point(420, 148)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(180, 51)
        self._button1.TabIndex = 0
        self._button1.Text = "Reset"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Location = System.Drawing.Point(613, 148)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(180, 51)
        self._button2.TabIndex = 1
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.White
        self._radioButton1.Location = System.Drawing.Point(12, 27)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(411, 39)
        self._radioButton1.TabIndex = 2
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Conference Regestration (896)"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.White
        self._radioButton2.Location = System.Drawing.Point(12, 82)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(411, 39)
        self._radioButton2.TabIndex = 3
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Opening Dinner + Keynote (30)"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # comboBox1
        # 
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Intro to E-Commerce",
            "The Future of the Web",
            "Advanced Visual Basic",
            "Network Security"]))
        self._comboBox1.Location = System.Drawing.Point(429, 28)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(288, 39)
        self._comboBox1.TabIndex = 4
        self._comboBox1.Text = "Select One"
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(805, 207)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "Form1"
        self.Text = "Form1"
        self.FormClosing += self.Form1FormClosing
        self.FormClosed += self.Form1FormClosed
        self.Load += self.Form1Load
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        self.myparent.Show()
        self.Close()

    def Form1Load(self, sender, e):
        self._radioButton2 = opt2
        self._radioButton1 = opt1
        self._comboBox.Text = opt3

    def Form1FormClosed(self, sender, e):
        pass

    def Form1FormClosing(self, sender, e):
        self.myparent.Show

    def Button1Click(self, sender, e):
        pass