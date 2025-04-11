using static System.Console;

Write("Enter Base: ");
double base1 = double.Parse(ReadLine());
Write("Enter Height: ");
double height = double.Parse(ReadLine());
double hyp = Math.Sqrt((height * height) + (base1 * base1));
double area = (height * base1) / 2;
double perim = height + base1 + hyp;
WriteLine("Hypotenuse: " + Math.Round(hyp, 2));
WriteLine("Area: " + area);
WriteLine("Perimeter: " + Math.Round(perim, 2));
