Console.Write("Enter Number 1: ");
int num1 = int.Parse(Console.ReadLine());
Console.Write("Enter Number 2: ");
int num2 = int.Parse(Console.ReadLine());

int sum = num1 + num2;
int dif = num1 - num2;
int prd = num1 * num2;
double avg = (double)sum / 2.0;
int abs = Math.Abs(dif);
int max, min;

if (num1 > num2)
{
    max = num1;
} else
{
    max = num2;
}

if (num1 <= num2)
    min = num1;
else min = num2;
// else if instead of elif

Console.WriteLine("Sum: " + sum);
Console.WriteLine("Difference: " + dif);
Console.WriteLine("Product: " + prd);
Console.WriteLine("Average: " + avg);
Console.WriteLine("Absolute Value: " + abs);
Console.WriteLine("Minimum: " + min);
Console.WriteLine("Maximum: " + max);
