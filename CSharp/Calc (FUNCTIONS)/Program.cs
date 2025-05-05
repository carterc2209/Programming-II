// <access level> <static or not static> <return type> name(<args>) {}
// In console app, we'll make all functions "static"
// Not static in Forms apps; always "public" though
static int add(int x, int y) {return x + y;}
static int subtract(int x, int y) {return x - y;}
static int multiply(int x, int y) {return x * y;}
static int divide(int x, int y) {return x / y;}
static void wait() {Console.ReadLine(); } // void means "return nothing" // return;

Random rand = new Random();
int n1 = rand.Next(1, 101);
int n2 = rand.Next(150, 201);
Console.WriteLine("Choose an option: add, sub, mult, or div");
string op = Console.ReadLine().ToLower();
int result = 0;
if (op == "add")
{
    result = n1 + n2;
}
else if (op == "sub")
{
    result = n1 - n2;
}
else if (op == "mul")
{
    result = n1 * n2;
}
else if (op == "div")
{
    result = n1 / n2;
}
else { Console.WriteLine("Error"); }
Console.WriteLine("Number 1: " + n1);
Console.WriteLine("Number 2: " + n2);
Console.WriteLine("Result: " + result);
wait();