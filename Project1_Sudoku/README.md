# Welcome to Project 1: Sudoku Solver! 🧩

By **Seth Keirn** and **Alex Knutson**

📅 **8 September 2025**

---

## 🚀 The Mission

Our goal is to build a powerful Sudoku solver in **Python**! We're creating a program that can tackle Sudoku puzzles of varying difficulty, from easy breezy to mind-bendingly extreme. This project isn't just about finding the right numbers; it's about exploring different approaches to problem-solving. We'll be using five distinct algorithms to show their unique strengths and weaknesses.

---

## 🛠️ System Requirements & Parameters

To get this project running, we've set up some key parameters. You'll define these at the top of your Python file under a `\# Parameters` section.

* `GROUP_ID`: Your group number, like `Group07`.
* `ALGORITHM`: Choose one of our five super-solvers:
    * `bt` (Backtracking) 🔄
    * `fc` (Forward Checking) ➡️
    * `ac3` (Arc Consistency) 🧠
    * `sa` (Simulated Annealing) 🔥
    * `ga` (Genetic Algorithm) 🧬
* `PUZZLE_TYPE`: The difficulty level. Pick from `easy`, `medium`, `hard`, or `extreme`.
* `PUZZLE_PATH`: The location of your puzzle file. The input is a `9x9` Sudoku puzzle in a comma-delimited `.txt` file.

**Example File Name:** `Group07_fc_easy_puzzle01.txt`

---

## ⚙️ System Architecture & Flow

The system is designed with a clear, logical flow:

1.  **Puzzle Importer**: Our `PuzzleImporter` class reads your `.txt` puzzle file and turns it into a handy 2D array.
2.  **SolveCheck**: This class takes the array and hands it off to the specific algorithm you selected.
3.  **Algorithm Classes**: Each of our five algorithms (`Backtrack`, `ForwardCheck`, etc.) has its own unique method to solve the puzzle. For example, the `Backtrack` class uses a **depth-first search** to find the solution.
4.  **Output**: Once an algorithm completes its task, it returns a solved puzzle array. The program will then print the completed board and a set of statistics, like the number of backtracks or checks, to show how efficiently each algorithm performs. 

---

## 🧪 Testing Our Strategy

We're taking a step-by-step approach to testing each algorithm. Instead of throwing a whole puzzle at them at once, we'll start with smaller, more manageable problems.

* **Backtracking & Forward Checking**: We'll begin by testing with just a few 3x3 grids to easily trace our program's progress.
* **Arc Consistency (AC3)**: This one is different! Since it uses domains, we'll test with simple problems involving just two variables to see how their domains relate.
* **Simulated Annealing & Genetic Algorithms**: These two are special because they start from random points. We'll give them a set of initial, possibly incorrect, solutions and see how they iteratively improve. We'll need to pay close attention to whether they can reach a perfect solution.

---

## 🤝 Teamwork & Schedule

We're tackling this project as a team! The puzzle-loading part is straightforward, so one of us will handle that. The real fun begins with the five algorithms, which we'll be designing and coding together. We'll be using a driver/navigator approach to ensure we're both on the same page and contributing equally.

We've set up a **GitHub repository** to work remotely and keep our progress on track. We'll also be in constant contact via phone in case we hit any snags. Our goal is to have all the code and algorithms finished by mid-week of the final week, leaving us plenty of time to wrap up the final report.

Wish us luck! ✨
