using Flurl.Http;

Console.Title = "DWS";
Console.OutputEncoding = System.Text.Encoding.UTF8;

static void exit() {
    Console.ResetColor();
    Console.Write("Press any key to exit the application...");
    Console.ReadKey();
    Environment.Exit(0);
}

Console.ForegroundColor = ConsoleColor.Blue;
Console.WriteLine(@"
  ______
 / _____)
( (____  ____  _____ ____  ____  _____  ____ 
 \____ \|  _ \(____ |    \|    \| ___ |/ ___)
 _____) ) |_| / ___ | | | | | | | ____| |
(______/|  __/\_____|_|_|_|_|_|_|_____)_|
        |_|
───────────────────────────────────────────────");
Console.ResetColor();
Console.WriteLine("Felierix's Webhooks Spammer\nVersion: 2.3.6\n");

Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine("Enter the webhook URL");
Console.ResetColor();
Console.Write("~> ");

string webhook_url = Console.ReadLine();
if (!webhook_url.StartsWith("https://discord.com/api/webhooks/")) {
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("Invalid webhook url! Please try again.");
    Console.ResetColor();

    while (!webhook_url.StartsWith("https://discord.com/api/webhooks/")) {
        Console.Write("~> ");
        webhook_url = Console.ReadLine();
    }
}

int testWebhook = (await webhook_url.AllowAnyHttpStatus().GetAsync()).StatusCode;
if (testWebhook == 404) {
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("[404] Specified webhook doesn't exist or was deleted!");
    exit();
} else if (testWebhook == 401 || testWebhook == 403) {
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("[401/403] Access was forbidden to the webhook!");
    exit();
} else if (testWebhook == 502) {
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("[502] There was not a gateway available to process the request!");
    exit();
} else if (testWebhook == 405) {
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("[405] The HTTP method used is not valid for the location specified!");
    exit();
}
Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine("\nEnter webhook's username");
Console.ResetColor();
Console.Write("~> ");

string user = Console.ReadLine();
if (user.Length <= 0 || user.Length > 32) {
    if (user.Length <= 0) {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("[!] Username length is shorter than 0 characters! Do you want to skip the username parameter? [y/n]");
        Console.ResetColor();
        Console.Write("~> ");

        if (Console.ReadLine().ToLower().StartsWith("y")) {
            user = "Default Webhook";
        } else {
            Console.WriteLine("Please enter the new webhook's username:");
            Console.Write("~> ");
            user = Console.ReadLine();
        }
    } else if (user.Length > 32) {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("[!] Username length is longer than 32 characters! Do you want to skip the username parameter? [y/n]");
        Console.ResetColor();
        Console.Write("~> ");

        if (Console.ReadLine().ToLower().StartsWith("y")) {
            user = "Default Webhook";
        } else {
            Console.WriteLine("Please enter the new webhook's username:");
            Console.Write("~> ");
            user = Console.ReadLine();
        }
    } else {
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("[!] An error occurred!");
        Console.ResetColor();
        exit();
    }
}

Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine("\nEnter message content:");
Console.ResetColor();
Console.Write("~> ");

string msgcontent = Console.ReadLine();
if (msgcontent.Length >= 2000) {
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("[!] Message cannot be longer than 2000 characters!");
    Console.ResetColor();
    while (msgcontent.Length >= 2000) {
        Console.Write("~> ");
        msgcontent = Console.ReadLine();
    }
}

Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine("\nHow many messages per row?");
Console.ResetColor();
int thread_count = 0;

while (true) {
    bool passed = true;
    try {
        Console.Write("~> ");
        thread_count = int.Parse(Console.ReadLine());
    } catch (Exception e) {
        passed = false;
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("[!] " + e);
        Console.ResetColor();
    }
    if (passed) {
        break;
    }
}

if (thread_count is >= 50 or < 1) {
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("[!] Too high/low amount of messages per row is strictly forbidden! Please enter it again!");
    Console.ResetColor();
    while (true) {
		bool didPass = true;
        Console.Write("~> ");
        try {
            thread_count = int.Parse(Console.ReadLine());
        } catch (FormatException) {
			didPass = false;
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("[!] Please enter integer number!");
            Console.ResetColor();
        }
        if (thread_count is >= 50 or < 1) {
			didPass = false;
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("[!] Too high/low amount of messages per row is strictly forbidden!");
            Console.ResetColor();
        } else {
			didPass = true;
        }
		if (thread_count is not >= 50 or < 1 && didPass) {
			break;
		}
    }
}

Console.ForegroundColor = ConsoleColor.Cyan;
Console.WriteLine("\nEnter the cooldown after each message in miliseconds (1000ms = 1s):");
Console.ResetColor();

int delay = 0;
while (true) {
    bool passed1 = true;
    try {
        Console.Write("~> ");
        delay = int.Parse(Console.ReadLine());
		if (delay <= 350) {
			throw new Exception();
		}
    } catch (FormatException) {
        passed1 = false;
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine("[!] Please enter an integer or float number!");
        Console.ResetColor();
    } catch (Exception) {
		passed1 = false;
		Console.ForegroundColor = ConsoleColor.Red;
    	Console.WriteLine("[!] Delay cannot be smaller than 350ms! Please enter it again");
    	Console.ResetColor();
	}
    if (passed1) {
        break;
    }
}

Console.ForegroundColor = ConsoleColor.DarkBlue;
Console.WriteLine("\n──────────── SPAMMING ────────────");
Console.ResetColor();

async void do_request() {
    while (true) {
        IFlurlResponse request = await webhook_url.AllowAnyHttpStatus().PostJsonAsync(new {
            username = user,
            content = msgcontent,
        });
        if (request.StatusCode == 404 || request.StatusCode == 502) {
            Console.WriteLine("Webhook owner deleted the webhook! :c");
            exit();
        } else if (request.StatusCode == 429) {
            try {
                int RetryAfter = int.Parse(Convert.ToString(request.ResponseMessage.Headers.RetryAfter)) + 15;
                Console.WriteLine($"[Ratelimit] Webhook is ratelimited for {RetryAfter - 15}ms! Bypassing...");
                Thread.Sleep(millisecondsTimeout: RetryAfter);
                Console.WriteLine("[Ratelimit] Bypassed!");
            } catch (OverflowException) {
                Console.WriteLine("[Critical Error] Webhook ratelimit value is too large to parse! Attempting bypass...");
                Thread.Sleep(millisecondsTimeout: 50*1000);
            }
        }
        Thread.Sleep(millisecondsTimeout: delay);
    }
}

List<Thread> threads = new();
for (int i = 0; i < thread_count; i++) {
    Thread t = new(start: do_request);
    t.Start();
    threads.Add(t);
}

foreach (Thread thread in threads) {
    thread.Join();
}

Console.ForegroundColor = ConsoleColor.DarkGray;
Console.WriteLine("~ Press enter to exit the application\n");
Console.ResetColor();
Console.WriteLine("Messages are sending now! We'll inform you if we've got an error.");
Console.ReadKey();
