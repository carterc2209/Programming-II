import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Location = System.Drawing.Point(316, 297)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(47, 56)
        self._button3.TabIndex = 13
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(389, 250)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(257, 157)
        self._button2.TabIndex = 12
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 36, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 250)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(257, 157)
        self._button1.TabIndex = 11
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(208, 17)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(439, 40)
        self._textBox1.TabIndex = 10
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(220, 172)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(427, 46)
        self._label3.TabIndex = 9
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 172)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(202, 46)
        self._label2.TabIndex = 8
        self._label2.Text = "Anagrams?"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(21, 17)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(258, 40)
        self._label1.TabIndex = 7
        self._label1.Text = "Enter Word1:"
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(208, 78)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(439, 40)
        self._textBox2.TabIndex = 15
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(21, 78)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(258, 40)
        self._label4.TabIndex = 14
        self._label4.Text = "Enter Word2:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(659, 419)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StrIntII"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label3.Text = ""

    def Button1Click(self, sender, e):
        self._label3.Text = ""
        word1 = self._textBox1.Text.lower()
        word2 = self._textBox2.Text.lower()
        
        if len(word1) != len(word2):
            self._label3.Text = "False"
        else:
            for lcv in range(len(word1)):
                c = word1[lcv]
                index = word2.find(c)
                if index == -1:
                    self._label3.Text = "False"
                else:
                    word2 = word2[0:index] + word2[index+1:]
        self._label3.Text = str(len(word2) == 0)