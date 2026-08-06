# Day-79-Find-Common-Characters

Day 79/100 - Python Program to Find Common Characters in Two Strings

# Find Common Characters in Two Strings

A program to dynamically compare two user-provided strings and extract the unique characters that appear in both sequences by utilizing Python's highly optimized `set` data structure.

## 📝 Description

This program analyzes two separate strings inputted by the user to determine exactly which characters they share in common.

The core logic is efficiently contained within the `find_common_characters(str1, str2)` function. Rather than using nested loops to manually compare every single character—which can be slow and inefficient—this script leverages Python's built-in mathematical sets. First, it converts both strings into sets using `set(str1)` and `set(str2)`. This action automatically removes any duplicate characters within the individual strings. Next, it utilizes the `.intersection()` method (`set1.intersection(set2)`). This built-in set operation instantly calculates and returns a new set containing only the elements that exist in both `set1` and `set2`. Finally, the driver code accepts the user inputs, executes the function, and prints the resulting set to the console.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string of text representing the first sequence (`str1`), provided via the terminal prompt.


* **Input 2:** A string of text representing the second sequence (`str2`), provided via the terminal prompt.



### Output:

* A formatted string stating: "Common characters: [common_chars]" where `[common_chars]` is a Python set object containing the matching elements.



### Rules:

1. The program must prompt the user to input two separate strings.


2. The core logic must be encapsulated in a function named `find_common_characters(str1, str2)`.


3. The function must convert both input strings into sets.


4. The function must use the `set1.intersection(set2)` method to identify overlapping characters.


5. The driver code must capture the returned set and print it to the console.



---

## 💡 Examples

### Example 1 (Standard Words)

**Input:**

```text
apple
peach

```

**Output:**

```text
Common characters: {'p', 'e', 'a'}

```

**Explanation:** The program converts "apple" to `{'a', 'p', 'l', 'e'}` and "peach" to `{'p', 'e', 'a', 'c', 'h'}`. The intersection perfectly isolates 'p', 'e', and 'a'. (Note: Sets are unordered collections, so the print order may vary.)

### Example 2 (Case Sensitivity & Spaces)

**Input:**

```text
Hello World
python

```

**Output:**

```text
Common characters: {'o', 'h'}

```

**Explanation:** Python sets evaluate characters with strict case sensitivity. The lowercase 'h' and 'o' in "python" perfectly match the lowercase 'h' and 'o' (from "World") in the first string. The uppercase 'H' is ignored.

### Example 3 (No Common Characters)

**Input:**

```text
abc
xyz

```

**Output:**

```text
Common characters: set()

```

**Explanation:** Because the two strings share absolutely no characters, the `.intersection()` method returns an empty set, which Python represents dynamically as `set()` to differentiate it from an empty dictionary.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 79.py").

```bash
git clone https://github.com/adiaryaz/Day-79-Find-Common-Characters.git
cd find-common-characters

```

2. **Run the program**:

```bash
python "Day 79.py"

```

Enter your two strings sequentially when prompted to instantly discover exactly which characters they share!
