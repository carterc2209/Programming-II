
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Mercury(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(12, 18)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(445, 40)
        self._label1.TabIndex = 0
        self._label1.Text = "Type: Terrestrial"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(12, 73)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(445, 40)
        self._label2.TabIndex = 1
        self._label2.Text = "Avg Dist from Sun: 0.387 AU"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(12, 127)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(445, 40)
        self._label3.TabIndex = 2
        self._label3.Text = "Mass: 3.31 × 10^23 kg"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(12, 180)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(445, 40)
        self._label4.TabIndex = 3
        self._label4.Text = "Surface Temp: –173°C to 430°C"
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 72, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 260)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(445, 119)
        self._button1.TabIndex = 4
        self._button1.Text = "Return"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # Mercury
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(469, 388)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "Mercury"
        self.Text = "Mercury"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Close()