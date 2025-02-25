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
        self._comboBox2 = System.Windows.Forms.ComboBox()
        self._comboBox3 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # comboBox1
        # 
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Red",
            "Green",
            "Blue",
            "Black"]))
        self._comboBox1.Location = System.Drawing.Point(280, 12)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(115, 33)
        self._comboBox1.TabIndex = 0
        self._comboBox1.Text = "Color"
        self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Transparent
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(117, 19)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(10, 10)
        self._button1.TabIndex = 1
        self._button1.Text = "Change"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Transparent
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(117, 19)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(10, 10)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # comboBox2
        # 
        self._comboBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox2.FormattingEnabled = True
        self._comboBox2.Items.AddRange(System.Array[System.Object](
            ["Exit"]))
        self._comboBox2.Location = System.Drawing.Point(12, 12)
        self._comboBox2.Name = "comboBox2"
        self._comboBox2.Size = System.Drawing.Size(115, 33)
        self._comboBox2.TabIndex = 3
        self._comboBox2.Text = "File"
        self._comboBox2.SelectedIndexChanged += self.ComboBox2SelectedIndexChanged
        # 
        # comboBox3
        # 
        self._comboBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox3.FormattingEnabled = True
        self._comboBox3.Items.AddRange(System.Array[System.Object](
            [""]))
        self._comboBox3.Location = System.Drawing.Point(143, 12)
        self._comboBox3.Name = "comboBox3"
        self._comboBox3.Size = System.Drawing.Size(115, 33)
        self._comboBox3.TabIndex = 4
        self._comboBox3.Text = "Help"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(64, 64, 64)
        self.ClientSize = System.Drawing.Size(425, 177)
        self.Controls.Add(self._comboBox3)
        self.Controls.Add(self._comboBox2)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._comboBox1)
        self.Name = "MainForm"
        self.Text = "Pg447Menu"
        self.ResumeLayout(False)


    def ComboBox1SelectedIndexChanged(self, sender, e):
        combo = self._comboBox1.Text
        if combo == "Red":
            self.BackColor = Color.Red
        elif combo == "Blue":
            self.BackColor = Color.Blue
        elif combo == "Green":
            self.BackColor = Color.Green
        elif combo == "Black":
            self.BackColor = Color.Black

    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        Application.Exit()

    def ComboBox2SelectedIndexChanged(self, sender, e):
        combo2 = self._comboBox2.Text
        if combo2 == "Exit":
            Application.Exit()
        