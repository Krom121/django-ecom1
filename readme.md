# Affiliate Website Demo

For my final project I have decided to build an Amazon affiliated
website using the amazon links.
I have not gained access to the Amazon api's as I have to sell a number of items before I can gain access to the api's.

## Tech And Dependencies Used

    * Django version 3 is the main framework for this project.
  
    * Python verion 3.8 was used as the main oop language.

    * Bootstrap 4 theme used for the main layout for the project.
  
    * Django Ck Editor was used for writing the posts.

    * Django ImageKit was used to process uploaded images.

    * Django Taggit was use to help create tags for the posts.

## From Development to Production

In my first thoughts of what ecommerce website I could build, I did think of building my mouse mat website, but after much thought I decided to go with an affiliate website demo. As my mouse mat website would be to exposed, as I have alot of my own copyrighted designs for that. Deciding to do a affiliate website demo would pose less risk. I wanted the website to be affiliated with Amazon.com as there are thousands of products available for me to display. Unfortunately Amazon do not allow access to there api's straight away, only allowing me to use there links provided instead.

Which makes the decision easy, for a demo webiste with a landing page with products, a slider jumbotron, search bar and featured blogs and a main blog app.

### Bootstrap Theme

I downloaded a Bootstrap theme from <https://startbootstrap.com/>.
To which I put certian components into seperate html files. To allow me to use the Django include tag. This way my base.html file will be cleaner in code, orangized and readable.

Html files that use the include tag affiliate/templates/layout/

    * head.html
    * header.html
    * navagation.html
    * footer.html
    * scripts.html

Also you will find that the contact form is in the layout folder within the forms folder. The contact page uses the class based view FormView.

### Affiliate App

The affiliate app is a simple index page used as a landing page with products from the Amazon links. Search bar that is also provided by Amazon so users can look for more products. Featured blog posts to give demo website a more friendlier feel to the overall landing page. Allows users easy access to the posts that have been created.

### Blog App

The blog app was pre-built by me for my company webiste which in turn, the blog app has been used as boiler plate app. This app allows for users to access the posts created by the admin. I used flexbox for the layout of the post list page.

## Unit Testing

Thourgh out the project I manual tested links and buttons that where create to insure that the affiliate app and blog app where contected properly and that the contact form save the new contacts correctly.

Amazon links where tested through Amazon link checker, which allows me to check links that are created for products.
