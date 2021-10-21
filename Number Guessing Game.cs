# NET 6

#nullable disable // fix many ANNOYING problems with null

while (true) {
    int guess = 0;
    int guesses = 0;
    Random random = new Random();
    int number = random.Next(1, 101);

    while (guess != number) {
        Console.WriteLine("Guess a number between 1 to 100");
        Console.Write("~> ");
        try {
            guess = Convert.ToInt16(Console.ReadLine());
        } catch (Exception ex) {
            Console.WriteLine("[!] " + ex.Message);
        }


        if (guess > number) {
            Console.WriteLine(guess + " is too high!");
        } else if (guess < number) {
            Console.WriteLine(guess + " is too low!");
        }
        guesses++;
    }
    Console.WriteLine("Congratulations on winning guess a number game!");
    Console.WriteLine("Number: " + number + "\nGuesses: " + guesses + "\n");
    Console.WriteLine("Do you want to play again? (y/n)");
    Console.Write("~> ");
    string response = Console.ReadLine();

    if (!response.ToUpper().StartsWith("Y")) {
        break;
    }
}
