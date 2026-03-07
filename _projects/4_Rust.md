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

I was very much in doubt of how to begin with rust and what my initial way into should be, so i decided that i would start by trying to solve some of the [Rosalind challenges](https://rosalind.info/problems/list-view/). These seemed suitable as of writing this still identify myself as a bioinformatician. 

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


