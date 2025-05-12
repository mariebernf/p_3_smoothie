# p_3_smoothie

## Description

## Project requirments

## User stories

## Design

### Colour scheme

### Typography

### Wireframe

## Technologies used

## Tools used

## Deployment

## Testing

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

**Solution:** *Was missing csrf settings. I added the heroku domain to the csrf trusted origins in settings.*

## Credits
