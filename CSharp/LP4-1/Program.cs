Console.WriteLine("Enter Copies: ");
int copies = int.Parse(Console.ReadLine());
double ppc = 0;

// && = and         || = or           ! = not


if (copies > 0 && copies <= 99)
{
    ppc = 0.30;
}else if (copies > 100 && copies <= 499)
{
    ppc = 0.28;
}
else if (copies >= 500 && copies <= 749)
{
    ppc = 0.27;
}
else if (copies >= 750 && copies <= 999)
{
    ppc = 0.26;
}
else if (copies > 1000)
{
    ppc = 0.25;
}
double tot = ppc * copies;
Console.WriteLine("Total price for the copies: " + tot);
Console.ReadLine();