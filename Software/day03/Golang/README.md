# PoC Software Pool 2023 - Day 03 - REST API

**Day purposes**

✔️ Discover HTTP server with Gin.

✔️ Learn the basics and good practices of web development.

✔️ Secure your endpoints with validators.

✔️ Explore request's resources, their location and usage.

## Introduction

In our modern world, **everything** is a story of [server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server).

If you want to share a resource on the internet you will need a server. You
want to save your picture into a cloud? Same. You want to access PoC's ✨ amazing ✨
subject for this day? Everything is on GitHub and by extension, on their servers.

They have many usages and everyone uses it daily. One of the most common is resource sharing.
 With server and a protocol, you can share resources between applications or clients.

Those kinds of applications are called [API](https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces),
it's an interface exposed to let your application share resources with other applications
or consumers. For example, you can ask for the weather through a [weather API](https://www.weatherapi.com).

To communicate, APIs usually follow the [HTTP protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)
and standard. The most popular is [REST](https://en.wikipedia.org/wiki/Representational_state_transfer).

Here's a simple schema of an API and a client:

![server client relation](../../../.github/assets/software_api_client_server.png)

This subject will give you all the knowledge required to create a secure REST API.

## Step 0 - Setup

Still in your repository, create a new directory for the `day03`:
```shell
mkdir -p day03
```

- Initialize a Go module `SoftwareGoDay3`.

> See [day01](../../day01/Golang) if you don't remember how to initialize a Go module 😉

# Step 1 - Hello Web

Let's begin with a simple `hello world`. In fact, it will be more complex
than a simple hello world function called from a main, but it's not that hard 🙂

First, we must create a server using the [Gin](https://github.com/gin-gonic/gin)
package. It's the most popular framework to create server in Go.
> ***Please take a moment to read the documentation.***\
> Here is the [quickstart](https://github.com/gin-gonic/gin#quick-start) to help you.

When your `server` is correctly initialized, launch it to listen on port `8080`.

> We encourage you to show a message that displays your server root
> endpoint to easily reach it.\
> For example: `server listening on http://localhost:8080/`

You must also define an endpoint `/hello` reachable through the `GET` [method](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).<br>
When hitting the endpoint, it must responds `world` with the status `200`.

To do so:
- Create a package `routes` with your Router and Controllers.
- Create a package `server` with:
  - A structure `Server` (storing your Gin Engine).
  - A function `NewServer()` that will instantiate a new Server.
- Create a main to launch your Server.

Here is an example to manage your routes:
```go
package router

import (
	"github.com/gin-gonic/gin"
)

func world(c *gin.Context) {
}

func ApplyRoutes(r *gin.Engine) {
  //r.HttpMethod(route, controller)
}
```

## Step 2 - Where is the data?

### Theory

In [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol),
data is stored in different parts of the request depending on the data type:

- [`body`](https://en.wikipedia.org/wiki/HTTP_message_body): message in the
request. Generally used to store structured data in a given format (`JSON`, `XML`, ...)
- [`query`](https://en.wikipedia.org/wiki/Query_string): a string that
extends the url to fill parameter of type `key/value`. Generally used to
give additional information about the request.<br>
For example: order of data to return, max number of entities etc... It's also
used for [SEO](https://en.wikipedia.org/wiki/Search_engine_optimization).
- [`url param`](https://doriantaylor.com/policy/http-url-path-parameter-syntax): a dynamic
string in the path. Generally used to select a resource directly from
the url. For example: `http://localhost:3000/cat/1` select the resource `cat` with
the id `1`.
- [`cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies): used to
store session (keep user logged in) or track user activity.
- [`header`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers): `key/value` pairs used for contextual information. You can specify the type of your request, proxy
information, give an API key, specify how the server should manage cache etc...

### Here we are

It's time to create your different endpoints 🚀

#### Query

Create the endpoint `/repeat-my-query`, it must define the following handler
for the `GET` method:

If there is a `message` in the [query](https://github.com/gin-gonic/gin#querystring-parameters),
return it with status `200`.<br>
If there is no message: return a status `400`.

#### Param

Create the endpoint `/repeat-my-param/:message`, it must define the following handler
for the method `GET`:

Take as [url parameter](https://github.com/gin-gonic/gin#parameters-in-path)
a `message` and return it with status `200`.

#### Body

Create the endpoint `/repeat-my-body`, it must define the following handler
for the `POST` method:

If there is a `message` in the [`body`](https://github.com/gin-gonic/gin#try-to-bind-body-into-different-structs)
of your request, return it with status `200`.<br>
If there is no message, return a status `400`.

#### Header

Create the endpoint `/repeat-my-header`, it must define the following handler
for the `GET` method:

If there is a [header](https://github.com/gin-gonic/gin#serving-data-from-reader)
`X-Message`, return it with status `200`.<br>
If there is no message: return a status `400`.

#### Cookie

Create the endpoint `/repeat-my-cookie`, it must define the following handler
for the `GET` method:

If there is a [cookie](https://github.com/gin-gonic/gin#set-and-get-a-cookie)
`message`, return it with status `200`.<br>
If there is no message: return a status `400`.

> You can use [Postman](https://www.postman.com) or [Insomnia](https://insomnia.rest) to test your HTTP endpoints 😉

> 💡 You should check [AbortWithStatus](https://pkg.go.dev/github.com/gin-gonic/gin#Context.AbortWithStatus).

## Step 3 - A scaling issue

### Theory

It's common to configure your web server when you are about to launch it.<br>
In this case, you can't just hardcode value in your code, you need another
way.

[Environment variables](https://en.wikipedia.org/wiki/Environment_variable) 
are the best way to configure a software behavior.
> You can check them by tipping `env` in your terminal 😉

Those variables are used when you deploy an application in production to
specify some parameters that will affect the global behavior of your app.
It can also be used to pass sensitive information, such as API Key, secrets...

It's essential to know how use it! In this step, we will try to dynamically
configure your `host` and `port` when running the server, and create a 
dynamic greeting message.

It's also important to think about your configuration from the beginning
of your application by putting any variable that should be configurable into
your environment.

### Installation

Let's install the package [dotenv](https://github.com/joho/godotenv) in order to automatically load environment variables from a file.

```shell
go get github.com/joho/godotenv
```

### Practice

Now you can create a file named `.env` that will `export` the following
environment variables:
- `SERVER_PORT`: `8080`
- `SERVER_HOST`: `localhost`
- `HELLO_MESSAGE`: `world`

Let's create a `config.go` file in the directory `server`.

> 💡 In order to keep a clean architecture, it's common to dedicate a file 
> to your API configuration.

In it, use the [envconfig](https://github.com/kelseyhightower/envconfig) package to create a structure storing your server's environment variables.

Update the needed files to use your environment variables.

> If your `.env` contains sensitive information, **do not push it**! A good
practice is to create a file `.env.example` that will define the
same environment variables but without value.

## Step 4 - HTTP status

REST APIs return data according to customer's desire, but in case he tries to
access data that he doesn't own, or which do not exist, the REST API will
not be able to do what he asked for.

When this happens, the REST API must explicitly send an error. To do so,
we can use [HTTP codes](https://medium.com/@sahelasumi/http-status-codes-31644d99fb1) to help the client understand what happened. Those codes are essentials and must be correctly set from your REST API.

For example, a response with status `404` means that the resource has not been
found in the server, `201` stands for resource creation and `200` is used
when everything went well.

Let's create an endpoint `/health` that will always return the status `200`.<br>
If that endpoint fails when you test it, you are sure that your server is not
working. That's call a health-check!

Even if status codes make sense of their own, you don't know the meaning of [every status
code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).
<br>
When the client receives the response status, it's his own responsibility to properly handle it. But it's important to explicit these status in your codebase.

To do so, we will use aliases instead of the raw number. This way it will be really easy to understand what we return in our response 😉

Now, replace all raw http status codes by the one s[exported](https://pkg.go.dev/net/http#pkg-constants) by the [http package](https://pkg.go.dev/net/http).

TODO: remove the step and talk about the given tests
## Step 5 - Testing time

Since [day01](../../day01/Golang), we asked you to create tests to verify
the behavior of your functions. API are not exception and there are also
tools to manage tests.

To do so, you can use [Postman](https://www.postman.com), it's a powerful 
GUI to make requests, tests suites and many other useful stuff like API 
mockup, documentation etc...

Install Postman and create a [Postman collection](https://learning.postman.com/docs/sending-requests/intro-to-collections/)
to tests every endpoint previously coded.<br>
After you create your request, you should be able to run a whole [test-suite](https://www.postman.com/use-cases/api-testing-automation/)
on your server.

You can also create an [environment](https://learning.postman.com/docs/sending-requests/managing-environments/)
to manage your configuration.

## Step 6 - Who use hard coded text?

It's important to transform the data sent to the client to make the API easier to use 😄<br>
With time, data took standard forms like `JSON` or `XML`. Here we will use
the most popular: [`JSON`](https://en.wikipedia.org/wiki/JSON).

Create an endpoint `/repeat-all-my-queries` with a handler on the `GET` method.

This handler must retrieve all the [query parameters](https://en.wikipedia.org/wiki/Query_string)
znd return an array of objects containing the `key` and the `value` of each
query parameter.

Here's the shape of the data to return:
```json
[
    {
        "key": "<key of the query>",
        "value": "<value of the query>"
    }
]
```

> As it returns an Object array, you have to create a `structure` 👀

## Step 7 - Some logic 🤯

In the previous step, you learned how to format data. We will increase a bit
the difficulty by manipulating it.

Create an endpoint `/are-these-palindromes` with a handler on `POST`.

This endpoint must take a JSON body containing an array of strings like the
one below:
```json
[
    "meow",
    "lol"
]
```

And it must return an array of objects containing the string and a boolean
set to `true` if the string is a [palindrome](https://en.wikipedia.org/wiki/Palindrome).

Here's an example:
```json
[
    {
        "input": "meow",
        "result": false
    },
    {
        "input": "lol",
        "result": true
    }
]
```

> 💡 You will need to call [string methods](https://pkg.go.dev/strings)
to correctly complete this exercise.

## Step 8 - Server's bodyguard
TODO: remove/reduce this and the next step
> This exercise is not useful, please go to the further step

It's important to know what kind of data is sent to your API. This will
help you to keep an API resilient and secured.

For example, if you send an empty body to the endpoint from step 7, you should
get an error. That kind of issue is not suitable in a production API.

To ensure API security, a system has been created: [`Middleware`](https://en.wikipedia.org/wiki/Middleware).

> 💡 Middleware can also be used for other purposes: logger, permissions management etc...

Here's a code snippet of a [middleware for an gin API](https://github.com/gin-gonic/gin#custom-middleware):

```go
func Logger() gin.HandlerFunc {
    return func(c *gin.Context) {
        // before request
        t := time.Now()

		// Set example variable
		c.Set("example", "12345")


		c.Next() // Next function to be executed

		// after request
		latency := time.Since(t)
		log.Print(latency)

		// access the status we are sending
		status := c.Writer.Status()
		log.Println(status)
	}
}
```

- Create a `middlewares` package, containing the `CheckPalindrome` function.
> Here's [how to validate body with gin](https://github.com/gin-gonic/gin#model-binding-and-validation).\
> If the body is invalid, return the right error code with an explicit error message.

- Apply this middleware to the `/are-these-palindromes` endpoint.
> Here's [how to use middlewares with gin](https://github.com/gin-gonic/gin#using-middleware).

## Step 9 - Time to clean up

At this point, you should have many endpoints in one file in your package `routes`:
- Some simply retrieve content in the request and return it.
- One analyze palindromes.
- One says a message.
- One checks health.

It's time to organize our endpoints into different files.

Create the file `routes/index.go` with the following content :
```go
package routes

import (
	"github.com/gin-gonic/gin"
)

func ApplyRoutes(r *gin.Engine) error {
	applyHealth(r)
	applyHello(r)
	applyRepeat(r)
	applyPalindrome(r)
	return nil
}
```

Then create these files: `routes/health.go`, `hello.go`, `palindrome.go`, `repeat.go`.

Now move your endpoints into the corresponding files and create the required functions.
> `ApplyRoutes` should be the only exported function.

You should end up with the following architecture:
```
...
routes/
  health.go
  hello.go
  index.go
  palindrome.go
  repeat.go
...
```

## Bonus

Well done for completing this day 🔥

If you are still looking for exercises, here are two intermediate ones:

### Testing time, round 2
TODO: replace with advanced tests based on the provided ones

Postman is a powerful tool, but it's an external tool... you need a team
who knows the tool and everything relate to it. As well, it's hard to
create complex pipelines with Postman, scripts work good, but it does not
feel natural compared to code.

Here is [how to write a tests suite](https://kpat.io/2019/06/testing-with-gin/) for each endpoint to verify that it correctly handles errors and works well.

### Expose Data

Yesterday you discovered how to manipulate a database with Ent. Today, you've build an API with Gin.

What about mixing it?

Expose yesterday's database with today's API 🚀

> Made with ❤️ by PoC
