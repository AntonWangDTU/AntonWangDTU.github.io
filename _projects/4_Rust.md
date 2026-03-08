---
layout: page
title: Rust
description: My rust coding journey
img: assets/img/projects/rustlogo2.png
importance: 1
category: work
related_publications: true
---

<div class="row justify-content-sm-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/rustlogo.png" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
</div>


## Why Rust?

I started learning Rust because i was recorded saying that wanted to learn rust as my new years resolution for 2026, this was then posted on social media, and thus my fate was sealed. 

## What I've built so far

I was very much in doubt of how to begin with rust and what my initial way into should be, so i decided that i would start by trying to solve some of the [Rosalind challenges](https://rosalind.info/problems/list-view/). These seemed suitable as of this writing i still identify myself as a bioinformatician. 

#### **Rosalind challenges**

##### Evolution as mistakes
<details markdown="1">
<summary>Expand</summary>

In this challenge we need to find the hamming distance between two nucleotide sequences(strings).
```text
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
```

The distance is:

```text
7
```

Specific solution in rust:
The code just goes through each character of both strings simultaneously and counts ``h_distance`` + 1 if they do not match
```rust
// fn main etc...

let mut h_distance: i32 = 0;
for (char1, char2) in line1.chars().zip(line2.chars()) {
    if char1 != char2 {
        h_distance += 1;
    }
}
println!("{h_distance}");
```


<details markdown="1">
<summary>Full solution</summary>

```rust

use std::fs::File;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let file = File::open("sample.txt")?;
    let reader = io::BufReader::new(file);

    let mut line1 = String::new();
    let mut line2 = String::new();

    for (index, line) in reader.lines().enumerate() {
        let line = line?;

        if index == 0 {
            line1 = line.clone()
        }
        if index == 1 {
            line2 = line
        }
    }
    let mut h_distance: i32 = 0;

    for (char1, char2) in line1.chars().zip(line2.chars()) {
        if char1 != char2 {
            h_distance += 1;
        }
    }

    println!("{h_distance}");

    Ok(())
}
```

</details>

<details markdown="1">
<summary> My Rust language take aways</summary>

###### **std**

As i C++ : ``using namespace std`` we call the std in rust to avoid writing std:: before we call on each of the standard libraries
```rust
use std::  // your specific function
//ie
use std::io
```


###### **reading and looping through files**

In python: 
```python
with open("filename") as file:
  for line in file:
     #Do stufff
  
```
A little more complicated in rust :o We do create a file handle/variable like  in python:

```rust
use std::fs::File;

fn main() {
    let file = File::open("sample.txt")?;
}
```
But we cannot directly for loop through a variable. Why? 
Claude explains it like we have to read in the file into memory instead of reading each line from disc individually... so we use BufReader, 

```rust
use std::fs::File;
use std::io::{self, BufRead};
fn main() {
    let file = File::open("sample.txt")?;
    let reader = io::BufReader::new(file);
}
```
Are we ready to just for ``for line in reader: do stuff``??? NO! :o
We Have because when we read it the loop the `line` from: `for line in reader.line() ...`
actually returns a enum: `Result(String)` this is key take away from the rust error handling where we have to handle possible errors explicitly. In our case the enum looks like:
`Result<String, std::io::Error>`
With the expanded enum looking like
```rust
enum Result<T, E> {
    Ok(T),    // Ok(String) - successfully read a line
    Err(E),   // Err(io::Error) - something went wrong, e.g. file not found
}
```
This is what the `?` at `line?` implies, it defines a new line variable for each line `let line = line?` that can is either the string in `Ok(String)` or the `Err(io::Error)`. To clarify in even further we could get even more explicit when defining line:
```rust
 ....
for (index, line) in reader.lines().enumerate() {
    match line {
        Ok(content) => { // the '=>' implies take the string thats inside the Ok() case and call in content

            if index == 0 {
                line1 = content.clone();
            }
            if index == 1 {
                line2 = content;
            }
        }
        Err(e) => return Err(e),
    }
}

}
```
This essentially does the same. It checks line which is an enum and sees if the enum is the case of either Ok() or Err(). If it's Ok it extracts the String from inside and binds it to content. content is essentially the same variable as line was after doing let line = line? — just with a different name.


</details>
</details>

##### Introduction to Mendelian Inheritance



<details markdown="1">
<summary> Expand </summary>

Given three types of organisms:

k = Homozygous dominant : AA 

m = Heterozygous        : Aa

n = Homozygous recessive: aa

And two of each tyoe, yielding a population of 6. What is the probability that drawing two random individuals will have offspring with the dominant allele 
What draws can produce offspring with the dominant allele?


| Pairings | P(dominant allele) | probability of draw |
| -------- | ------------------ | --------------------- |
| AA + AA  | 1                  | k/t * (k-1)/(t-1)     |
| AA + Aa  | 1                  | 2 * k/t * m/(t-1)     |
| AA + aa  | 1                  | 2 * k/t * n/(t-1)     |
| Aa + Aa  | 0.75               | m/t * (m-1)/(t-1)     |
| Aa + aa  | 0.5                | 2 * m/t * n/(t-1)     |
| aa + aa  | 0                  | n/t * (n-1)/(t-1)     |


Pseudo code for a function that calculates 
```text
total = k + m + n

P(dominant) = (
    k/t * (k-1)/(t-1) * 1.0    +  # AA x AA
    m/t * (m-1)/(t-1) * 0.75   +  # Aa x Aa
    2 * k/t * m/(t-1) * 1.0    +  # AA x Aa
    2 * k/t * n/(t-1) * 1.0    +  # AA x aa
    2 * m/t * n/(t-1) * 0.5       # Aa x aa
)

```

This can be done in rust by making a function: 
```rust
fn p_dominant(k: f32, m: f32, n: f32) -> f32 {
    let t: f32 = k + m + n;
    let result = k/t * (k-1.0)/(t-1.0) * 1.0   +  // AA x AA
        m/t * (m-1.0)/(t-1.0) * 0.75  +  // Aa x Aa
        2.0 * k/t * m/(t-1.0) * 1.0   +  // AA x Aa
        2.0 * k/t * n/(t-1.0) * 1.0   +  // AA x aa
        2.0 * m/t * n/(t-1.0) * 0.5;
    // Aa x aa
    result
}
```

<details markdown="1">
<summary> Fulle rust code </summary>

```rust
use std::fs::File;
use std::io::{BufRead, BufReader};

fn p_dominant(k: f32, m: f32, n: f32) -> f32 {
    let t: f32 = k + m + n;
    let result = k/t * (k-1.0)/(t-1.0) * 1.0   +  // AA x AA
        m/t * (m-1.0)/(t-1.0) * 0.75  +  // Aa x Aa
        2.0 * k/t * m/(t-1.0) * 1.0   +  // AA x Aa
        2.0 * k/t * n/(t-1.0) * 1.0   +  // AA x aa
        2.0 * m/t * n/(t-1.0) * 0.5;
    // Aa x aa
    result
}

fn main() -> Result<(), std::io::Error> {
    let file = File::open("rosalind_iprb.txt")?;
    let first_line = BufReader::new(file).lines().next();
    let mut line1 = String::new();

    match first_line {                          // Again being extremely explicit about the enums here
        Some(result) => match result {
            Ok(line) => {
                line1 = line;
            }
            Err(e) => return Err(e),
        },
        None => panic!("File was empty"),
    }

    let parts: Vec<&str> = line1.split_whitespace().collect();

    let (k, m, n): (f32, f32, f32) = (
        parts[0].parse().unwrap(),
        parts[1].parse().unwrap(),
        parts[2].parse().unwrap(),
    );

    let homo_res = vec![2, 3, 4, 6, 7, 8, 9, 10, 15, 20, 100, 200];

    for i in &homo_res {
        println!("p(dominant) when n is {n}");

        println!("{:.5}", p_dominant(k, m, *i as f32));
    }
    println!("Final answer:");
    println!("{:.5}", p_dominant(k, m, n));

    Ok(())
}
```

</details>
</details>



##### RNA translation

<details markdown="1">
<summary> Expand </summary>
<details markdown="1">
<summary> Codon amino acid table </summary>

| Codon | AA   | Codon | AA   | Codon | AA   | Codon | AA   |
| ----- | ---- | ----- | ---- | ----- | ---- | ----- | ---- |
| UUU   | F    | CUU   | L    | AUU   | I    | GUU   | V    |
| UUC   | F    | CUC   | L    | AUC   | I    | GUC   | V    |
| UUA   | L    | CUA   | L    | AUA   | I    | GUA   | V    |
| UUG   | L    | CUG   | L    | AUG   | M    | GUG   | V    |
| UCU   | S    | CCU   | P    | ACU   | T    | GCU   | A    |
| UCC   | S    | CCC   | P    | ACC   | T    | GCC   | A    |
| UCA   | S    | CCA   | P    | ACA   | T    | GCA   | A    |
| UCG   | S    | CCG   | P    | ACG   | T    | GCG   | A    |
| UAU   | Y    | CAU   | H    | AAU   | N    | GAU   | D    |
| UAC   | Y    | CAC   | H    | AAC   | N    | GAC   | D    |
| UAA   | Stop | CAA   | Q    | AAA   | K    | GAA   | E    |
| UAG   | Stop | CAG   | Q    | AAG   | K    | GAG   | E    |

</details>

I will use a ``use std::collections::HashMap;`` for paring codons with amino acids. A hashmap is basically just like a dictionary in python - a way to match keys(codons) with valus(amino acids).

This is the heart of the code: 
```rust 
    //Go through the RNA character by character and build the codons
    let mut codon = String::new();
    let mut amino_seq = String::new();

    for n in rna.chars() {
        codon.push(n);
        if codon.chars().count() == 3 {
            let amino = codons.get(&codon).unwrap();
            if amino == "Stop" {
                break;
            }
            amino_seq.push_str(amino);
            codon.clear();
        }
    }

    println!("{}", amino_seq);
```
Here we loop through the RNA sequence and as we build the codons we match it with theur respective amino acids


</details>
