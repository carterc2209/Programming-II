import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._comboBox2 = System.Windows.Forms.ComboBox()
        self._comboBox3 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # comboBox1
        # 
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Regular",
            "Folding",
            "Roman"]))
        self._comboBox1.Location = System.Drawing.Point(12, 12)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(162, 39)
        self._comboBox1.TabIndex = 0
        self._comboBox1.Text = "Styles"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(19, 336)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(146, 80)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(228, 336)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(146, 80)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(19, 198)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(354, 42)
        self._label1.TabIndex = 3
        self._label1.Text = "Total: "
        # 
        # comboBox2
        # 
        self._comboBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox2.FormattingEnabled = True
        self._comboBox2.Items.AddRange(System.Array[System.Object](
            ["25 Inch",
            "27 Inch",
            "32 Inch",
            "40 Inch"]))
        self._comboBox2.Location = System.Drawing.Point(12, 70)
        self._comboBox2.Name = "comboBox2"
        self._comboBox2.Size = System.Drawing.Size(162, 39)
        self._comboBox2.TabIndex = 4
        self._comboBox2.Text = "Sizes"
        # 
        # comboBox3
        # 
        self._comboBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox3.FormattingEnabled = True
        self._comboBox3.Items.AddRange(System.Array[System.Object](
            ["Natural",
            "Blue",
            "Teal",
            "Red",
            "Green"]))
        self._comboBox3.Location = System.Drawing.Point(12, 129)
        self._comboBox3.Name = "comboBox3"
        self._comboBox3.Size = System.Drawing.Size(162, 39)
        self._comboBox3.TabIndex = 5
        self._comboBox3.Text = "Colors"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(386, 438)
        self.Controls.Add(self._comboBox3)
        self.Controls.Add(self._comboBox2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._comboBox1)
        self.Name = "MainForm"
        self.Text = "Pg485Shade"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        combo1 = self._comboBox1.Text
        combo2 = self._comboBox2.Text
        combo3 = self._comboBox3.Text
        cost1 = 0
        cost2 = 0
        cost3 = 0
        if combo1 == "Regular":
            cost1 = 0
        elif combo1 == "Folding":
            cost1 = 10
        elif combo1 == "Roman":
            cost1 = 15
        
        if combo2 == "25 Inch":
            cost2 = 0
        elif combo2 == "27 Inch":
            cost2 = 2
        elif combo2 == "32 Inch":
            cost2 = 4
        elif combo2 == "40 Inch":
            cost2 = 6
        
        if combo3 == "Natural":
            cost3 = 5
        elif combo3 == "Blue":
            cost3 = 0
        elif combo3 == "Teal":
            cost3 = 0
        elif combo3 == "Red":
            cost3 = 0
        elif combo3 == "Green":
            cost3 = 0
        
        self._label1.Text = "Total: " + str(50+cost1+cost2+cost3)