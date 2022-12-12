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


