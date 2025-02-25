import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton5 = System.Windows.Forms.RadioButton()
        self._radioButton6 = System.Windows.Forms.RadioButton()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._radioButton7 = System.Windows.Forms.RadioButton()
        self._radioButton8 = System.Windows.Forms.RadioButton()
        self._radioButton9 = System.Windows.Forms.RadioButton()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._radioButton10 = System.Windows.Forms.RadioButton()
        self._radioButton11 = System.Windows.Forms.RadioButton()
        self._radioButton12 = System.Windows.Forms.RadioButton()
        self._radioButton13 = System.Windows.Forms.RadioButton()
        self._radioButton14 = System.Windows.Forms.RadioButton()
        self._radioButton15 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 424)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(233, 121)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(308, 489)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(233, 56)
        self._button2.TabIndex = 1
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(308, 424)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(233, 59)
        self._button3.TabIndex = 2
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.White
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(200, 137)
        self._groupBox1.TabIndex = 4
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Decks:"
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(6, 23)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(188, 31)
        self._radioButton1.TabIndex = 5
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "The Master Trasher"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(6, 60)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(188, 31)
        self._radioButton2.TabIndex = 6
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "The Dictator of Grind"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(6, 97)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(188, 31)
        self._radioButton3.TabIndex = 7
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "The Street KIng"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.White
        self._groupBox2.Controls.Add(self._radioButton4)
        self._groupBox2.Controls.Add(self._radioButton5)
        self._groupBox2.Controls.Add(self._radioButton6)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(341, 12)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(200, 137)
        self._groupBox2.TabIndex = 8
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Truck Assembly"
        # 
        # radioButton4
        # 
        self._radioButton4.Location = System.Drawing.Point(6, 97)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(188, 31)
        self._radioButton4.TabIndex = 7
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "8.5 Axle"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # radioButton5
        # 
        self._radioButton5.Location = System.Drawing.Point(6, 60)
        self._radioButton5.Name = "radioButton5"
        self._radioButton5.Size = System.Drawing.Size(188, 31)
        self._radioButton5.TabIndex = 6
        self._radioButton5.TabStop = True
        self._radioButton5.Text = "8 Axle"
        self._radioButton5.UseVisualStyleBackColor = True
        # 
        # radioButton6
        # 
        self._radioButton6.Location = System.Drawing.Point(6, 23)
        self._radioButton6.Name = "radioButton6"
        self._radioButton6.Size = System.Drawing.Size(188, 31)
        self._radioButton6.TabIndex = 5
        self._radioButton6.TabStop = True
        self._radioButton6.Text = "7.75 Axle"
        self._radioButton6.UseVisualStyleBackColor = True
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.White
        self._groupBox3.Controls.Add(self._radioButton15)
        self._groupBox3.Controls.Add(self._radioButton13)
        self._groupBox3.Controls.Add(self._radioButton7)
        self._groupBox3.Controls.Add(self._radioButton8)
        self._groupBox3.Controls.Add(self._radioButton9)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(341, 173)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(200, 206)
        self._groupBox3.TabIndex = 10
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "MISC:"
        # 
        # radioButton7
        # 
        self._radioButton7.Location = System.Drawing.Point(6, 97)
        self._radioButton7.Name = "radioButton7"
        self._radioButton7.Size = System.Drawing.Size(188, 31)
        self._radioButton7.TabIndex = 7
        self._radioButton7.TabStop = True
        self._radioButton7.Text = "Riser Pads"
        self._radioButton7.UseVisualStyleBackColor = True
        # 
        # radioButton8
        # 
        self._radioButton8.Location = System.Drawing.Point(6, 60)
        self._radioButton8.Name = "radioButton8"
        self._radioButton8.Size = System.Drawing.Size(188, 31)
        self._radioButton8.TabIndex = 6
        self._radioButton8.TabStop = True
        self._radioButton8.Text = "Bearings"
        self._radioButton8.UseVisualStyleBackColor = True
        # 
        # radioButton9
        # 
        self._radioButton9.Location = System.Drawing.Point(6, 23)
        self._radioButton9.Name = "radioButton9"
        self._radioButton9.Size = System.Drawing.Size(188, 31)
        self._radioButton9.TabIndex = 5
        self._radioButton9.TabStop = True
        self._radioButton9.Text = "Grip Tape"
        self._radioButton9.UseVisualStyleBackColor = True
        # 
        # groupBox4
        # 
        self._groupBox4.BackColor = System.Drawing.Color.White
        self._groupBox4.Controls.Add(self._radioButton14)
        self._groupBox4.Controls.Add(self._radioButton10)
        self._groupBox4.Controls.Add(self._radioButton11)
        self._groupBox4.Controls.Add(self._radioButton12)
        self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox4.Location = System.Drawing.Point(12, 173)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.Size = System.Drawing.Size(200, 165)
        self._groupBox4.TabIndex = 9
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Wheel Sets:"
        # 
        # radioButton10
        # 
        self._radioButton10.Location = System.Drawing.Point(6, 97)
        self._radioButton10.Name = "radioButton10"
        self._radioButton10.Size = System.Drawing.Size(188, 31)
        self._radioButton10.TabIndex = 7
        self._radioButton10.TabStop = True
        self._radioButton10.Text = "58 mm"
        self._radioButton10.UseVisualStyleBackColor = True
        # 
        # radioButton11
        # 
        self._radioButton11.Location = System.Drawing.Point(6, 60)
        self._radioButton11.Name = "radioButton11"
        self._radioButton11.Size = System.Drawing.Size(188, 31)
        self._radioButton11.TabIndex = 6
        self._radioButton11.TabStop = True
        self._radioButton11.Text = "55 mm"
        self._radioButton11.UseVisualStyleBackColor = True
        # 
        # radioButton12
        # 
        self._radioButton12.Location = System.Drawing.Point(6, 23)
        self._radioButton12.Name = "radioButton12"
        self._radioButton12.Size = System.Drawing.Size(188, 31)
        self._radioButton12.TabIndex = 5
        self._radioButton12.TabStop = True
        self._radioButton12.Text = "51 mm"
        self._radioButton12.UseVisualStyleBackColor = True
        # 
        # radioButton13
        # 
        self._radioButton13.Location = System.Drawing.Point(6, 134)
        self._radioButton13.Name = "radioButton13"
        self._radioButton13.Size = System.Drawing.Size(188, 31)
        self._radioButton13.TabIndex = 8
        self._radioButton13.TabStop = True
        self._radioButton13.Text = "Nuts & Bolts Kit"
        self._radioButton13.UseVisualStyleBackColor = True
        # 
        # radioButton14
        # 
        self._radioButton14.Location = System.Drawing.Point(6, 128)
        self._radioButton14.Name = "radioButton14"
        self._radioButton14.Size = System.Drawing.Size(188, 31)
        self._radioButton14.TabIndex = 8
        self._radioButton14.TabStop = True
        self._radioButton14.Text = "61 mm"
        self._radioButton14.UseVisualStyleBackColor = True
        # 
        # radioButton15
        # 
        self._radioButton15.Location = System.Drawing.Point(6, 169)
        self._radioButton15.Name = "radioButton15"
        self._radioButton15.Size = System.Drawing.Size(188, 31)
        self._radioButton15.TabIndex = 9
        self._radioButton15.TabStop = True
        self._radioButton15.Text = "Assembly"
        self._radioButton15.UseVisualStyleBackColor = True
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 352)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(273, 69)
        self._label1.TabIndex = 11
        self._label1.Text = "Cost:"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(555, 557)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Pg485Skate"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self._groupBox4.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        Application.Exit()
        

    def Button3Click(self, sender, e):
        self._radioButton1.Checked = False
        self._radioButton2.Checked = False
        self._radioButton3.Checked = False
        self._radioButton4.Checked = False
        self._radioButton5.Checked = False
        self._radioButton6.Checked = False
        self._radioButton7.Checked = False
        self._radioButton8.Checked = False
        self._radioButton9.Checked = False
        self._radioButton10.Checked = False
        self._radioButton11.Checked = False
        self._radioButton12.Checked = False
        self._radioButton13.Checked = False
        self._radioButton14.Checked = False
        self._radioButton15.Checked = False