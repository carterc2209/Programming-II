using static System.Console;

Write("Enter the radius: ");
double rad = double.Parse(ReadLine());

double area = 3.14 * Math.Pow(rad, 2);
double cir = 6.28 * rad;
WriteLine("Area: " + Math.Round(area, 3));
WriteLine("Circumference: " + Math.Round(cir, 3));
