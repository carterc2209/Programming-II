
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Mars(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 72, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 254)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(445, 119)
        self._button1.TabIndex = 9
        self._button1.Text = "Return"
        self._button1.UseVisualStyleBackColor = False
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 174)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(445, 40)
        self._label4.TabIndex = 8
        self._label4.Text = "Surface Temp: –140°C to 20°C"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 121)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(445, 40)
        self._label3.TabIndex = 7
        self._label3.Text = "Mass: 0.6424 × 10^24 kg"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(12, 67)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(445, 40)
        self._label2.TabIndex = 6
        self._label2.Text = "Avg Dist from Sun: 1.5237 AU"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(12, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(445, 40)
        self._label1.TabIndex = 5
        self._label1.Text = "Type: Terrestrial"
        # 
        # Mars
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(464, 382)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "Mars"
        self.Text = "Mars"
        self.ResumeLayout(False)

