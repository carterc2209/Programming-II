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
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(420, 52)
        self._label1.TabIndex = 0
        self._label1.Text = "Select a Planet"
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
        self._comboBox1.Location = System.Drawing.Point(12, 79)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(420, 39)
        self._comboBox1.TabIndex = 1
        self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(14, 131)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(417, 235)
        self._label2.TabIndex = 2
        self._label2.Text = """Type

Avg Distance From the Sun

Mass

Surface Temp
"""
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(14, 382)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(195, 128)
        self._button1.TabIndex = 3
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(232, 382)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(200, 128)
        self._button2.TabIndex = 4
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(444, 522)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg486Astronomy"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        Application.Exit()

    def ComboBox1SelectedIndexChanged(self, sender, e):
        combo = self._comboBox1.Text
        if combo == "Mercury":
            self._label2.Text = "Type: Terrestrial" + "\n\n" + "Avg Distance From the Sun: 0.387 AU" + "\n\n" + "Mass: 3.31 x 10^23 kg" + "\n\n" + "Surface Tempurature: -173°C to 420°C"
        elif combo == "Venus":
            self._label2.Text = "Type: Terrestrial" + "\n\n" + "Avg Distance From the Sun: 0.7233 AU" + "\n\n" + "Mass: 4.87 x 10^24 kg" + "\n\n" + "Surface Tempurature: 472°C"
        elif combo == "Earth":
            self._label2.Text = "Type: Terrestrial" + "\n\n" + "Avg Distance From the Sun: 1 AU" + "\n\n" + "Mass: 5.967 x 10^24 kg" + "\n\n" + "Surface Tempurature: –50°C to 50°C"
        elif combo == "Mars":
            self._label2.Text = "Type: Terrestrial" + "\n\n" + "Avg Distance From the Sun: 1.5237 AU" + "\n\n" + "Mass: 0.6424 x 10^24 kg" + "\n\n" + "Surface Tempurature: –140°C to 20°C"
        elif combo == "Jupiter":
            self._label2.Text = "Type: Jovian" + "\n\n" + "Avg Distance From the Sun: 5.2028 AU" + "\n\n" + "Mass: 1.899 x 10^27 kg" + "\n\n" + "Surface Tempurature: –110°C"
        elif combo == "Saturn":
            self._label2.Text = "Type: Jovian" + "\n\n" + "Avg Distance From the Sun: 9.5388 AU" + "\n\n" + "Mass: 5.69 x 10^26 kg" + "\n\n" + "Surface Tempurature: –180°C"
        elif combo == "Uranus":
            self._label2.Text = "Type: Jovian" + "\n\n" + "Avg Distance From the Sun: 19.18 AU" + "\n\n" + "Mass: 8.69 x 10^25 kg" + "\n\n" + "Surface Tempurature: –220°C"
        elif combo == "Neptune":
            self._label2.Text = "Type: Jovian" + "\n\n" + "Avg Distance From the Sun: 30.0611 AU" + "\n\n" + "Mass: 1.03 x 10^26 kg" + "\n\n" + "Surface Tempurature: –216°C"
        elif combo == "Pluto":
            self._label2.Text = "Type: Low Density" + "\n\n" + "Avg Distance From the Sun: 0.387 AU" + "\n\n" + "Mass: 1.2 x 10^22 kg" + "\n\n" + "Surface Tempurature: –230°C"
            

    def Button1Click(self, sender, e):
        self._comboBox1.Text = ""
        self._label2.Text = "Type: " + "\n\n" + "Avg Distance From the Sun: " + "\n\n" + "Mass: " + "\n\n" + "Surface Tempurature: "
        