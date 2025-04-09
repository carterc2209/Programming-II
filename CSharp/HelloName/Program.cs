// See https://aka.ms/new-console-template for more information
//Console.WriteLine("Hello, World!");
Console.Write("Enter your name: ");
// int, bool, string, char, double instead of float
string name = Console.ReadLine();
Console.WriteLine("Hello," + name);

Console.WriteLine("Enter your age: ");
// int age = convert.ToInt32(Console.ReadLine());
int age = int.Parse(Console.ReadLine());
// age = int(input)
Console.WriteLine("You are: " + age + "years old");