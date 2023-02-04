# Angular Setup


## CLI & Project initialization

Installing Angular is a straightforward process. First, you will need to make sure that you have the Angular CLI (Command Line Interface) installed on your computer. 

This can be done by running the following command in your terminal:
```sh
npm install -g @angular/cli
```

> This installation cam take a while, don't worry 😉

Once the CLI is installed, you can create a new project by running the command:
```sh
ng new my-project
```

where `my-project` is the name of your project. This command will create a new directory with the structure of an Angular project 🚀

Then, navigate to the newly created directory:
```sh
cd my-project
```

Your project is ready, now you have to choose a UI library 😄

## UI library

You have 2 choices: [PrimeNG](https://www.primefaces.org/primeng/setup) or [Angular Material](https://material.angular.io/components/categories).

> 💡 If you are motivated and skilled enough you can also use pure CSS, but using a library is highly recommended

PrimeNG is a collection of rich UI components for Angular, such as advanced datatables and charts. It is a commercial library that provides a wide range of feature-rich components for building robust and attractive user interfaces.

On the other hand, Angular Material is a library of reusable UI components for building Angular applications. It provides a consistent look and feel across all Angular applications and is an open-source library. It provides a wide range of components such as form controls, navigation, layout, and more. It is based on Material Design, which is a design system developed by Google.


Once you made your choice, follow the installation steps required for your library.

### Angular Material setup

Install the Angular Material package by running the command:
```sh
ng add @angular/material
```

This command will install the necessary packages and make the necessary modifications to your project, such as adding the required modules and styles to your application.

Now you can import the Angular Material modules in your `app.module.ts` file, by importing the modules from `@angular/material`.

Then you have to add the Material Design icons to your project. You can do this by adding the following line in the `index.html` file:
```html
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
```

Finally, you can start using Angular Material components in your application by adding them to your component's template and applying the appropriate styles.

By following these steps, you should have a working Angular project with Angular Material UI set up and ready to use, you can go back to the subject 🚀


### PrimeNG setup

Install the PrimeNG package by running the command:
```sh
npm install primeng --save
```

Now you can install the related `primeicons` package by running the command:
```
npm install primeicons --save
```

Once this is done, you have to import the CSS and JS files of PrimeNG and PrimeIcons in your `angular.json` file.

You will later need import the PrimeNG modules in your `app.module.ts` file, by importing them from: `primeng/{module}`

Finally, you can start using PrimeNG components in your application by adding them to your component's template and applying the appropriate styles.

By following these steps, you should have a working Angular project with PrimeNG set up and ready to use, you can go back to the subject 🚀