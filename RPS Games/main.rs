#![allow(non_snake_case)] // Doing so because 'RPS' crate is all uppercase

use rand::Rng;
use std::io::Write;
use std::process::exit;
use colour::*;
fn main() {
    println!("Welcome to RPS! Type 'q' or 'Q' to quit.");

    // Stats
    let mut wins: u64 = 0;
    let mut draws: u64 = 0;
    let mut loses: u64 = 0;

    // Main game
    loop {
        println!("Choose rock, paper, or scissors");

        // Player input
        print!("~> ");
        std::io::stdout().flush().unwrap();
        let mut player: String = String::new();
        std::io::stdin().read_line(&mut player).unwrap();
        player = player.trim().to_lowercase();

        // Checking if player is valid
        if player != "rock" && player != "paper" && player != "scissors" {
            if player == "q" {
                break;
            }
            if player.chars().count() >= 70 || player.is_empty() {
                red_ln!("[bad string] is not a valid option!");
            } else {
                red_ln!("'{}' is not a valid option!", player);
            }
            println!(" "); // Insert a newline
            continue; // Skip to next iteration of the loop
        }

        // Generating random choice for computer
        let rand_number: u8 = rand::thread_rng().gen_range(1..=3); // Generate number between 1 and 3
        let computer: &str;

        if rand_number == 1 {
            computer = "rock";
        } else if rand_number == 2 {
            computer = "paper";
        } else {
            computer = "scissors";
        }

        // Display results
        print!("You chose {}, and computer chose {}. ", player, computer);
        if player == "rock" {
            if computer == "rock" { // rock:rock
                yellow!("It's a draw!");
                std::io::stdout().flush().unwrap();
                draws += 1;
            } else if computer == "paper" { // rock:paper
                red!("You've lost!");
                std::io::stdout().flush().unwrap();
                loses += 1;
            } else { // rock:scissors
                green!("You've won!");
                std::io::stdout().flush().unwrap();
                wins += 1;
            }
        } else if player == "paper" {
            if computer == "rock" { // paper:rock
                green!("You've won!");
                std::io::stdout().flush().unwrap();
                wins += 1;
            } else if computer == "paper" { // paper:paper
                yellow!("It's a draw!");
                std::io::stdout().flush().unwrap();
                draws += 1;
            } else { // paper:scissors
                red!("You've lost!");
                std::io::stdout().flush().unwrap();
                loses += 1;
            }
        } else {
            if computer == "rock" { // scissors:rock
                red!("You've lost!");
                std::io::stdout().flush().unwrap();
                loses += 1;
            } else if computer == "paper" { // scissors:paper
                green!("You've won!");
                std::io::stdout().flush().unwrap();
                wins += 1;
            } else { // scissors:scissors
                yellow!("It's a draw!");
                std::io::stdout().flush().unwrap();
                draws += 1
            }
        }
        println!("\n"); // Insert a newline
    }
    // Display stats
    print!("You scored ");
    green!("{} wins, ", wins);
    yellow!("{} draws, ", draws);
    red!("{} loses", loses);
    std::io::stdout().flush().unwrap();

    println!("\nThanks for playing!");
    print!("Press any key to continue...");

    std::io::stdout().flush().unwrap();
    let mut temp: String = String::new();
    std::io::stdin().read_line(&mut temp).unwrap();
    drop(temp);

    // Terminate application
    exit(0);
}