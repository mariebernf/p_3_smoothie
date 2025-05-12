# p_3_smoothie

View here:[Smoothie Share](https://p3smoothie-bf6a9d7a1c89.herokuapp.com/)

## Description

Smoothie Share is a web application where users can create, share, and find smoothie recipes. It is user friendly, easy navigation means users can easily sign up or login. When logged in users can add new smoothies  Users can only add, edit and delete their own recipes when logged in. They can not change other users recipes. Smoothie ingredients are shown for logged in users. Non-logged in users will see a prompt to log in. This will encourage people to sign up.

## Project requirments

The project requirements are to create and deploy a full-stack web application using Django. Users must be able to log in and perfum CRUD operations, Create, Read, Update and Delete. The site should be user friendly and responsive. It must be deployed on Heroku.

## Accessing the App

* Username:
* Password:

## User stories

* User story: As a user, I want to create an account easily so that I can access the website's features.
  
  Meets requirment: Signup form
  Users can create an account by filling out the sign up form, which is easy to find and fill out. When the form is submitted and validated, the user is logged in 
  and can view the smoothie recipes and add their own.

* User story: As a user, I want to be able to add my smoothie recipes so I can share with other users.
  
  Meets requirement: Smoothie creation form
  Users can add their own smoothie recipes through a form, which allows them to input the smoothie title, description, and ingredients.

* User story: As a user, I want to be able to edit my smoothie recipes.

  Meets requirment: Edit functionality
  Users can edit their own smoothie recipes. This is ensured by restricting the editing funciton to only the user who created the smoothie recipe.

* As a user, I want to able to delete my smoothie recipes.

  Meets requirment: Delete functionality
  Users can easily delete their own smoothie recipes. Users can only delete their own recipes.

## Features

* User Authentication: Users can sign up, log in, and log out.
* CRUD Operations: Users can create, view, edit and delete their smoothie reciepes.
* Smoothie List: View a list of all smoothies shared by other users.
* Only users who created the smoothie recipe has access to edit and delete it.
* Only logged in users can see smoothie ingredients, non users will see a prompt encouraging them to sign up.

## Future Features

* A profile page for users.
* Users can add images of their smoothie recipes.
* Users can save other users smoothie recipes to their profile page.
* Users can rate and comment on other users smoothie recipes.
* Apply better design to the smoothie application overall.
  
## Design

### Colour scheme

* Background colour: Light yellow (#FFFACD)
* Navbar and Footer colour: Light Navy Blue (#5D6D7E)
* Text colour: White (#FFFFFF) for headings, and black text in the body for readability.

The light yellow background colour, creats a warm feel for the user. The light navy blue navbar and footer offer a modern look. The overall design is minimalistic, focusing on functionality and ease of navigation.

### Typography

Primary Font: Montserrat from Google Fonts.
* Used for navigation, footer and general body text.
  
Fallback Font: sans-serif for Montserrat in case it doesn't load.

### Wireframe

## Technologies used

* Django: Backend web framwork.
* Python: Programming language
* HTML/CSS: Frontend design
* Bootstrap: Responsive layout and design
* Git: Version control
* Heroku: Deployment platform

## Tools used

* Github: Platform for hosting code reposistories.
* Django Admin: Manage content on your app.
* Chrome DevTools: Used to inspect elemnts, debug and troubleshoot.
* Google fonts: For customizing fonts.
* VSCode: Used to write and manage code.

## Deployment

## Testing

I have done the following tests: ( tests.py )

**Smoothie Creation Test:** Verifies that the smoothies are created properly, and the title and author are assigned.

**Smoothie List View Test:** Ensures that smoothie liste page returns a 200 status code and displays the correct smoothie title.

## Bugs and Fixes

**Issue:** *Name Error: name 'include' was not defined.*

**Solution:** *Added 'include' to the top of main urls file.*

---

**Issue:** *TemplateSyntaxError.*

**Solution:** *Was missing a closing quote, fixed in the base.html file.*

---

**Issue:** *The navbar was positioned incorrectly (to the side), and the footer was also incorrectly positioned.*

**Solution:** *The issue was fixed by updating the base html structure, using boothstrap's grid and utility classes.*

---

**Issue:** *After deploying to heroku, the application would not load.*

**Solution:** *Several changes were made to try to solve this:*
1. Used heroku logs --tail to check logs and identify the issues.
2.  Fixed Procfile. I had initially named it procfile(lowercase) which caused problems.
3.  Updated allowed hosts in settings.
4.  I manually entered secret key to heroku's environment variables.
5.  Addressed various issues relating to incorrect paths in urls and settings that were discovered during the troubleshooting process.
6.  Triggered a rebuild so heroku would regognize the changed Procfile name, this worked to set up the application correctly.

---

**Issue:** *CSRF verification failed error.*

**Solution:** *Was missing csrf settings. I added the heroku domain to the csrf trusted origins in settings

## Credits
