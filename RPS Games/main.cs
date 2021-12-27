//#nullable disable
Console.WriteLine("Welcome to RPS! Type 'q' or 'Q' to quit.");

// Stats
uint wins = 0;
uint draws = 0;
uint loses = 0;

// Main game
while (true) {
    Console.WriteLine("Choose rock, paper, or scissors");

    // Player input
    Console.Write("~> ");
    string player = Console.ReadLine().Trim().ToLower();

    // Checking if player is valid
    // Using string.Equals to compare string objects
    if (!"rock".Equals(player) && !"paper".Equals(player) && !"scissors".Equals(player)) {
        if ("q".Equals(player)) {
            break;
        }
        Console.ForegroundColor = ConsoleColor.Red;
        Console.WriteLine($"'{player}' is not a valid option!\n");
        Console.ResetColor();
        continue; // Making sure the code does not continue
    }

    // Generating random choice for computer
    int randNumber = new Random().Next(1, 4);
    string computer = "";

    if (randNumber == 1) {
        computer = "rock";
    } else if (randNumber == 2) {
        computer = "paper";
    } else if (randNumber == 3) {
        computer = "scissors";
    }

    // Display what computer and player chose on the same line to display message
    Console.Write($"You chose {player}, and computer chose {computer}. ");

    // Display the other part
    if ("rock".Equals(player)) {
        if ("rock".Equals(computer)) { // rock : rock
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("Draw!");
            Console.ResetColor();
            draws++;
        } else if ("paper".Equals(computer)) { // rock : paper
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("You lose!");
            Console.ResetColor();
            loses++;
        } else if ("scissors".Equals(computer)) { // rock : scissors
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("You win!");
            Console.ResetColor();
            wins++;
        }
    } else if ("paper".Equals(player)) {
        if ("rock".Equals(computer)) {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("You win!");
            Console.ResetColor();
            wins++;
        } else if ("paper".Equals(computer)) {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("Draw!");
            Console.ResetColor();
            draws++;
        } else if ("scissors".Equals(computer)) {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("You lose!");
            Console.ResetColor();
            loses++;
        }
    } else if ("scissors".Equals(player)) {
        if ("rock".Equals(computer)) {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("You lose!");
            Console.ResetColor();
            loses++;
        } else if ("paper".Equals(computer)) {
            Console.ForegroundColor = ConsoleColor.Green;
            Console.Write("You win!");
            Console.ResetColor();
            wins++;
        } else if ("scissors".Equals(computer)) {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("Draw!");
            Console.ResetColor();
            draws++;
        }
    }
    Console.WriteLine("\n"); // Output a newline
}

// Display score text
Console.Write("You scored ");

// Display wins
Console.ForegroundColor = ConsoleColor.Green;
Console.Write($"{wins} wins, ");
Console.ResetColor();

// Display draws
Console.ForegroundColor = ConsoleColor.Yellow;
Console.Write($"{draws} draws, ");
Console.ResetColor();

// Display loses
Console.ForegroundColor = ConsoleColor.Red;
Console.Write($"{loses} loses");
Console.ResetColor();

Console.WriteLine("\nThanks for playing!");
Console.Write("Press any key to exit the application...");
Console.Read();
Environment.Exit(0); // Exit with statuscode 0
