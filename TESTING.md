# The Bike Shop

## Code Institute - Milestone Project 4 (Testing)

![Image template](readme/testing/responsive-homepage-testing.png)

<a href="https://the-bike-shop-project.herokuapp.com/" target="_blank">Click here to view The Bike Shop live</a>

## Table of contents

1. [Automated Testing](#automated-testing)
    * Book App
        - TBC
    * Cart App
        - TBC
    * Checkout App
        - TBC
    * Complete App
        - TBC
    * Home App
        - TBC
    * Products App
        - TBC
    * Profiles App
        - TBC
    * Services App
        - TBC
1. [Manual Testing](#manual-testing)
    * [Screen sizes](#screen-sizes)
        - [Mobile screens](#mobile-screens)
        - [Tablet screens](#tablet-screens)
        - [Desktop screens](#desktop-screens)
    * [Navigation bar menu](#navigation-bar-menu)
        - [Hamburger navigation bar](#hamburger-navigation-bar)
        - [Full screen navigation bar](#full-screen-navigation-bar)
    * [User Stories Complete](#user-stories-complete)
    * [W3C Markup Validation Service](#w3c-markup-validation-service)
        - [HTML templates](#html-templates)
    * [W3C CSS Validation Service](#w3c-css-calidation-service)
        - [Base](#base)
        - [Checkout](#checkout)
        - [Profile](#profile)
    * [JS Hint Javascript code validator](#js-hint-javascript-code-validator) 
        - [JS Files](#js-files)
        - [Scripts](#scripts)
    * [PEP8 online validator](#pep8-online-validator)
        - [Book App](#book-app)
        - [Cart App](#cart-app)
        - [Checkout App](#checkout-app)
        - [Complete App](#complete-app)
        - [Home App](#home-app)
        - [Products App](#products-app)
        - [Profiles App](#profiles-app)
        - [Services App](#services-app)
        - [The Bike Shop App](#The-bike-shop-app)
        - [Project Level](#project-level)
    * Web Browsers
        - Google Chrome
        - Apple Safari
        - Microsoft Edge
        - Mozilla Firefox
    * Testing responsiveness
        - Mobile screenshots
        - Tablet screenshots
        - Desktop screenshots
    * Lighthouse testing
        - Desktop results
        - Mobile results
    * Issues fixed
        - TBC
    * Further testing
        - 

Return to my [README Doc](README.md) 


## Automated Testing
Automated Unit Testing was done using Django’s testing tools by importing the inbuild TestCase class from Django.

### Django Testing


## Screen sizes

### Mobile screens
![Image template](readme/testing/mobile-screens.png)

### Tablet screens
![Image template](readme/testing/tablet-screens.png)

### Deskop screens
![Image template](readme/testing/desktop-screens.png)


## Navigation bar menu

### Hamburger navigation bar
![Image template](readme/testing/hamburger-menu.png)
### Full screen navigation bar
![Image template](readme/testing/desktop-menu.png)


## User Stories Complete

Click this link to see all <a href="https://github.com/liamwalsh1980/Milestone-Project-4/blob/main/readme/pdf/user_stories_complete.pdf" target="_blank">User Stories</a> completed. 

## W3C Markup Validation Service

I used <a href="https://validator.w3.org/" target="_blank"> W3 validator</a> to check the html templates for this project. All Errors found were based on rendering added and the base template holding the boilerplate. 

Errors found: -
- Non-space characters found without seeing a doctype first. Expected DOCTYPE html.
- Element head is missing a required instance of child element title.
- Stray doctype. Stray start tag html
- Cannot recover after last error. Any further errors will be ignored.
- Consider adding a lang attribute to the html start tag to declare the language of this document.
- Bad value {% url [URL NAME] %} for attribute action on element form: Illegal character in path segment: { is not allowed.
- Bad value {% url [URL NAME] %} for attribute href on element a: Illegal character in path segment: { is not allowed.
- Bad value {{ MEDIA_URL }}noimage.jpg for attribute src on element img: Illegal character in path segment: { is not allowed.
- Misplaced non-space characters inside a table. {% for order in orders %}
- Misplaced non-space characters inside a table. {% for item in cart_items %}

## W3C CSS Validation Service

I used <a href="https://jigsaw.w3.org/css-validator/" target="_blank">W3C jigsaw validator</a> to check the 3 CSS files used for this project. Results below show that there are no erros. 

### Base
![Image template](readme/testing/base.css-checked.png)

### Checkout
![Image template](readme/testing/checkout.css-checked.png)

### Profile
![Image template](readme/testing/profile.css-checked.png)

## JS Hint Javascript code validator

### JS files


I used <a href="https://jshint.com/" target="_blank">JS Hint</a> to check the Javascript files in this project. The following files were checked with no errors founds: -

- checkout app - <a href="https://github.com/liamwalsh1980/Milestone-Project-4/blob/main/checkout/static/checkout/js/stripe_elements.js" target="_blank">stripe.element.js</a>

- profile app - <a href="https://github.com/liamwalsh1980/Milestone-Project-4/blob/main/profiles/static/profiles/js/countryfield.js" target="_blank">countryfield.js</a>

### Scripts

Scripts added within HTML files

- cart app > cart.html - <a href="https://github.com/liamwalsh1980/Milestone-Project-4/blob/main/cart/templates/cart/cart.html" target="_blank">script</a>

- products app > add_product.html - <a href="https://github.com/liamwalsh1980/Milestone-Project-4/blob/main/products/templates/products/add_product.html" target="_blank">script</a>

- products app > edit_product.html - <a href="https://github.com/liamwalsh1980/Milestone-Project-4/blob/main/products/templates/products/edit_product.html" target="_blank">script</a>

- products app > products.html - <a href="https://github.com/liamwalsh1980/Milestone-Project-4/blob/main/products/templates/products/products.html" target="_blank">script</a>

## PEP8 online validator

I used the <a href="http://pep8online.com/" target="_blank">PEP8 online</a> validator to check all python files. The following files were checked and confirm 'All right' except for one error found in most files (line to long). All files below with a ** has this error. 

### Book App
- book app - app.py
- book app - contexts.py
- book app - urls.py
- book app - views.py

### Cart App
- cart app - apps.py
- cart app - contexts.py
- cart app - urls.py
- cart app - views.py **

### Checkout App
- checkout app - admin.py
- checkout app - apps.py
- checkout app - forms.py
- checkout app - models.py **
- checkout app - signals.py
- checkout app - test_forms.py
- checkout app - urls.py
- checkout app - views.py **
- checkout app - webhook_handler.py **
- checkout app - webhooks.py **

### Complete App
- complete app - admin.py
- complete app - apps.py
- complete app - emails.py
- complete app - forms.py **
- complete app - models.py
- complete app - test_forms.py
- complete app - urls.py
- complete app - views.py

### Home App
- home app - apps.py
- home app - urls.py
- home app - views.py

### Products App
- products app - admin.py
- products app - apps.py
- products app - forms.py
- products app - models.py
- products app - urls.py
- products app - views.py **
- products app - widgets.py **

### Profiles App
- profiles app - apps.py
- profiles app - forms.py **
- profiles app - models.py **
- profiles app - urls.py
- profiles app - views.py

### Services App
- services app - admin.py
- services app - apps.py
- services app - models.py **
- services app - urls.py
- services app - views.py

### The Bike Shop App
- the_bike_shop app - asgi.py
- the_bike_shop app - settings.py **
- the_bike_shop app - urls.py
- the_bike_shop app - wsgi.py

### Project Level
- project level - manage.py





