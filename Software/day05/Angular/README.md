# PoC Software Pool 2023 - Day 05 - Angular 

## Introduction

✔️ Angular is an open-source JavaScript-based web application development framework developed and maintained by Google. 

It is used to create dynamic web applications using reusable components. By getting interested in Angular, you will learn to create dynamic web applications, handle real-time data, and use directives, services and templates to structure your code. 

You will also be able to use tools such as Typescript and RxJS to improve the quality of your code and make error management easier. In short, Angular will allow you to develop modern and performant web applications 😄

## Step 0 - Setup

Please refer to the [SETUP.md](./SETUP.md) file.

## Step 1 - Your very first component in Angular 💯

### 📑 **Description**
The goal of this task is to create your first component and display it with a great style using libraries or [SCSS](https://blog.logrocket.com/the-definitive-guide-to-scss/).

#### Explanation
By using components, you can make your application more modular, reusable, and easier to maintain. By breaking your application into smaller, more focused components, you can better organize your code and make it more manageable 😉

Components also allow for better code reuse, by allowing you to build reusable components that can be used across different parts of your application. This can help to speed up development time, reduce the amount of code you need to write, and make your application more maintainable 🔥

### 📌 **Tasks**

Let's create your first component using the following command:
``` sh
ng generate c my-first-comp
```

This will create a folder named `my-first-comp`, and as you can see in the screenshot below you will found 4 files inside it:
![First component output](/.github/assets/software/angular/first-component.png)

- `.component.ts` - This file contains the TypeScript class for the component, including properties and methods. It also includes any imports and decorators needed for the component to function properly.

- `.component.html` - The template for the component, written in HTML. It defines the structure and layout of the component.

- `.component.scss` - Includes the styles for the component, written in CSS. It defines the look and feeling of the component.

- `.component.spec.ts` - This file contains the unit tests for the component, written in Typescript. It tests the functionality of the component to ensure it works as expected.

Once your component is created, you have to add styles on it with libraries.

Go to the `.html` and add UI elements to it to create a [navbar](https://en.wikipedia.org/wiki/Navigation_bar).

Once this is done call the component in the right file to display it!

> This first step is intentationnaly complicated to let you discover Angular, but don't hesitate to ask for help 😉


### 📚 **Documentation**

- [Start with Angular](https://angular.io/start)
- [PrimeNG, an Angular component library](https://www.primefaces.org/primeng/)
- [MaterialUI, the Material design components for Angular](https://material.angular.io/)

### ✔️ **Validation**:

You have now a beautiful navbar!\
It's only styles for the moment, but we will add functionnality soon 😄


## Step 2 - Binding data 🔖

### 📑 **Description**

Data-binding allow you to make your application more dynamic and responsive to user interactions. 

For example, you can use data binding to display data from your component class in the template, or to update the component's class properties when the user interacts with the template. This can help to make your application more interactive and user-friendly 👨

The purpose of this task is to pass data from the HTML interface to your Typescript for interactive actions.

### 📌 **Tasks**

Create another component:
``` sh
ng generate c data-binding
```

Now you have to modify two files: `data-binding.html` and `data-binding.ts` to add 
an input and try to get the data in your `.ts` file. 

> If you aren't using custom style libraries and only CSS you will also have to modify `data-binding.scss` 😉

The documentation bellow will help you to do so 😄

### 📚 **Documentation**
- [Data binding in Angular](https://www.tektutorialshub.com/angular/ngmodel-two-way-data-binding-in-angular/)


### ✔️ **Validation**

You can now pass data from the HTML interface to the corresponding TS file 🥳\
It's a good start to create amazing things that you will discover soon!


## Step 3 - Forms ℹ️

### 📑 **Description**

Angular forms allow you to create complex forms with validation, and can be used to handle user input and data submission.

By using Angular forms, you can create forms that are more dynamic and responsive to user interactions. For example, you can use Angular forms to validate user input and provide feedback to the user, or to update the component's class properties when the user submits the form.

The goal of this task is to manage forms input, for multiple usage like a register or login page.


### 📌 **Tasks**

- Create a form in a component with multiple input and store the data in the right way (remember the last step 😉)
    - You have multiple way to do it in Angular, check the documentation and do it in a proper way
    - You can create a model in Typescript to handle the object created by your forms and pass it easily

### 📚 **Documentation**:

- [Forms](https://angular.io/guide/forms-overview)

### ✔️ **Validation**:

You have now a forms that handle multiple inputs and you created a model in Typescript so when someone gives an answer to the form an object of a model is generated and logged 🎉

## Step 4 - Angular Router 🔀

### 📑 **Description**

The Angular router is powerful because it allows for dynamic routing, lazy loading, handling of route parameters, navigation, and route protection.\
It enables developers to create responsive and efficient applications that adapt to different types of URLs and requests without the need for extensive custom code.

The goal of this task is to add the ability to navigate in your app using the Router and create several pages, for instance we will implement the login and register pages here.


### 📌 **Tasks**:

- Create a `login` component
    - Add styles on it make it beautiful 😝
- Create a `register` component
    - Add styles on it make it beautiful 😝
- Create your first router and add endpoints for the `register` and `login` components
    - Check the documentation to discover how router works and how to call it in your app. Things can be hard to understand at first, but we are are to help 😄
  
If you ran the right command, you should have a `app-routing.module.ts` file in which you can add this:
```ts
const routes: Routes = [] // all your endpoints will be stored in this array, check the documentation and how to add more.
```

which should give the following hierarchy:
![Router](/.github/assets/software/angular/router.png)


### 📚 **Documentation**

- [Angular Router](https://angular.io/guide/router)

### ✔️ **Validation**:

You have now a great app with a login and register page that you can browse easily,
the code is clean and the UI is beautiful 🥳

## Step 5 - Angular Services with backend interaction 💻

### 📑 **Description**:
Angular services are powerful because they allow for separation of concerns and code reusability. They are classes that can be used to share data and logic across multiple components in an Angular application. \
Services can also be used to handle complex logic that shouldn't be included in a component, such as calling an API.

By using services, you can make your application more modular and maintainable. You can encapsulate complex logic and data in a service, which can then be easily reused across multiple components. This can help to reduce the amount of code you need to write and make your application more maintainable.

Services also allows for better separation of concerns by allowing you to separate the logic of your component class from the layout of your template. This makes it easier to understand how different parts of your application are working and makes it easier to make changes to your application without affecting other parts of the application.

### 📌 **Tasks**:

Let's create your first service in Angular 🔥

You can start with this command to generate some basic files:
```sh
ng g service service/my-first-service
```

Now it's time to call the [API](../resources/README.md) and interact with real data 🚀
> Please take a moment to setup this.\
> Feel free to play with it with a tool like [Postman](https://www.postman.com/).

Let's call the API when a user registers 🧔‍♂️

- Create a service that will handle the communication with the backend
    - You'll need to create a model for the user and other data 😉
    - Take a look to the API documentation of the backend
- Implement a user registration using the backend
- Implement a user login using the backend

### 📚 **Documentation**:

- [Injectable Angular Services](https://angular.io/guide/creating-injectable-service)

### ✔️ **Validation**:

You now have an app with working login and register pages, congratulation 🎉

## Step 6 - Testing time 🧪

### 📑 **Description**:

The goal of this task is to test your component and why not your service.\ 
Testing your code is an important thing in the workflow of a developer, don't underestimate it 😉

Tests files ending by `.spec.ts` are automatically created by the CLI with your components and services 🧪

### 📌 **Tasks**:

Add tests in the files created by the CLI for the login and the register components.
Test that your UI elements correspond to what you expect (number of inputs, their type, number of buttons...)

The syntax is pretty straight-forward and you shouldn't have any problem by following the documentation, but don't hesitate to ask the staff for help 😄

### 📚 **Documentation**:
- [Testing in Angular](https://angular.io/guide/testing)
- [Testing Services](https://angular.io/guide/testing-services)

### ✔️ **Validation**:

You learned how to test your components, it's a huge leap towards an efficient and maintainable application 💯


## Step 7 - Dashboard 🖌️

### 📑 **Description**:

Let's summarize everything you've learned by creating a complete dashboard to manage artists 🚀

### 📌 **Tasks**:
- Create a dashboard page accessible to logged-in users
  - It should contain a button that opens a modal to add an artist, and artist cards will be displayed in the dashboard
- Create another service that will handle the management of artists
- Add protection on your endpoints
    - For example, a non-logged in user can't create an artist 😉

### 📚 **Documentation**:

No more documentation, you should have everything you need now 😄

### ✔️ **Validation**:

You can manage artists in your dashboard, you need to be login and register for access the dashboard

## Conclusion

Well done! You've accomplished a lot with Angular, and there is so much more to discover 😄
Refer to the [official documentation](https://link.com) to deep-dive into it. 

Hope you enjoyed the day!

<h2 align=center>
Organization
</h2>
<br/>
<p align='center'>
    <a href="https://www.linkedin.com/company/pocinnovation/mycompany/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
    </a>
    <a href="https://www.instagram.com/pocinnovation/">
        <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
    </a>
    <a href="https://twitter.com/PoCInnovation">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
    </a>
    <a href="https://discord.com/invite/Yqq2ADGDS7">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white">
    </a>
</p>
<p align=center>
    <a href="https://www.poc-innovation.fr/">
        <img src="https://img.shields.io/badge/WebSite-1a2b6d?style=for-the-badge&logo=GitHub Sponsors&logoColor=white">
    </a>
</p>

> 🚀 Follow us on our different social networks, and put a star 🌟 on `PoC's` repositories.