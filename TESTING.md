# Beach House Testing

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
The warnings I choose to ignore since they are imorted with packeges. And the jQuery for future uses.
![index.html validation eddited](readme/media/validator.w3.org-index-edited.png)

W3C Markup Validator concerning bookings_list.html.
![bookings_list.html validation](readme/media/validator.w3.org-bookings_list.png)
The info I have looked as best i can but I can not find it in my code so I'm choosing to ignore it.

W3C Markup Validator concerning house_list.html.
![house_list.html validaton](readme/media/validator.w3.org-house_list.png)
The same javascript warnings are ignored.

W3C Markup Validator concerning bookinglistadmin.html.
![bookinglistadmin.html validation](readme/media/validator.w3.org-bookinglistadmin.png)
Warnings of the unused javascript are ignored on this page as well.

W3C Markup Validator concerning bookings_update.html.
![bookings_update.html validation](readme/media/validator.w3.org-bookings_update.png)
Warnings of the unused javascript are ignored on this page as well.

W3C Markup Validator concerning house_update.html.
![house_update.html validation](readme/media/validator.w3.org-house_update.png)
Warnings of the unused javascript are ignored on this page as well.

W3C Markup Validator concerning house.html.
![house.html validation](readme/media/validator.w3.org-house.png)
Warnings of the unused javascript are ignored on this page as well.

### CSS

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the CSS code of the project to ensure there were no syntax errors. 

W3C CSS Validator found no errors in my CSS but found four warnings. But I choose to ignore them since they fill a function.

![CSS Validation](readme/media/jigsaw.w3.org-css-validator.png)

### Pyhton

Pylint was used continuously to analyse the Python code for programming errors during the development process.

[PEP8 online](http://pep8online.com/) is offline and can't be used, so I rely on pylint.

### JavaScript

[JSHints JavaScript Code Quality Tool](https://jshint.com/) validated the site's JavaScript code.
![Javascript validation](readme/media/jshint.com-script.png)
![Javascript validation](readme/media/jshint.com-map.png)

## Accessibility

Lighthouse in Chrome DevTools and [GTmetrix](https://gtmetrix.com) have been used to confirm that the colours and fonts used throughout the website are easily read and accessible. GTmetrix was used if the lighthouse fell below 90 in any category to get a more in-depth report. See reports in the table below:

### Lighthouse Reports

Page | Lighthouse Report | GTmetrix report |
| --- | --- | --- |
| Index | ![Index Lighthouse Report](readme/media/lighthouse-validator-index.jpeg) | ![Index GTmetrix Report](readme/media/gtmetrix-validator-index.jpeg) |
| Profile | ![Profile Lighthouse Report](readme/media/lighthouse-validator-profile.jpeg) | - |
| House list | ![House List Lighthouse Report](readme/media/lighthouse-validator-houselist.jpeg) |
| Login | ![Login Lighthouse Report](readme/media/lighthouse-validator-login.jpeg) |
| Register | ![Register Lighthouse Report](readme/media/lighthouse-validator-signup.jpeg) |
| Admin | ![Admin Lighthouse Report](readme/media/lighthouse-validator-admin.jpeg) |
| Add Boooking | ![Add Booking Lighthouse Report](readme/media/lighthouse-validator-addbooking.jpeg) | ![Add Booking GTmetrix Report](readme/media/gtmetrix-validator-addbooking.jpeg)
| Update Booking | ![Update Booking Lighthouse Report](readme/media/lighthouse-validator-bookingupdate.jpeg) |
| Add House | ![Add House Lighthouse Report](readme/media/lighthouse-validator-addhouse.jpeg) |
| Update House | ![Update House Lighthouse Report](readme/media/lighthouse-validator-houseupdate.jpeg) |

## Tools Testing

### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

Chrome DevTools was used during the development process to test, explore and modify the project's HTML elements and CSS styles.


### Responsiveness

* [Am I Responsive?](http://ami.responsivedesign.is/#) was used to check the responsiveness of the site pages across different devices.

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing

### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Safari | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Mozilla Firefox | No responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Microsoft Edge | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |


### Device Compatibility

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
Dell Optiplex 7060 | Windows 11 | No appearance, responsiveness or functionality issues. | <span style="color:green">Pass</span> |
MacBook Air | macOS Big Sur | No appearance, responsiveness or functionality issues. | <span style="color:green">Pass</span> |
iPad Pro 12.9" | iOS 15 | No appearance, responsiveness or functionality issues. | <span style="color:green">Pass</span> |
iPad Pro 10.5" | iOS 15 |No appearance, responsiveness or functionality issues. | <span style="color:green">Pass</span> |
iPhone XR | iOS 15 |No appearance, responsiveness or functionality issues. | <span style="color:green">Pass</span> |
iPhone 7 | iOS 15 |No appearance, responsiveness or functionality issues. | <span style="color:green">Pass</span> |

### Test Results

#### General

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=16>Navigation Bar</td>
        <td rowspan=2>Main logo link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Home page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Home link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Home page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Register link</td>
        <td rowspan=2>Unregistered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Register page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Login link</td>
        <td rowspan=2>Unregistered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Login page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Logout link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link activated the Logout modal.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Our Houses link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Our Houses page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <td rowspan=2>Admin link</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the Admin page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Hamburger Menu button </td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button toggle navigation menu.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Responsive navigation menu on smaller screens.<br>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=10>Footer</td>
        <td rowspan=2>Logo link</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link redirects to the home page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Facebook icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens the Facebook page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <tr>
        <td rowspan=2>LinkedIn icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens the LinkedIn page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Instagram icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens the Instagram page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <tr>
        <td rowspan=2>GitHub icon</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the link opens the GitHub page on a separate tab.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Home Page 

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Parallax image</td>
        <td rowspan=2>Scroll function</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Scrolling the page activates the Parallax effect.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Form button</td>
        <td rowspan=2>Submit function</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Clicking the button sends the message form and reloads the main page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Google Map</td>
        <td rowspan=2>Location set</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Showing the location on Google maps</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### Register 

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Send registration form</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Register the user and redirect to the main page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Login 

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Checking user name and password.</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>If correctly entered username and password redirect to the index page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Profile

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Update button</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Update the booking or house depending on with button you click.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Delete</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Activate a modal for deleting a booking.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Add house</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Sends you too an add house page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Our Houses

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Filter</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Displays the filter options.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Reset</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Resets the filter options and reloads the page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected</td>
        <td><span style="color:green">Pass</span></td>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Apply.</td>
        <td rowspan=2>All</td>
        <td>Functionality</td>
        <td>Apply the options for the filter and displays the houses that match.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Book this house</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Send you to the booking site for a specific house.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Add Booking

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Date picker</td>
        <td rowspan=2>Pick date</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Allows you to pick a date to check in and check out.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Book this house</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Send you to the booking site for a specific house.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Book this house</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>If you choose a date in the past, the button will be blocked and display a message.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Go Back</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Send you back one page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Admin

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Previus month/next month</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you switch months back and forth.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Check out</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you as an admin on the site check out a guest if the check-out date is that day or has passed.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>House name</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you browse a house and see a preview of the inventory.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Update</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Updates the list of houses with the checked houses.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Delete message</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Lanches a modal to make sure you want to delete a message.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>    
    <tr>
        <td rowspan=2>Message counter</td>
        <td rowspan=2>Span counter</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Keeps a count of how many messages there are in the database.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>House check boxes</td>
        <td rowspan=2>Check boxes</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>The checked houses will show on the "Our houses" page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### House Preview

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>House card</td>
        <td rowspan=2>A preview of the House card</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you see how the house card will look.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Image will load on top and the description under.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <tr>
        <td rowspan=2>Inventory list</td>
        <td rowspan=2>A list of the inventory for the house that the filter function will use.</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you know what the house has and not.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
</table>

#### House Update

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>House Form</td>
        <td rowspan=2>A list of inputs for the owner to fill in</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Update any fields of chooice.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Use bootstrap layout from widgets.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
        <tr>
        <td rowspan=2>Inventory list</td>
        <td rowspan=2>A list of the inventory for the house that the filter function will use.</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you know what the house has and does not.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Delete</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Lanches a modal to make sure you want to delete.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Update</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Makes the changes to the database.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td rowspan=2>Page button</td>
        <td rowspan=2>Go Back</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Sends you back one page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>

#### Booking Update

<table>
    <tr>
        <th colspan=2>Feature</th>
        <th>Users</th>
        <th>Test</th>
        <th>Outcome</th>
        <th>Pass/Fail</th>
    </tr>
    <tr>
        <td rowspan=2>Booking form</td>
        <td rowspan=2>Date picker for checkin and checkout.</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you pick a date.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Booking form</td>
        <td rowspan=2>Date picker for checkin and checkout.</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Let you pick a date.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td rowspan=2>Page Button</td>
        <td rowspan=2>Book</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Update the booking, if the choosen date is in the past the button will be blocked and display an error message.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>    <tr>
        <td rowspan=2>Page Button</td>
        <td rowspan=2>Go Back</td>
        <td rowspan=2>Registered</td>
        <td>Functionality</td>
        <td>Sends you back one page.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
    <tr>
        <td>Style</td>
        <td>Hover effect working as expected.</td>
        <td><span style="color:green">Pass</span></td>
    </tr>
</table>