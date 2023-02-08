[Back to the README.md file](https://github.com/CBergane/beachhouse#readme)  

[View the live website here](https://airbnbbeachhouse.herokuapp.com/index)

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)

***


## Testing User Stories

### 1. As a site admin/staff I can add new houses so the users can book them.
* A section under the user profile it was added so anyone can add a house but the in the admin/staff section the house need to be approved to be listed.

### 2. As an admin I can approve houses so that my community can list their homes easily.
* As in the previus section a function on the admin/staff side they can easaly se with houses has been approved and se in advance how they will look.

### 3. As a admin I can display my booking so that my users can see what too book.
* A site was made so the list of houses and the content was displayed for the user.

### 4. As a user I can sign upp so that book a house.
* An easy way to sign up was made with django allauth.

### 5. As a user I can place a booking so that I can go on hollyday.
* A link on the cards was made for each house so that the user can easaly choose a house too book.

### 6. As a user, I can filter my searches so that I can find a suitable house to rent.
* A filter form was put up on the list of houses to make it easy to choose what kind of house you are looking for.

### 7. As a user, I can send a question to the site admin so that I can get answers.
* A form was made on the index page so that a user can send questions to the admin.

### 8. As a user I can delete my booking so that change my mind of the booking.
* Under the profile where the user finds their bookings they can also find a delete link to remove a booking.

### 9. As a user I can edit my bookings so that so I can make changes.
* Under the same page, Profile, the user can find an update link so they can make an update to their booking.

### 10. As a user, I can list my house and edit it so that I can rent it out.
* Again under Profile page you can choose to put your house up for rent with a form that needs to be filed out. this form will then leater be approved by the site admin/staff.

## Code Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML code of the project in order to ensure there were no syntax errors.

W3C Markup Validator found the following errors concerning index.html.
![index.html validator errors](readme/media/validator.w3.org-index-before.png)
The error was solved be adding an alt tag to the logo img.
