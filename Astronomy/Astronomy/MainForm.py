import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(431, 60)
        self._label1.TabIndex = 0
        self._label1.Text = "Select a planet"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # comboBox1
        # 
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Mercury",
            "Venus",
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn",
            "Uranus",
            "Neptune",
            "Pluto"]))
        self._comboBox1.Location = System.Drawing.Point(12, 72)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(431, 39)
        self._comboBox1.TabIndex = 1
        self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 72, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 179)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(431, 137)
        self._button1.TabIndex = 2
        self._button1.Text = "Exit"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(455, 328)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Astronomy"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        Application.Exit()

    def ComboBox1SelectedIndexChanged(self, sender, e):
        combo = self._comboBox1.Text
        if combo == "Mercury":
            pass
        elif combo == "Venus":
            pass
        elif combo == "Earth":
            pass
        elif combo == "Mars":
            pass