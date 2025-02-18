import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.White
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(33, 31)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(195, 63)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Morning  $0.07"
        self._radioButton1.UseVisualStyleBackColor = False
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.White
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(33, 137)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(195, 63)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Evening  $0.12"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.White
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(33, 238)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(195, 63)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Off-Peak  $0.05"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 498)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(202, 92)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(220, 498)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(202, 92)
        self._button2.TabIndex = 4
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(428, 498)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(127, 92)
        self._button3.TabIndex = 5
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(244, 31)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(301, 426)
        self._label1.TabIndex = 6
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(33, 364)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(194, 44)
        self._textBox1.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(33, 318)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(193, 43)
        self._label2.TabIndex = 8
        self._label2.Text = "Enter Amount of Minutes:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(567, 624)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Name = "MainForm"
        self.Text = "Pg272LongDistance"
        self.ResumeLayout(False)
        self.PerformLayout()


    def RadioButton1CheckedChanged(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._radioButton1.Checked = False
        self._radioButton2.Checked = False
        self._radioButton3.Checked = False
        self._label1.Text = ""
        self._textBox1.Text = ""
        
    def Button1Click(self, sender, e):
        minutes = int(self._textBox1.Text)
        time = 0
        if self._radioButton1.Checked == True:
            time = 0.07
        elif self._radioButton2.Checked == True:
            time = 0.07
        elif self._radioButton3.Checked == True:
            time = 0.05
        self._label1.Text = str(minutes * time)
            