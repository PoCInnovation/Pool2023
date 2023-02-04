# PoC Software Pool 2023 - Day 01 - Go

Welcome to the Software pool 2023! 🚀

During this week, you will learn the base of the modern web programming, core
concept of frontend, backend, data storage... with a piece of devops.

**Day purposes**

✔️ Setup a Go project.

✔️ Learn basics of Go.

✔️ Discover software development good practices.

✔️ Introduce you to design pattern, especially MVC.

✔️ Create an interactive application using your terminal.

## Introduction

### Requirements

Go is a powerful language with many features and capabilities, you can
manage any Go project from its [complete CLI](https://go.dev/doc/install).

With it, you can build a go binary, download dependencies, format your code...
If you are curious, you can [look at the CLI documentation](https://pkg.go.dev/cmd/go) 😉

Start by [installing the CLI](https://go.dev/doc/install), you can verify that
everything works using the command below:
```shell
# Version must be at least 1.16
go version
# go version go1.19.4 linux/amd64
```

> If you have any issue don't hesitate to ask the staff for help 😄

### Why Go?

Go is an open source programming language created and maintained by Google.<br>
It solves several problems of the modern software world thanks to its simplicity
and incredible standard library. It's also really strong to build
[microservices](https://www.encora.com/insights/building-microservices-with-golang-and-go-kit)
and [software that required high level of performance](https://www.willowtreeapps.com/craft/the-pros-and-cons-of-programming-in-go).

Go has many usage, you can write powerful cloud & networks, CLI, 
API or DevOps tools.<br>
Because it's a compiled language, it's really fast, much faster than [Javascript for instance](https://qvault.io/golang/node-js-vs-go/) 🏃

Here's an exhaustive list of Go killer features:
- Easily solve complex concurrency issues with [go routine](https://gobyexample.com/goroutines).
- Strongly statically typed
- Amazing dependency management with [go module](https://medium.com/@adiach3nko/package-management-with-go-modules-the-pragmatic-guide-c831b4eaaf31)
- Multi-paradigm from [OOP](https://www.toptal.com/go/golang-oop-tutorial) to [functional](https://medium.com/@geisonfgfg/functional-go-bc116f4c96a4)

### Warp up

Let's begin this pool with a simple warm up: [The Go Tour](https://go.dev/tour/welcome/1)<br>
This tour is a set of exercise to learn Go basics.

You can also try the [Go Playground](https://go.dev/play/), a useful tool to test or share pieces of codes.

You will also need a good IDE, we recommend [Visual Studio Code](https://code.visualstudio.com)
or [GoLand](https://www.jetbrains.com/fr-fr/go/).

In summary, here's a bunch of links that will be very useful during the pool:
- [Go Docs](https://go.dev/doc/)
- [Go Playground](https://go.dev/play/)
- [Go Tour](https://go.dev/tour/list)
- [Visual Studio Code Go plugin](https://code.visualstudio.com/docs/languages/go)
- [GoLand](https://www.jetbrains.com/fr-fr/go/)
- [Standard Library](https://pkg.go.dev/std)

## Step 0 - Setup

As usual, every exercise must be pushed to a git repository.<br>

To make it easier, we will use a GitHub classroom! Follow this [link](https://classroom.github.com/a/DoR-K1PO) to create your git repository.

Then, you can clone your repository.

```shell
git clone git@github.com:PoC-Community/software-pool-days-{YOUR-GITHUB-USERNAME}.git
```

For each day, we will create a new folder. Start with the `day01`.

```shell
mkdir -p day01
```

Inside it, let's initialize a Go project

```shell
go mod init SoftwareGoDay1
> go: creating new go.mod: module SoftwareGoDay1
```

You should see a [`go.mod`](https://faun.pub/understanding-go-mod-and-go-sum-5fd7ec9bcc34?gi=7a3186a145d6) file appear in your directory.

You can now create your first go file: `main.go` 🎉

```go
package main

import "fmt"

func main() {
  fmt.Println("You are ready to start the 2023 PoC software pool!")
}
```

> 💡 If you are curious about this, check the [fmt package documentation](https://pkg.go.dev/fmt)

Let's execute it:
```shell
# Use `go run` to execute your program without building the binary
go run SoftwareGoDay1 # Or go run ./main.go

# You can also build and run it in separate command
go build SoftwareGoDay1
./SoftwareGoDay1

# You should have the following output
> You are ready to start the 2023 PoC software pool!
```

Before going further, do the [Go Tour](https://go.dev/tour/basics/1) and read
the [package documentation](https://medium.com/rungo/everything-you-need-to-know-about-packages-in-go-b8bac62b74cc), those core concepts are important to understand the rest of the pool 💯

## Step 1 - Hello World

It's time to start coding! We will start with a simple `helloWorld` package.

Let's create a folder `helloWorld` with a file `helloWorld.go` in it.

```shell
mkdir -p helloWorld
```

You will implement a function `HelloWorld` that will display `Hello World!`
in your terminal.

> Don't forget to add the correct package name at the top of `helloWorld.go` 😉

Update the file `main.go` to call `HelloWorld`.

> 💡 Here's a couple of slides about [what is a good naming in Go](https://go.dev/talks/2014/names.slide#1).

## Step 2 - Loops, conditions, array and unit tests

The purpose of this step is to use what you have learned during the [Go Tour](https://go.dev/tour/welcome/1) 👀

Let's create a function to sort numbers so we can cover useful concepts such as loops, conditions, arrays and tests 🥳

Your function must:
1. Sort a list in ascending order
2. Remove odd numbers
3. Format the result to return

### Sort like a pro

Create a new package `getEvenNumbers` with a file `getEvenNumbers.go`.

```shell
mkdir -p getEvenNumbers
```

Create a function `GetEvenNumbers` that will take an array of int.<br>
It must sort the array in ascending order and return a string that
contains only pairs number in ascending order, split by a `-`.

Update `main.go` to call `GetEvenNumbers` and display the result:
```go
array := []int{
  	1,
  	0,
  	19,
  	17,
  	16,
  	8,
  	13,
  	24,
  }

fmt.PrintLn(getEvenNumbers.GetEvenNumbers(array))
```

You should have the following result:
```shell
0 - 8 - 16 - 24
```

### Test like a pro 🧪

It's really important to correctly test your code, a code not tested can lead
 to unpredictable bugs and the time lost to debug it could be avoided by creating some tests.

To do so, Go provides a [built-in test package](https://pkg.go.dev/testing),
with a [clean way to organize your tests](https://dave.cheney.net/2019/05/07/prefer-table-driven-tests) 💥

Let's create a test file named `getEvenNumbers_test.go`.

To make sure your `getSortedEvenNumbers` works as intended, you can write a test for each of these cases:
- Only positive numbers
- Only negative numbers
- Mixed numbers

You can then execute them with `go test`, which should produce a result similar to this one:
```
go test ./getEvenNumbers -v

=== RUN   TestGetEvenNumbersCasePositive
--- PASS: TestGetEvenNumbersCasePositive (0.00s)
=== RUN   TestGetEvenNumbersCaseNegative
--- PASS: TestGetEvenNumbersCaseNegative (0.00s)
=== RUN   TestGetEvenNumbersCasePositiveAndNegative
--- PASS: TestGetEvenNumbersCasePositiveAndNegative (0.00s)
PASS
ok      SoftwareGoDay1/getEvenNumbers     0.001s
```

## Step 3 - My name is ...

Now it's time to learn how to read input from the terminal 🤩

Create a new package `whatIsYourName` with a file `whatIsYourName.go` and a function `WhatIsYourName` inside it.
```shell
mkdir -p whatIsYourName
```

This function must display a prompt in the terminal to ask a user
to fill his name and retrieve it.

To do so, you can use the [bufio](https://pkg.go.dev/bufio) and [os](https://pkg.go.dev/os) packages 😉

You should end up with the following behavior:
```shell
What is your name ?
# User fill input
> Slim Shady

# Display input
Your name is Slim Shady
```

Don't forget to call it from `main.go` and [correctly manage errors](https://medium.com/gett-engineering/error-handling-in-go-53b8a7112d04).

> 💡 Display your errors using the [log package](https://pkg.go.dev/log)
and [`fmt.Errorf`](https://pkg.go.dev/fmt#Errorf).

### Testing time

It's really hard to test I/O with unit test, but that's why functional tests exist!

[Download them from GitHub](./resources/testWhatIsYourName.zip)
and extract sources in your directory 📁

Then, create a binary of your project using `go build`.

You can now simply execute `testWhatIsYourName` to launch the tests of your function:
```shell
OK - TEST 1 PASSED
OK - TEST 2 PASSED
OK - TEST 3 PASSED
```

> Don't hesitate to add more tests and modify your program to make sure all of them pass 🧪

## Step 4 - Make it the cutest code that I have ever seen

As we said in the introduction, Go come with great built-ins to help you
during your development.

One of these tools is [gofmt](https://pkg.go.dev/cmd/gofmt), a powerful formatting tool that will help you have standard coding style rules in your code.  
> Its really helpful on the format, but having a [clean code architecture](https://en.wikipedia.org/wiki/SOLID) is up to you 🚀

To use [gofmt](https://pkg.go.dev/cmd/gofmt), just launch `go fmt .` at the
root of your module 😉

You can also configure [VSCode](https://code.visualstudio.com/docs/languages/go#_formatting)
or [GoLand](https://www.jetbrains.com/help/go/integration-with-go-tools.html#gofmt)
to format your code on save.

## Step 5 - Artists Book v1.0

You are ready for a complex exercise. Let's create our first application!

It will be a program that help you manage your favorite artists from your terminal.

We will not code everything in one step, that would be too huge for this moment.

⚠️ Read the **whole** step before coding, it will help you understand
what to do and how to do it

Let's start with a simple implementation. The goal is to have a CLI similar to this one:
```text
Welcome into your Artists Book!

What do you want to do?
1 - List my favorite artists
2 - Leave

# User tip input
> 3

Tip 1 or 2.

# User tip input
> 1

Here's your favorite artists:
-- 1 -- B2O
-- 2 -- SCH
-- 3 -- Laylow
-- 4 -- Billie Eilish

What do you want to do?
1 - List my favorite artists
2 - Leave

# User tip input
> 2

See you!
```

To do this, we must build a program that follows a strong architecture.
We will use one of the most popular: [MVC](https://www.calhoun.io/using-mvc-to-structure-go-web-applications/).

MVC stands for **Model - View - Controller**. It's an architecture where your
code logic is split into smaller parts to easily maintain and scale a project.

We will now adapt MVC to our need, don't worry if we do not strictly follow the architecture.

Here's a schema of your architecture:
![Artists Book architecture](../../../.github/assets/software_mvc.png)

Let's code step by step 😄

### Router

Router corresponds to the entrypoint of your program and the main loop.<br>
It has different roles:
- Display actions to user.
- Catch the user input.
- Call `controllers` to execute the action asked by the user.

A good architecture also requires a good folder management in your code.
Each _resource_ must be in its own package and with the `router` making the link
between them.

- Create a package `artistsBook` with a file `router.go` in it.
- Create a function `Router` that will do the loop described in the example.
> You are big boy/girl now, you got the keys to do it by yourself 💪
- Update `main.go` to call `Router`.

### Controllers

A controller is in charge of the business logic that manages your resources.

Its only purpose is to create the link between the function that manage your
data storage (for now it will be a simple `JSON` file) and functions exposed
to the user.

- Create a package `controllers` in `artistsBook` folder.
- Create a sub-package `artists` in it.
- Create a file `display.go`
- Write the function `DisplayAll` that controls the display of the user's favorite artists

### Repositories

A repository is responsible for all interactions with the data storage.

- Create a package `repositories` in the `artistsBook` folder.
- Create a sub-package `artists` in it.
- Create a file `get.go`
- Write the function `GetAll` that retrieves user's favorite artists

> You will need the [os](https://pkg.go.dev/os) and [json](https://pkg.go.dev/encoding/json) packages to read a file (see more information below).

### Views

A view expose a list of functions to the user to make it interact with a resource.

- Create a package `views` in `artistsBook` folder.
- Create a sub-package `artists` in it.
- Create a file `display.go`
- Write the function `DisplayAll` that display the user's favorite artists in the terminal.

### Models

A model defines the type of the stored data.

- Create a package `models` in `artistsBook` folder.
- Create a sub-package `artist`
- Create a file `artist.go` in it
- Export a [struct](https://www.geeksforgeeks.org/structures-in-golang/)
`Artist` that contains a field `name` of type `string`

### Data

Data defines your storage, it can be a database, an Excel file or whatever that
can store data. Here, it will be a simple `JSON` file.

> [JSON](https://en.wikipedia.org/wiki/JSON) stands for JavaScript Object Notation.
> It's a standard like `CSV`, `XML` or `YAML` used to define a structured data.

> We'll discover real databases tomorrow 👀

- Create a directory `data` in the `artistsBook` folder.
- Create the file `artists.json` with the following content :

```json
[
  {
    "name": "B2O"
  },
  {
    "name": "SCH"
  },
  {
    "name": "Laylow"
  },
  {
    "name": "Billie Eilish"
  }
]
```

### Summary

Finally, you should have the following architecture:

```text
artistsBook/
  router.go
  controllers/
    artists/
       display.go
  repositories/
    artists/
      get.go
  views/
    artists/
       display.go
  models/
    artist.go
  data/
    artists.json
```

This exercise may seems hard but if you write your code step by step, it will
be a piece of cake 🍰!

## Step 6 - Artists Book v2.0

You've built the base of your MVC architecture, it's time to improve it 📈

For now, you can only read data, let's add operations to create, update or delete it.

Those four primitive operations are mandatory to manage a resource in a data storage.
They are usually called [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete),
which stands for **CREATE - READ - UPDATE - DELETE**.

Let's add the missing ones 🚀

### CREATE

Update your codebase to allow a user to **add** a new artist to his list.

#### Repository

Add a file `create.go` in your artists repository that will contain
the function `Create` to add an artist to the database.

> ⚠️ You will need to write the whole `artists.json` file  
> Take care to not **lose data** when you rewrite the file.

#### View

- Create the file `ask.go` in the `views/artists` directory.
- Write the function `AskName` that retrieve an artist's name from the terminal.

> 💡 You can copy code from the precedent step to win time 

#### Controller

- Create the file `create.go` in `controllers/artists` directory.
- Write the function `Create` that controls the artist addition.

#### Routing

Add the possibility to create an artist in `router.go`.

#### Result

You can code other functions to make your code works. For example, a function to
display the artist name if it has been correctly added to the list.<br>
This function should be in the views, in `display.go` for example.


You should have the following result: 

```text
Welcome into your Artists Book!

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Leave

# User tip input
> 2

What's the artist's name?

# User tip input
> Bob Marley

Bob Marley has been added to your favorite artists!

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Leave

# User tip input
> 1

Here's your favorite artists:
-- 1 -- B2O
-- 2 -- SCH
-- 3 -- Laylow
-- 4 -- Billie Eilish
-- 5 -- Bob Marley

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Leave

# User tip input
> 2

What's the artist's name?

# User tip input
> Bob Marley

Bob Marley already exists!

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Leave

# User tip input
> 3

See you!
```

### UPDATE

Update your application to allow the user to **update** an artist in his list.

#### Repository

Create the file `update.go` in your `repository/artists` folder.

Add the function `Update` to modify an artist in the data storage.

#### View

Add the function `AskNewName` in your `views/artists` directory.

> I'm sure you have understood the logic 🧠

#### Result

Don't forget to update your `controller`, the `router` and add anything
required to correctly update an artist.

You should have a result similar to this one:

```text
Welcome into your Artists Book!

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Leave

# User tip input
> 2

What's the artist's name?

# User tip input
> Bob Marley

Bob Marley has been added to your favorite artists!

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Update an artist in my favorite
4 - Leave

# User tip input
> 3

What's the name of the artist you want to update?

# User tip input
> unknown

What will be the new name of unknown?

# User tip input
> Mac Miller

unknown is not in your favorite list.

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Update an artist in my favorite
4 - Leave

# User tip input
> 3

What's the name of the artist you want to update?

# User tip input
> B20

What will be the new name of unknown?

# User tip input
> Booba

B2O has been successfully updated.

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Update an artist in my favorite
4 - Leave

# User tip input
> 1

Here's your favorite artists:
-- 1 -- Booba
-- 2 -- SCH
-- 3 -- Laylow
-- 4 -- Billie Eilish
-- 5 -- Bob Marley

What do you want to do?
1 - List my favorite artists
2 - Add an artist to my favorite
3 - Update an artist in my favorite
4 - Leave

# User tip input
> 4

See you!
```

### DELETE

Update your codebase to allow user to **remove** an artist from his list.

It's up to you to find the best way to do it 🚀

## Step 7 - Artists Book v3.0

You have implemented a complete MVC architecture, that's excellent 🚀

Only one thing is missing, our data is too basic, it only has a name.

Let's add some fields by updating the `Artist` structure:
- `id`: A [unique identifier](https://pkg.go.dev/github.com/aidarkhanov/nanoid) of type `string`
- `top`: Best song, as a `string`
- `fans`: `number` of fans
- `listenedTime`: the amount of time you listened to this artist. It must be stored as a [`Time`](https://pkg.go.dev/time)

>💡 It's common to put a unique identifier when you store data, this way, you can easily distinguish them.

You'll have to update all your codebase to support those new fields.

> Don't worry, it's not that hard because you have build a strong architecture!  
> And if you struggle, remember that the staff is here to help you out 😃

## Step 8 - Interface

It's time to learn another important concept in Go: [interfaces](https://go.dev/tour/methods/9).

To do so, we will do a simple example with geometric shapes 🟥

Let's create a package `geometricShape`.
```shell
mkdir -p geometricShape
```

### Definition

Inside it, create an interface `GeometricShape` with a method `CalcPerimeter`.<br>
This method must have the following prototype:
```go
CalcPerimeter() float64
```

Create a function `CalcPerimeter` that will take this time an interface
`GeometricShape` **as parameter** and return the result of the function
`CalcParameter` called from the interface.

Here's a prototype to help you:
```go
func CalcPerimeter(shape GeometricShape) float64
```

### Shapes

Create the struct `Circle` with a field `Radius`.<br>
Create the struct `Rectangle` with a field `X` and `Y`.<br>
Create the struct `Triangle` with a field `X`, `Y` and `Z`.

For each shape, implement the method `CalcParameter` that will return
the parameter of the shape.

Here's an example of prototype for a `Square`:
```go
func (square Square) CalcPerimeter() float64 {}
```

> 💡 As you may have noticed, you can write a Go function in this order too (parameters before the function name)

### Upgrade

Update the file `main.go` to create 3 shapes:
- A `Circle` with `radius`: `12.0`
- A `Rectangle` with `X`: `2.0` and `Y`: `3.0`
- A `Triangle` with `X`: `5.0`, `Y`: `2.0` and `Z`: `1.0`

For each shape, display their perimeter using `CalcPerimeter` from the package `geometricShape`.

Here's an example of output:
```shell
&{12} has a perimeter of 75.398224
&{2 3} has a perimeter of 10.000000
&{5 2 1} has a perimeter of 8.000000
```

As you can see, it's not clear... Let's use the power of interfaces to
fix that 😃

The package `fmt` call the method [`String`](https://go.dev/tour/methods/17) of given the given argument to display it properly.<br>

> So if our structures implement the method `String`, you can control the 
way it's displayed by `fmt` 😉

Update your structures to print it correctly, here's an example of prototype 
with `Square`:
```go
func (square Square) String() string {}
```

Thanks to interfaces, you do not have to change anything in `main.go`,
just rerun the program and appreciate the moment 😍

```shell
# You can configure `String()` to display this
Circle: { radius = 12 } has a perimeter of 75.398224
Rectangle: { X = 2, Y = 3 } has a perimeter of 10.000000
Triangle: { X = 5, Y = 2, Z = 1 } has a perimeter of 8.000000
```

## Step 9 - Artists Book v4.0

Since you now know interfaces, why not use it in your MVC?

The purpose is to update `Artist` to correctly display it with `fmt` package.

In your `artist` model, implement the method `String`.

You can also update `DisplayAll` from your `views` to use a simple `fmt.Printf`
to display `Artist`.

## Bonus

First, congratulation! You've survived day 1 👏

Your MVC currently manages only one resource: `Artist`.

You can create a new resources named `Music` containing the following data:
- `id`: Resource unique identifier
- `artist`: Owner of the music
- `name`: Music's title
- `listened`: Number of listening
- `link`: A link to the music (E.g: `spotify`, `youtube`...)

You're free to add any features to your application.

You can maybe start by adding the **CRUD** for your new `Music` resource.

## Additional resources

- [Clean code in Go](https://github.com/Pungyeon/clean-go-article#Clean-Go)
- [Go benchmark](https://dave.cheney.net/2013/06/30/how-to-write-benchmarks-in-go)
- [Go amazing project](https://github.com/avelino/awesome-go)
- [Generics](https://go.dev/doc/tutorial/generics)
- [Go routines](https://medium.com/technofunnel/understanding-golang-and-goroutines-72ac3c9a014d)
- [Courses](https://www.calhoun.io)

<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn logo">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram logo"
>
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter logo">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord logo">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white" alt="Website logo">
    </a>
</p>

> 🚀 Don't hesitate to follow us on our different networks, and put a star 🌟 on `PoC's` repositories.