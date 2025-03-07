
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.opt1 = False
        self.opt2 = False
        self.opt3 = False
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._label1 = System.Windows.Forms.Label()
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
        # label1
        # 
        self._label1.Location = System.Drawing.Point(43, 158)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(161, 40)
        self._label1.TabIndex = 5
        self._label1.Text = "label1"
        # 
        # Form1
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(805, 207)
        self.Controls.Add(self._label1)
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
        opt1 = self._radioButton1
        opt2 = self._radioButton2
        opt3 = self._comboBox1.Text
        if opt1:
            self.myparent.price += 896
        elif opt2:
            self.myparent.price += 30
        if opt3 == "Intro to E-Commerce":
            self.myparent.price += 295
        elif opt3 == "The Future of the Web":
            self.myparent.price += 295
        elif opt3 == "Advanced Visual Basic":
            self.myparent.price += 395
        elif opt3 == "Network Security":
            self.myparent.price += 395
        

    def Form1Load(self, sender, e):
        pass

    def Form1FormClosed(self, sender, e):
        pass

    def Form1FormClosing(self, sender, e):
        self.myparent.Show

    def Button1Click(self, sender, e):
        self.opt1 = False
        self.opt2 = False
        self.opt3 = False
        self._label1.Text = str(self.myparent.price)