import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.Dorm = 0
        self.Mealcost = 0
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._label2 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 382)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(218, 179)
        self._button1.TabIndex = 0
        self._button1.Text = "Go To Meal Plans"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(280, 382)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(218, 179)
        self._button2.TabIndex = 1
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(19, 35)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(464, 58)
        self._label1.TabIndex = 2
        self._label1.Text = "Select your dorm plan"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # comboBox1
        # 
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Allen Hall ($1,500 per semester)",
            "Pike Hall ($1,600 per semester)",
            "Farthing Hall ($1,200 per semester)",
            "University Suites ($1,800 per semester)"]))
        self._comboBox1.Location = System.Drawing.Point(19, 96)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(464, 37)
        self._comboBox1.TabIndex = 3
        self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(19, 198)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(470, 48)
        self._label2.TabIndex = 4
        self._label2.Text = "Dorm Cost per Semester:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(510, 573)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg484DormAndMealPlans"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        from MealForm import *
        meals = MealForm(self)
        meals.Show()
        self.Hide()

    def ComboBox1SelectedIndexChanged(self, sender, e):
        combo = self._comboBox1.Text
        if combo == "Allen Hall ($1,500 per semester)":
            self.Dorm = 1500
        elif combo == "Pike Hall ($1,600 per semester)":
            self.Dorm = 1600
        elif combo == "Farthing Hall ($1,200 per semester)":
            self.Dorm = 1200
        elif combo == "University Suites ($1,800 per semester)":
            self.Dorm = 1800
        self._label2.Text = "Dorm Cost per Semester: " + str(self.Dorm + self.Mealcost)
        