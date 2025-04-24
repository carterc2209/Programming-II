Console.WriteLine("Enter weight in kilograms");
double weight = double.Parse(Console.ReadLine());
Console.WriteLine("Enter length in centimeters");
double length = double.Parse(Console.ReadLine());
Console.WriteLine("Enter width in centimeters");
double width = double.Parse(Console.ReadLine());
Console.WriteLine("Enter height in centimeters");
double height = double.Parse(Console.ReadLine());
double vol = length * width * height;

if (weight >= 27 && vol >= 100000)
{
    Console.WriteLine("Package is too heavy and too big!!");
} else if (vol >= 100000)
{
    Console.WriteLine("Package is too big!!");
} else if (weight >= 27)
{
    Console.WriteLine("Package is too heavy!!");
}