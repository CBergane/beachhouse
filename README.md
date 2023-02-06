# Beach House!

![Beach house mockup image](readme/media/mockup.jpg)

Beach House is a mock site for a communety that wishes to rent out their summer houses to guets.
The main fokus of the site is an easy way for the guests to get an overview of what kind of properties there is to rent, the guest can filter from a list of options to get a more spesific house to rent.

If the user is a house owner that wiches to rent out their hose the can fill out an aplication for the house to the site owner whom will get preview of the house and can then choose to display it or not.

Visit the deployed site [here](https://airbnbbeachhouse.herokuapp.com/index).

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
        3. [Strategy Table](#strategy-table)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
    4. [Skeleton](#skeleton)
    5. [Surface](#surface)
2. [Features](#features)
    1. [General](#general)
    2. [Home Page](#home-page)
3. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependecies Installed](#packages--dependecies-installed)
    4. [Database Management](#database-management)
    5. [Tools and Programs](#tools-and-programs)
4. [Testing](#testing)
    1. [Go to TESTING.md](https://github.com/josswe26/code-buddy/blob/main/TESTING.md#code-buddy-testing)
5. [Deployment](#deployment)
6. [Finished Product](#finished-product)
7. [Credits](#credits)
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)


***

## User Experience (UX)

### Strategy

#### Project Goals

* The website contains simple colors for a modern design and also to not draw attention from the content.
[add a pic of colors for the site here]

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly.

* Site users are able to register an account in order to interact with the content.

* The users can both book and add a house for rent.

* The site admin can then sort between the houses and choose witch to display.


#### User Goals

* As a Site Admin, I want to manage the site content.

* As a Site User, I want to be able to interact with the content.

* As a Site User, I want the information to be easy to find and read.

* As a Site User, I can do a booking or add a house for rent.

* As a Site User, I want to manage the content I created.


#### Strategy Table

Strategy | Description |
--- | --- | 
User signups | Make it easy for users to signup to the page. |
An easy way for users to display their houses for new custumers | Offer better tools for property owners to list and showcase their properties, encourage more detailed and attractive listings. |
Enhance guest experience | Streamline the booking and check-in process. |
Have a responsive design | Make the content responsive on smaler divices. |


### Scope

Since this is a mock site, there is no actual booking of real houses, but the goal is that I should be able to use it in real life as close to ready to go.
The purpose of this site is for a community to have a portal for their houses to be rented out for a set price.
Some of the functions:

* Responsive design.
* A easy way to sign up.
* List houses that have been approved by the site admin for display.
* An easy way for the site admin to see what's going on and control it.
* An easy way for the owners of the houses to list their house/houses.

#### User Stories

GitHub projects was used as my project management tool to track user stories.

**Start Of The Project**

![User Stories Progress - Start](readme/media/github.com-projects-start.jpg)

**Week 1**
![User Stories Progress - Week 1](readme/media/github.com-projects-first.jpg)

**Week 2**
![User Stories Progress - Week 2](readme/media/github.com-projects-middle.jpg)

**Week 3**
![User Stories Progress - Week 3](readme/media/github.com-projects-last.jpg)

**Week 4**
![User Stories Progress - Week 4](readme/media/github.com-projects-end.jpg)


### Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively. Here you can you can find the website map design.

![beachhouse site map](readme/media/sitemap.png)

**Contact Model**

* fname: A fisrt name must be added to the message.
* lname: A last name must be added to the conntact form.
* email: An email addres to let the staff get in contagt with whom ever sent the message.
* message: A message with a max length of 300 and cant be left blank.

**House Model**

* name: Gives the house a name.
* adress: Gives a adress to the house so the booker can lokate it.
* owner: A owner for the house and it can't be left blank.
* beds: Number of beds that the house contains.
* capacity: the number of guets that the house will hold.
* price: Give a price per night.
* description: The owner diescribes the house but can be left blank.
* house_image: A picture of the house but there is a default img given be the site if none is given.
* has_tv: If the house have a tv in the inventory.
* has_wifi: If the house have wifi in the inventory.
* has_bbq: If the house have a bbq in the inventory.
* has_shower: If the house have a shower in the inventory.
* has_bath: If the house have a bath in the inventory.
* BED_SIZE_CHOICES: the deferent choices of bed sizes to choose from.
* bed_size: the choice made be the owner to be displayed for the user.
* approved: a approved option from the staff/admin to be displayed, set to false so it can be inspected first.

**Booking Model**

* user: Set to whom is loged in as a foreignkey and all bookings made with this user will be deleted if the user is delted.
* house: Also set to foreignkey and bound to the house, if the house is deleted the bookings on the house will be delted with it.
* checkin: The checkin date for the house.
* checkout: The checkout date for the house.


### Skeleton

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version/Tablet Version/ Mobile Version
--- | ---
Index | ![Wireframe index.html](readme/media/wireframe_index.png)
House list | ![Wireframe houselist.html](readme/media/wireframe_house_list.png)
Booking | ![Wireframe booking.html](readme/media/wireframe_booking.png)
Profile | ![Wireframe profile.html](readme/media/wireframe_profile.png)
Admin | ![Wireframe admin.html](readme/media/wireframe_admin.png)

### Surface

#### Color Scheme

The colors are were chosen keeping in mind simplicity but also providing the website a modern design. This in order to keep the focus on the content but also appealing for the users.

![Color scheme image](readme/media/color_palette.png)

#### Typography

The main font being used in the site is Poppins, with sans-serif as a fallback in case Poppins doesn't get imported correctly. 

[Back to top ⇧](#beach-house)

## Features

### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.

* Navigation Bar