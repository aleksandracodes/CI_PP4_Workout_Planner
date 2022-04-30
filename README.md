# Workout Planner

**Developer: Aleksandra Haniok**

💻 [Visit live website](https://xyz.herokuapp.com/)

![Mockup image](docs/screenshot-home.JPG)

## About



## Table of Contents
  - [About](#about)
  - [Table of Contents](#table-of-contents)
    - [About](#about-1)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
        - [Back to top](#back-to-top)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
        - [Back to top](#back-to-top-1)
  - [Design](#design)
    - [Colour](#colour)
    - [Fonts](#fonts)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries & Tools](#frameworks-libraries--tools)
        - [Back to top](#back-to-top-2)
  - [Features](#features)
        - [Back to top](#back-to-top-3)
  - [Validation](#validation)
        - [Back to top](#back-to-top-4)
  - [Testing user stories](#testing-user-stories)
        - [Back to top](#back-to-top-5)
  - [Bugs](#bugs)
        - [Back to top](#back-to-top-6)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
        - [Back to top](#back-to-top-7)
  - [Credits](#credits)
    - [Images](#images)
    - [Code](#code)
        - [Back to top](#back-to-top-8)
  - [Acknowledgements](#acknowledgements)

### About

The Workout Planner is an application for creating weekly training rota which also gives users ideas of exercises for their next training session.

### User Goals

- Be able to plan their workouts
- Be able to amend their plan at any point
- View the plan at any time

### Site Owner Goals

- Provide an online solution for users to plan their weekly workouts
- Create visually appealing design
- Provide fully responsive application with straightforward navigation


## User Experience

### Target Audience
- People who want to be more organised with their workouts
- Gym enthusiasts who focus on training different body parts and want to plan their weekly schedule to potentially avoid repetitions in their training
- People who want to keep track of their workout/fitness routine
- People who don’t want to think back and remember which day of the week they trained a specific part of the body

### User Requirements and Expectations

- Straightforward navigation
- Easy to use
- A responsive application that allows the user to access their plan on any devise
- Visually appealing design for all screen size
- Links and functions that work as expected
- An easy way to contact the developer
- Accessibility

##### Back to [top](#table-of-contents)


## User Stories

### Users

1.	I want to see the home page with explanation of the app
2.	I want to be able to easily navigate around the application to different pages
3.	I want to create my account to be able to plan my workouts
4.	I want to prepare a plan for multiple weeks in advance
5.	I want to be able to edit my current plans at any point
6.	I want to delete my plan if no longer needed
7.	I want to see feedback messages so that I know that my plan was created, edited or deleted
8.	I want to be able to view previous plans to help me prepare the following week’s workout
9.	I want to find inspiration for my workouts and be able to use search option to find a particular exercise
10.	As a returning user, I want to log in to the app to see my current plans

### Site Owner
11.	I want every site visitor to be able to view the catalogue of exercises
12.	I want only the logged-in users to be able to create their plans
13.	I want users to be able to create the plan on any day that suits their needs
14.	I want data entry to be validated on sign-up page
15.	I want the user to come to a 404 error page instead of having to use the browser back button if they enter a URL that does not exist
16.	I want user to be able to contact me and provide their feedback
17.	I want user to receive feedback if their message in contact form has been sent.
18.	I want my site to be fully responsive


##### Back to [top](#table-of-contents)


## Design

### Colours

The colour scheme was chosen to provide simple, neutral and fresh look. It was an intention to keep the website for all range of users and avoid colour stereotype typically found in the gyms and sports centres such as bright green or blue.

These colours were used throughout all the pages in such a way as to ensure adequate contrast and good user experience.

The pallet created using [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>
<img src="docs/Color-pallet-PP4.png">
</details>

### Fonts

Google Fonts were implemented on the website. Roboto with sans-serif as fallback was used thoughout the site to present the content in a clear and legible way.

### Structure

Simplicity, clarity and ease of navigation between pages were the key aspects for design of this website's structure.

At the top of the page there is a recognisable type of navigation bar with website name on the left side and the navigation links to the right which collapses to hamburger icon on smaller screen sizes. At the bottom of the page there is a footer with links to a contact page and developer's social media (opening in a separate tab/window).

- The website consists of the following sections:
  - Home page with an overview of the content and aim of the website.
  - Planner page where a not logged-in user can see an example of the workout plan and choose to log in or register. Registered user can either view their workout plans or create a new one.
  - Choose date screen where user can select the start date of their workout plan.
  - Add plan page allowing user to create a plan.
  - View plans page where user can see all their plans.
  - Edit plan page where user can edit an existing plan.
  - Delete plan allowing user to delete selected plan.
  - Exercises list page with catalogue of exercises and a filter option to find a specific exercise.
  - Exercise detail page where user can see a description of a chosen exercise.
  - Login page for returning user to log in.
  - Register page allowing a new user to sign up.
  - Profile page where user can view details of their account and created plans and also delete their account.
  - Logout page allowing user to log out of the website.
  - Contact page with contact form which allows users to send an email to the developer and provide their feedback.
  - 404 error page.


### Wireframes

<details><summary>Big screens - laptop & desktop</summary>
<img src="docs/wireframes/wireframes-desktop.png">
</details>
<details><summary>Medium screens - tablet</summary>
<img src="docs/wireframes/wireframes-tablet.png">
</details>
<details><summary>Small screens - mobile</summary>
<img src="docs/wireframes/wireframes-mobile.png">
</details>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python 3.10.2
- Django 3.2


### Libraries & Tools

- [Balsamiq](https://balsamiq.com/) to create the projects wireframes
- [Bootstrap v5.1.3](https://getbootstrap.com/). This project uses the Bootstrap library for UI components (Buttons, Card, Footer, Modal, Pagination, Navbar)
- [Cloudinary](https://cloudinary.com/) to store static files
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Font Awesome](https://fontawesome.com/) - Icons from Font Awesome were used throughout the site
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login) was used to deploy the project into live environment
- [jQuery](https://jquery.com) was used for drop-down exercises filters on smaller screens
- [Postgres](https://www.postgresql.org/) – deployed project on Heroku uses a Postres database
- [Remove.bg](https://www.remove.bg/) was used to remove background on home page images & 404 page image
- [Summernote](https://summernote.org/) - editor used for exercise description field in Admin page
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/) - code editor used to write this project

##### Back to [top](#table-of-contents)


## Features

##### Back to [top](#table-of-contents)

## Validation

The W3C Markup Validation Service was used to validate the HTML of the website.
<details><summary>Home</summary>
<img src="docs/validation/validation-html-index.html.JPG">
</details>

<details><summary>Planner</summary>
<img src="docs/validation/validation-html-planner.html.JPG">
</details>

<details><summary>Choose date</summary>
<img src="docs/validation/validation-html-choose-date.html.JPG">
</details>

<details><summary>Add Plan</summary>
<img src="docs/validation/validation-html-add-plan.html.JPG">
</details>

<details><summary>Edit Plan</summary>
<img src="docs/validation/validation-html-edit-plan.html.JPG">
</details>

<details><summary>View Plans</summary>
<img src="docs/validation/validation-html-view-plans.html.JPG">
</details>

<details><summary>Exercises list page</summary>
<img src="docs/validation/validation-html-exercises-list.html.JPG">
</details>

<details><summary>Exercise detail page</summary>
<img src="docs/validation/validation-html-exercise.html.JPG">
</details>

<details><summary>Login</summary>
<img src="docs/validation/validation-html-login.html.JPG">
</details>

<details><summary>Signup</summary>
<img src="docs/validation/validation-html-signup.html.JPG">
</details>

<details><summary>Profile</summary>
<img src="docs/validation/validation-html-profile.html.JPG">
</details>

<details><summary>Logout</summary>
<img src="docs/validation/validation-html-logout.html.JPG">
</details>

<details><summary>Contact form page</summary>
<img src="docs/validation/validation-html-contact.html.JPG">
</details>

<details><summary>Error Pages (400, 403, 404, 500)</summary>
<img src="docs/validation/validation-html-error-pages.html.JPG">
</details>

### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website. When validating all website, it passes with no errors.

<details><summary>Style.css</summary>
<img src="docs/validation/validation-css.JPG">
</details>

### JavaScript Validation
JSHint JS Validation Service was used to validate the Javascript files. No errors were found.

<details><summary>Script.js</summary>
<img src="docs/validation/validation-script.js.JPG">
</details>

### PEP8 Validation


##### Back to [top](#table-of-contents)


## Testing user stories

##### Back to [top](#table-of-contents)


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |

##### Back to [top](#table-of-contents)

## Deployment

### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name (this project is named "ci-pp3-connect4") and choose your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars store any sensitive data you saved in .json file. Name 'Key' field, copy the .json file and paste it to 'Value' field. Also add a key 'PORT' and value '8000'.
6. Add required buildpacks (further dependencies). For this project, I set up 'Python' and 'node.js' in that order.
7. Go to "Deploy" and select "GitHub" in "Deployment method"
8. To link up our Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
9.  Choose the branch you want to buid your app from
10. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
11. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

##### Back to [top](#table-of-contents)

## Credits

### Images

### Code

##### Back to [top](#table-of-contents)

## Acknowledgements

