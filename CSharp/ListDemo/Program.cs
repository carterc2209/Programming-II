Console.WriteLine("Hello, World!");
// List<TYPE> name = new List<TYPE>();
// List<string> text = []
// List<string> lines = new List<string>();
List<int> nums = new List<int>() {1, 2, 3};
nums.Add(1);
nums.Add(5);
nums.Add(6);
nums.Add(7);
nums.RemoveAt(5); // Removes 5
nums.Remove(7);   // Removes 7
Console.WriteLine("Length: ", nums.Count);
Console.WriteLine(string.Join(", ", nums)); // "1, 2, 3, 4, 5"
// list.Sort()
// list.Reverse()
// list.find()
// list.Contains()
foreach (int n in nums)
    Console.WriteLine(n);
// list.ToArray()
// Look at C# docs on MSDN for all List methods