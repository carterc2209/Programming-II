Console.Write("Enter a string: ");
string line1 = Console.ReadLine();
List<string> beans = new List<string>();
Console.WriteLine("Enter a character to remove: ");
string cha = Console.ReadLine();
beans.Remove(cha);
Console.WriteLine(beans);
