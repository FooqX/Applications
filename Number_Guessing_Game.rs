use rand::Rng; // Include rand dependency in cargo.toml (rand = 'latest version goes here')
use std::cmp::Ordering;

fn main() {
    let _play_again = true;
    println!("== Guess a number game ==\n");

    while _play_again {
        let guess = 0;
        let mut guesses = 0;
        let secret_number = rand::thread_rng().gen_range(1..101);
        while guess != secret_number {
            println!("Guess a number between 1 - 100.");
            let mut guess: String = String::new();
            std::io::stdin()
                .read_line(&mut guess)
                .expect("Failed to read line");
            let guess: u32 = match guess.trim().parse() {
                Ok(num) => num,     // Return number
                Err(_) => continue, // Ignores error by skipping to next iteration
            };

            match guess.cmp(&secret_number) {
                Ordering::Less => println!("Too small!"),
                Ordering::Greater => println!("Too big!"),
                Ordering::Equal => break,
            }
            guesses += 1;
        }
        println!("Secret number was {}.", secret_number);
        println!("You win!");
        println!("It took you {} guesses.", guesses);

        println!("\nWould you like to play again? (y/n)");
        let mut choice = String::new();
        std::io::stdin()
            .read_line(&mut choice)
            .expect("Failed to read line");
        if choice.to_lowercase() == "y" {
            if !_play_again {
                let _play_again = true;
            }
        } else {
            let _play_again = false;
        }
    }
    let mut temp = String::new();
    println!("Thanks for playing!");
    std::io::stdin()
        .read_line(&mut temp)
        .expect("Failed to read line");
    drop(temp);
}
