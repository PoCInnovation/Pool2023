# PoC Software Pool 2023 - Day 03 - REST API

**Day purposes**

✔️ Discover the basics of the NestJS framework.

✔️ Learn the concept of reverse control.

✔️ Learn the advanced concepts in the backend development (serialization, constraint validation...).

✔️ Learn how to create an authentication system.

## Introduction 📻

Pshhh ! Pshhh ! (sound of talkie walkie)

*You pick up the walkie-talkie*

Hello soldier! As I can see, you choose the royal way today. This is great because I need you.

We need to build a new war robot, it's name is "the destroyer 300".

## Step 0 - Setup the robot 🔧

To create our robot, it's mandatory to setup our tools. Go to the [SETUP.md](./SETUP.md) file and follow the steps.

## Step 1 - Hello world 👋

First of all, we need to restructure and start the app. 

To do that, you need to create a new **module app**. In the **src/app** folder.

The **principal concept** used by Nest is the **inversion control**. This consists in **allowing the application** to **handle class injections**. The purpose of a module is both to **compartmentalize the application** in different functionalities, but also to **define that where are the classes that we need to inject in our module**.

I recommend you to use the **CLI** provided by **nest** with this command:
```shell
# command for creating a module
npx nest g module app
```

This module serve us to test if the app is running.

After creating a the new module you need to create a new controller in the `src/app/controller/app` folder.

*It's important to structure your files well in this type of application because there are often many files very quickly and it is important to browse it.*

you can use the command:
```shell
# command for creating a controller
npx nest g controller ./app/controller/app
```

In this controller create one route **GET /app** to display a hello world:
you can use the command:
```shell
# command for creating a service
npx nest g service ./app/service/app
```

To display a hello a world, create a new **service** in the `src/app/service/app` folder with a method **helloWorld** that return the string `hello world!`

Inject this service in your controller and return the result of the method helloWorld.

After that, install the **SwaggerUi package** and create **a tag** for **the controller**.

**Swagger ui** is a library that allows you to **generate documentation** of your **API** automatically **throughout your development**.

### Technical documentation 📝:
- [NestJS modules](https://docs.nestjs.com/modules)
- [NestJS controllers](https://docs.nestjs.com/controllers)
- [NestJS services](https://docs.nestjs.com/providers)
- [Inversion of control](https://www.theserverside.com/definition/inversion-of-control-IoC#:~:text=Inversion%20of%20control%20is%20a,different%20part%20of%20the%20application.)
- [NestJS swagger UI](https://docs.nestjs.com/openapi/introduction)

## Step 2 - Repeat info 🦜

Now begin the warm-up ! In this step yo need to learn how to use NestJS and how to get all the information that you need.


Here are the steps to follow:
- Create a **new module repeat-info**
- Create a **new controller repeat-info**
- Create a **route GET 'repeat-info/repeat-my-query'** that **repeat query params**
- Create a **route GET 'repeat-info/repeat-my-param/:myParam'** that **repeat param**
- Create a **route POST 'repeat-info/repeat-my-body'** that **repeat the body**
- Create a route **GET 'repeat-info/repeat-my-header'** that **repeat the headers**


### Important ⚠️

Because you are in **Typesscript** you need to **type all the information** that you **receive in your app**. For the body, create a dto/repeat-info folder in your module and create a `repeat-info-dto.ts` file. In this file create a RepeatMyBodyDto class with a message property in readonly (type string).

### Technical documentation 📝:

- [NestJS request object](https://docs.nestjs.com/controllers#request-object)
- [Documentation about dto](https://medium.com/@jonathan.tjendana/just-give-me-what-i-want-bdad1f1d0c6)


## Step 3 - Soldier 🪖

Can't handle no more ? ah ah ah it's just the beginning! 

In this this step we will create a soldier module. Th goal of this module is to allow you te create, update, get and delete a soldier. For security the robot this information to allow you to using it.

Here are the steps to follow:
-  Create a **new module soldier** 
-  Create a **new service soldier** 
-  Create five method: **create, update, get, getAll, delete.**
-  Use the **prismaService service** to **interact** with **the database**
-  Create routes **to interact** with your **service's methods**

### Important ⚠️

You need to **create one type of dto per request that requires a body**. For example if you want to create, and update a weapon in a module you need to create one **CreateWeaponDto** and one **UpdateWeaponDto** (with nullable properties because we not need to update all info all times).

*If you don't know the information to set in your dto, check the prisma.module file*

### Technical documentation 📝:
- [Prisma documentation](https://www.prisma.io/docs/concepts/components/prisma-client)
- [NestJS services](https://docs.nestjs.com/providers)


## Step 4 - Data validation 👮

Nice, it works! However there are things missing. We need to be sure of the information that we receive in our robot.

Here are the steps to follow:
- Setup the **class-validator** library
- Use decorator to check if: **soldierSecret, firstName, lastName** are **strings** and **grade** is a **GradeType enum**. You need to do this for all dto that you need for your body.

### Technical documentation 📝:
- [NestJS class validator](https://docs.nestjs.com/pipes#class-validator)


## Step 5 - Confidential information 🔒

Great! Now we can interact with a soldier model but we need to **be sure** of **the information** provided when **we interact** with **it**. 

We have one **last thing** to do for **this part** of the **robot**. **Keep sensitive information secret.**

Indeed, **the soldierSecret information must not leave the application**.
The **enemy should not be able** to **take control** of our **robot**. To do that we will use **serialization**.


Here are the steps to follow:
- Create a **SoldierCreatedDto** class
- Create a **SoldierUpdatedDto** class
- Create a **SoldierFoundDto** class
- Create a **SoldierDeletedDto** class
- Exclude the property **SoldierSecret**
- Declare a **partial constructor** on each class
- **Return the good dto** in **each service's method** and **each controller's method**
- Use the **ClassSerializerInterceptor** in the **main**


### Important ⚠️

If you wants to **exclude a variable** in a **dto** you need to **construct your object** with the keyword **new** and **to use the constructor**.

### Technical documentation 📝:
- [NestJS serialization](https://docs.nestjs.com/techniques/serialization)

## Step 6 - Identity check 🛂

Before create the robot module, we need to construct an auth system. To do this, we need use the **jwt passport module**. 

First of all I recommend you to **read the documentation** about it in the **nestjs documentation**

Here are the steps to follow:
- Create a **new auth module**
- Create a **new auth controller** with a route **POST '/auth/login' route**
- Create **a new jwtAuthService** with **two methods** one for **validate the soldier** with his **id** and one for **login the user with is id and soldierSecret**
- Create a **jwtStrategy** in a **folder /strategy/jwt** in the **auth module**. in its constructor **extract the token from bearer** and create a method that **validate a soldier** with a **jwt payload**. This method must call the **jwtAuthService validate method to validate the user**.


## Important ⚠️

You need to use the **bcrypt library** to hash the passport. This data is very sensitive it's therefore necessary to the **cipher** to avoid that the enemy can obtain it even if the database leak. If one day they get all the information from the databases, they will see only a hash and will not be able to get the real password.


### Technical documentation 📝:
- [NestJS authentication](https://docs.nestjs.com/security/authentication)
- [Passport JWT](https://docs.nestjs.com/security/authentication#implementing-passport-jwt)

## Step 7 - The destroyer 300 🤖

Youhou, it’s time to show who is the boss 😎

Let's create the robot and its weapon.

Here are the steps to follow:
- Create a **new robot module**
- Create a **new robot controller** with a **GET '/robot/fire' route**
- Create a **new robot service** with a **fire method** that **returns one of these strings randomly** (you can add your own if you wants): 'piou piou', 'tou tou tou', 'ratatatata', 'bang', 'pow'
- Create a **JwtAuthGuard** in the **auth module** in a **folder guard/jwt**
- **call the fire method** in the **robot controller** and **protect this route with the guard**

Congratulation 🎉 we can make a nice fireworks! 🥳
### Technical documentation 📝
- [NestJS guards](https://docs.nestjs.com/guards#guards)
- [Passport jwt protect routes](https://docs.nestjs.com/security/authentication#implement-protected-route-and-jwt-strategy-guards)

## Bonus - Unitary tests ✅

Now that the robot is up and running it's important to make sure that it will continue to work with future changes. A real soldier has to do a clean work! 

In this step you need to **unitary test all your app**.

In the **backend application** development there are **different types of tests**. In this bonus you will see the **unit test**, this type of test consists to test your functions isolated form their context.

### Technical documentation 📝:

- [NestJS unit testing](https://docs.nestjs.com/fundamentals/testing#unit-testing)