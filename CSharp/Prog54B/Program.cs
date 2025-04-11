using static System.Console;
Console.WriteLine("Enter Number 1: ");
int num1 = int.Parse(ReadLine());
Console.WriteLine("Enter Number 2: ");
int num2 = int.Parse(ReadLine());
Console.WriteLine("Enter Number 3: ");
int num3 = int.Parse(ReadLine());
Console.WriteLine("Enter Number 4: ");
int num4 = int.Parse(ReadLine());

int sum = num1 + num2 + num3 + num4;
double avg = (double)sum / 4;
WriteLine("Sum: " + sum);
WriteLine("Average: " + Math.Round(avg, 2));
ReadKey();