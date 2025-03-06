
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MealForm(Form):
    def __init__(self, parent):
        self.myparent = parent
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # comboBox1
        # 
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["7 Meals per Week ($560 per Semester)",
            "14 Meals per Week ($1,095 per Semester)",
            "Unlimited Meals ($1,500 per Semester)"]))
        self._comboBox1.Location = System.Drawing.Point(12, 69)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(372, 32)
        self._comboBox1.TabIndex = 0
        self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(372, 57)
        self._label1.TabIndex = 1
        self._label1.Text = "Select your meal plan"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 345)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(372, 144)
        self._button1.TabIndex = 2
        self._button1.Text = "Dorm Form"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 152)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(372, 50)
        self._label2.TabIndex = 3
        self._label2.Text = "Meal Cost Per Semester:"
        # 
        # MealForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(396, 501)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._comboBox1)
        self.Name = "MealForm"
        self.Text = "MealForm"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Hide()

    def ComboBox1SelectedIndexChanged(self, sender, e):
        from MainForm import *
        combo = self._comboBox1.Text
        if combo == "7 Meals per Week ($560 per Semester)":
            Mealcost = 560
        elif combo == "14 Meals per Week ($1,095 per Semester)":
            Mealcost = 1095
        elif combo == "Unlimited Meals ($1,500 per Semester)":
            Mealcost = 1500
        self._label2.Text = str(Mealcost)