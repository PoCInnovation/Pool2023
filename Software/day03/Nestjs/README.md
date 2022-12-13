## Intoduction

Pshhh ! Pshhh ! (sound of talky walky)


Hello solider ! As I can see, you choose the royal way today. This is great because I need you.

We need to build the new war robot, it's name is "the destroyer 300"  


## Step 1 - Hello world

First of all, we need to start the app. 

To do so, you need to create a new module app. In the src/app folder

I recommend you to use the cli provided with nest with the command

```bash
# command for creating a module
npx nest g module app
```

This module serve us to test if the app is running.

After create a the new module you need to create a new controller in the folder 'src/app/controller/app'.

*It's important to structure your files well in this type of application because there are often many files very quickly and it is important to browse it.*

you can use the command:
```bash
# command for creating a controller
npx nest g controller ./app/controller/app
```

In this controller create one route GET '/app' to display a hello world

you can use the command:
```bash
# command for creating a service
npx nest g service ./app/service/app
```

To display a hello a world, create a new service in the folder 'src/app/service/app' with a methode helloWorld that return the string "hello world !"

inject this service in your controller and return the result of the method helloWorld.

After that, install the swaggerUi package and create a documentation of the controller. With ApiTags(app)

## Step 2 - Repeat info 

Now begin the warm-up ! In this step yo need to learn how to use nestjs and how to get all the informations that you need 

Here are the steps to follow:
- Create a new module repeat-info
- Create a new controller repeat-info
- Create a route GET 'repeat-info/repeat-my-query' that reapeat query params
- Create a route GET 'repeat-info/repeat-my-param/:myParam' that repeat param
- Create a route POST 'repeat-info/repeat-my-body' that reapeat the body
- Create a route GET 'repeat-info/repeat-my-header' that repeat the headers


### Important 

Because you are in typesScript you need to type all the informations that you receive in your app. For the body, create a dto/repeat-info folder in your module and create a repeat-info-dto.ts file. In this file create a RepeatMyBodyDto class with a message property in readonly (type string). If you wants more informations about dto, check this article: 


## Step 3 - Soldier 

Can't handle no more ? ah ah ah it's just the begining ! 

In this this step we will create a soldier module. Th goal of this module is to allow you te create, update, get and delete a soldier. For security the robot this informations to allow you to using it.

Here are the steps to follow:
-  Create a new module soldier 
-  Create a new service soldier 
-  Create five method: create, update, get, getAll, delete.
-  Use the prismaService service to interact with the database
-  Create routes to interact with your service's methodes

### Important

You need to create one type of dto per request. For example if you want to create, and update a weapon in a module you need to create one CreateWeaponDto and one UpdateWeaponDto (with nullable properties because we not need to update all info all times).


### Colonel Tips 

If you don't know how info to send in the soldier creation, check the prisma.module.file


## Step 4 - Data validation

Nice ! It's works ! However there are things missing. We need to be sure of the information that we receive in our.


In this step you need to setup the library class validator and set constraint validation on all property of our body dto.

## Step 5 - Confidential information

Great ! Now we can create a soldier and we are sure of the information we have to create it. 
We have one last thing to do for this part. Keep sensitive information secret  

Indeed, the soldierSecret must in no way leave the application.
The enemy should not be able to take control of our robot. To prepare for our end we will use serialization


Here are the steps to follow:
- create a SoldierCreatedDto class
- create a SoldierUpdatedDto class
- create a SoldierFoundDto class
- create a SoldierDeletedDto class
- exclude the property soldierSecret
- declare a partial contructor on each class
- return the good dto in each service's method and each controller's method
- use the ClassSerializerInterceptor in the main


### Important

If you wants to exclude a variable in a dto you need you need to go through its constructor to make it work.  

## Step 6 - Identity check

Before create the robot module, we need to construct an auth system. To do this, we need use the jwt passport module. 

First of all I reccomand you to read the documentation about it in the nestjs documentation

Here are the steps to follow:
- Create a new auth module
- Create a new auth controller with a Post '/auth/login' route
- Create a new jwtAuthService with two methods one for valitateSolider with his id and one for login the user with is id and soldierSecret
- Create a jwtStrategy in a folder /strategy/jwt/ in the auth module with. in its constructor extract the token from bearer and create a method that validate a soldier with a jwt payload. This method must call the jwtAuthService validate method to validate the user


## Important 

You need to use the bcrypt library to hash the passport. This data is very sensitive it is therefore necessary to the cipher to avoid that the enemy can obtain it even if the database leak.

## Step 7 - The destroyer 300
Youhou ! it’s time to show who is the boss ! Let's create the robot and its weapon

Here are the steps to follow:
- Create a new robot module
- Create a new robot controller with a GET '/robot/fire' route
- Create a new roboty service with a fire method that returns one of these strings randomly (you can add your own if you wants): 'piou piou', 'tou tou tou', 'ratatatata', 'bang', 'pow'
- Create a JwtAuthGuard in the auth module in a folder guard/jwt
- call the fire methode in the robot controller and protect this route


Tada !! We can make a nice fireworks !

## Bonus - unitary tests

Now that the robot is working it is important to make sure it will continue to work. A real soldier has to do clean work! Good thing the unit tests are here!

In this step you need to unitary test all your app 