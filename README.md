# p_3_smoothie

View here:[here] [Smoothie Share](https://p3smoothie-bf6a9d7a1c89.herokuapp.com/)

## Description

Smoothie Share is a web app where users can create, share, and find smoothie recipes. It is user friendly, easy navigation means users can easily sign up or login. When logged in users can add new smoothies They can edit and delete their own existing smoothies recipes. 

## Project requirments

The project requirements are to create and deploy a full-stack web application using Django. Users must be able to log in and perfum CRUD operations, Create, Read, Update and Delete. The site should be user friendly and responsive. It must be deployed on Heroku.

## Accessing the App

* Username:
* Password:

## User stories

## Features

* User Authentication: Users can sign up, log in, and log out.
* CRUD Operations: Users can create, view, edit and delete their smoothie reciepes.
* Smoothie List: View a list of all smoothies shared by other users.
* Only users who created the smoothie recipe has access to edit and delete it.

## Future Features

* A profile page for users.
* Users can add images of their smoothie recipes.
* Users can save other users smoothie recipes to their profile page.
* Users can rate and comment on other users smoothie recipes.
  
## Design

### Colour scheme

### Typography

### Wireframe

## Technologies used

## Tools used

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
