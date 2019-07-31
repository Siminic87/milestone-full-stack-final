# Online Marketing - Issue Tracker
The “Online Marketing - Issue Tracker” is an online tool with which owners of small and medium sized businesses can post/upvote bugs and feature requests regarding the products and services that are offered on MarketingMan.ie.

## Demo
A live demo can be found at [Heroku: Cloud Application Platform](https://milestone-full-stack-final.herokuapp.com)

## UX
The purpose of the Online Marketing Issue Tracker is to allow users to have a say in what products and bugs are tended to in terms of the products that offered on MarketingMan.ie. This is done via a voting system where bugs can be uptoved for free and feature requests at cost of 10$. 

The page is for any individual or company worldwide who has an interest in the products on MarketingMan.ie and would would like to influence the course of development.  

The Online Marketing Issue Tracker is the best way to influence the course of development at MarketingMan.ie because it gives a quick and comprehensive overview of bugs and featuer requests that have already been posted as well as allowing users to create topics of their own. Via the integrated voting system, users then have a quick and efficient way of having their say as to what bugs and features are tended to. 

- As a user type, I want to get a quick overview of bugs and feature requests that have already been posted by users of MarketingMan.ie. 
- As a user type, I want to be able to assess and vote on the urgency with which bugs and feature requests are developed.
- As a user type I want to be able to post, edit and delete bugs and feature requests that I would like to have tended to by the developers.
- As a user type I want to be able to discuss bugs and feature requests with other users.

### Mockups:
#### Desktop
![SEO User-Exchange Mockup - Desktop](/media/img/OM-Issue-Tracker-Desktop.jpg)

#### Tablet / Mobile
![SEO User-Exchange Mockup - Tablet/Mobile](/media/img/OM-Issue-Tracker-Tablet-Mobile.jpg)

## Features
The Online Marketing - Issue Tracker has various features that intend to allow users to get a quick overview of various bugs and feature requests that have been requested by other users. Users can then also post on vote on bugs and feature requests that they poersonnally would like to see tended to by the developers. 

### Existing Features
- User registration and authentication based on email and password.
- List of database entries – All bugs and feature requests are summarized on a list individual cards on the main page. Information contained on the cards is title, description, tcategory, number of upvotes and upvoting button. Results are ordered by number of upvotes in descending order.
- Filtering of results by category (bug vs. feature request).
- Bugs and feature requests can be upvoted once per user. Payment required for upvoting feature request, but purchase of multiple upvotes possible. 
- Posting, editing and deleting of bugs and feature requests.
- Detail view of individual bugs and feature requests. 
- Commenting on exising bugs and feature requests in detail view.
- Summary graphs showing how many feature requests and bugs are tended to on a daily, weekly and monthly basis.
- More information about service package on "about" page.

All features fully responsive on mobile devices (incl. tablets and smartphones). 

### Features Left to Implement
- Blog pages with developer updates.
- Reward pages for most active purchasers of upvotes
- Continuous Automatic Testing with Travis

## Technologies Used
- HTML
    - The project uses HTML code to allow structuring and display of the information presented on MarketingMan.ie.
- [Python](https://www.python.org/) & [Django](https://www.djangoproject.com/start/overview/)
    - The logic for rendering the various app routes is written in Python coding language. In order to streamline this process, the Django web framework written in Python was used.
- CSS
    - The project uses CSS code to visually design and animate the page's structure as defined by the HTML.
- [Bootstrap](https://getbootstrap.com/)
    - The project uses the Bootstrap framework (v. 4.3.1) to save time in development by relying on standardized HTML and CSS elements that can be found in the library.
- [jQuery](https://jquery.com/) & [Bootstrap javascript](https://getbootstrap.com/)
    - The project uses jQuery (v. 3.4.1) and Boostrap javascript (v. 4.3.1) for enabling execution of stripe payment services.
- [Stripe](https://pypi.org/project/stripe/)
    - The project uses "stripe", a Python library for interacting with Stripe’s API (v. 2.32.1).
- [Chart.js](https://www.chartjs.org/)
    - The project uses the chart.js javascript library for the purpose of visually summarising the databse entries on the portal (v. 2.8.0)
- [Django REST Framework](https://www.django-rest-framework.org/)
    - The project uses the Django REST framework which is a powerful and flexible toolkit for building Web API in this instance for visualising data from the database in the charts. 
- [Django Comments](https://django-contrib-comments.readthedocs.io/en/latest/quickstart.html)
    - The Django Comments framework can is used to attach comments to feature and bug posts. 
- [Django Forms Bootstrap](https://pypi.org/project/django-forms-bootstrap/)
    - The Django Forms Bootstrap framework is used to easily apply bootsrap styling to all forms in the app.

## Testing
1.  Quick overview of all posted bugs and feature requests
    1. Go to Online Marketing - Issue Tracker homepage
    2. Verify that bug and feature request cards are ordered in descending order according to number of upvotes and that only 10 results are shown per page and that the remaining results can be accessed via the pagination links.
    3. Try to click on category links above results and verify that depending on selected category, only results for this category are displayed.
    4. Try to click on “summary” link in top navigation and verify that the 2 graphs reflect current results of "Done" bugs and feature requests and change dynamically when database is edited.

Manual testing revealed that the “overview” and “summary" were integrated and visualised seamlessly. The pages are accessible on all devices and all major browsers and look virtually the same on different browsers.

2.	Assessing and voting on urgency of bugs and feature requests
    1. Go to Online Marketing - Issue Tracker homepage
    2. Try scrolling down results and verify that individual bug and feature request cards show number of received upvotes (See “Up:”).
    3. OR try to “Login” in via main navigation and verify that individual bug and feature request cards now have an upvote button.
    4. Try to click on upvote button of BUG and verify that total number of upvotes of the chosen bug goes up by 1. Verify that when same bug gets upvoted a second time by same user, message "you already upvoted this!" appears above results.
    5. OR try to click on upvote button of FEATURE REQUEST and verify that chosen number of upvotes in form of the chosen feature gets transferred to cart as indicated by badge icon on top navigation and actual cart page that user is now redirected to. Verify that subtotals and total Euro amount for chosen number of upvotes is correct.
    6. Try to click on "checkout" and verify that purchase can succesfully be made with 4242 4242 4242 4242 stripe test credit card when purchase information is entered in form fields. Verify that sub-totals and total are still correct on checkout page.
    7. OR try to “login” via main navigation, click on the “Read More” button on an individual card (either on filtered or non-filtered results page) and verify that the individual feature request or bug card now has an upvote button.
    8. Try to click on the upvote button and verify that total number of upvotes of the chosen BUG goes up or down accordingly.
    9. OR try to click on upvote button of FEATURE REQUEST detail apge and verify that chosen number of upvotes in form of the chosen feature gets transferred to cart as indicated by badge icon on top navigation and actual cart page that user is now redirected to. Verify that subtotals and total Euro amount for chosen number of upvotes is correct.
    10. Try to click on "checkout" and verify that purchase can succesfully be made with 4242 4242 4242 4242 stripe test credit card when purchase information is entered in form fields. Verify that sub-totals and total are still correct on checkout page. 

Manual testing revealed that assessing and voting on bugs and feature requests was integrated and visualised seamlessly. The functionality is accessible on all devices and all major browsers and looks virtually the same on different browsers. 

3.	Posting, editing and deleting bugs and feature requests
    1. Go to Online Marketing - Issue Tracker homepage
    2. Try to “login” in via top navigation, click “+Add Bug / Feature Request!” button on the right of results (or "+Add Bug" / "+Add Feature Request" on filtered pages) OR ”New Issue” link in main navigation and verify that form for posting new issue loads correctly and includes fields for “title”, “content", “image”, publishing date, "type" and "category".
    3. Try to populate fieds, click “SAVE” below form and verify that user is redirected to unfiltered results page and that the new bug or feature request is included in results.
    4. OR try to “login” via main navigation, click on the “Read More” button on an individual bug or feature request card (either on filtered or non-filtered results page), click “Edit Post” button and verify that form fields get populated correctly with data from chosen bug or feature request.
    5. Try making changes to pre-populated fields and click “SAVE” and verify that user is redirected to unfiltered results page and that the edited bug or feature request is included in results.
    6. OR try to “login” via main navigation, click on the “Read More” button on an individual bug or feature request card (either on filtered or non-filtered results page), click “Delete Post” button and verify that browser throws pop-up “Are you sure?”.
    7. Try clicking “OK” and verify that user is redirected to unfiltered results page and that the deleted bug or feature request was removed from results.

Manual testing revealed that adding, editing and deleting bugs and feature requests was integrated and visualised seamlessly. The functionality is accessible on all devices and all major browsers and looks virtually the same on different Browsers.

4.  Discussing bugs and feature requests
    1. Go to detail page of individual bug or feature request by clicking read more on summary card in overview
    2. Try to populate comment form on bottom of page, click post and verify that comment including appears underneath commented on bug or feature request when navigating back to detail page from comment thank you page.

Manual testing revealed that the “overview” and “summary" were integrated and visualised seamlessly. The pages are accessible on all devices and all major browsers and look virtually the same on different browsers.

Bug noticed in that cart doesn't update sometime when multiple feature requests are upvoted. To be fixed.

Potential bug noticed after deletion of bug or feature request, producing "No Post matches the given query" for all pages.

## Deployment
This app is hosted using Heroku: Cloud Application Platform.

Static assets and user uploaded files hosted via AWS S3. See process of setting up S3 with Django [here](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html).

To deploy the app from an AWS cloud9 environment, initialize git repository via "git init" command in terminal window. Once all changes have been tracked via "git add" and "git commit -m 'INSERT YOUR COMMIT DESCRIPTION HERE'", upload to a desired github repository that you have created for this purpose via "git remote add origin https://github.com/YOURUSERNAME/YOURREPONAME" and "git push -u origin master" commands. Then log in to heroku (heroku.com) and create new app by clicking on "new" button in top right corner. Once app is created, click on app and go to "Deploy" section. Click on "GitHub" and search for the corresponding GitHub repository that you have created for this purpose and make sure that you click the button "Enable Automatic Deploys" below. Then go to "Resources", search for "Postgres" and install free Postgres database add-on.

Then go to settings and select "Reveal Config Vars" and set Config Vars:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DATABASE_URL
- DISABLE_COLLECTSTATIC
- SECRET_KEY
- STRIPE_PUBLISHABLE
- STRIPE_SECRET

For security reasons, these variables will not be revealed here. AWS variable to be obtained from S3 interface, Database URL from Heroku, Secret Key from Cloud9 environment and Stripe varaible from Stripe API pages.

Having put this in place, the live site updates automatically each time there is a new push to its [GitHub repository](https://github.com/Siminic87/milestone-data-centric-final). You can git clone the code to run it locally on your machine.

## Credits
Advice for restricting votes per user to 1 taken from [stackoverflow.com](https://stackoverflow.com/questions/38332868/restrict-each-user-to-only-vote-once-polls-django-python?noredirect=1&lq=1)

Advice for querying database for entries older than certain date taken from [stackoverflow.com](https://stackoverflow.com/questions/1984047/django-filter-older-than-days)

Also, big thank you to my mentor Jim Richmond and the wonderful tutors at CodeInstitute.