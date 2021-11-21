Console.Title = "DWG";

Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine(@"
             ______        ______ 
            |  _ \ \      / / ___|
            | | | \ \ /\ / / |  _ 
            | |_| |\ V  V /| |_| |
            |____/  \_/\_/  \____|
~===============~ DWG v1.0.3 ~===============~

");
Console.ResetColor();

Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine("Enter the amount of webhooks you want to generate:");
Console.ResetColor();

int webhook_count = 0;
while (true) {
	bool success = true;
	try {
		Console.Write("~> ");
		webhook_count = int.Parse(Console.ReadLine());
		if (webhook_count <= 0) {
			throw new Exception();
		}
	} catch (FormatException) {
		success = false;
		Console.ForegroundColor = ConsoleColor.Red;
		Console.WriteLine("Invalid amount of webhooks! Please try again.");
		Console.ResetColor();
	} catch (ArgumentNullException) {
		success = false;
		Console.ForegroundColor = ConsoleColor.Red;
		Console.WriteLine("Please enter a valid amount of webhooks! Please try again.");
		Console.ResetColor();
	} catch (Exception) {
		success = false;
		Console.ForegroundColor = ConsoleColor.Red;
		Console.WriteLine("Please enter a valid number of webhooks count. Please try again.");
		Console.ResetColor();
	}
	if (success) {
		break;
	}
}

static string RandomToken() {
	const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_";
	return new string(Enumerable.Repeat(chars, new Random().Next(67, 69)).Select(s => s[new Random().Next(s.Length)]).ToArray());
}

static string RandomNumber() {
	const string chars = "0123456789";
	return new string(Enumerable.Repeat(chars, 18).Select(s => s[new Random().Next(s.Length)]).ToArray());
}

if (File.Exists("webhooks.txt")) {
	Console.ForegroundColor = ConsoleColor.Yellow;
	Console.WriteLine("Cleaning up old webhooks...");
	Console.ResetColor();
	File.WriteAllText("webhooks.txt", "");
}
for (int i = 0; i <= webhook_count; i++) {
	Console.SetCursorPosition(0, Console.CursorTop);
	Console.Write($"Generating webhooks... | {i}/{webhook_count}");
	File.AppendAllText("webhooks.txt", $"\nhttps://discord.com/api/webhooks/{RandomNumber()}/{RandomToken()}");
	Thread.Sleep(10);
}

Console.ForegroundColor = ConsoleColor.Green;
Console.WriteLine($"\nSuccessfully generated {webhook_count} webhooks!");
Console.ResetColor();

Console.WriteLine("Press any key to terminate the program...");
Console.Write("...");
Console.ReadKey();
