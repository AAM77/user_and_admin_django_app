# DEV LOG

## Backend

[] Create a User model                 ---- (if not an internal component of Django)
[] Create routes                       ---- see how these work compared to controllers
[] Create a view (multiple views?)     ---- figure out how these work compared to controllers
[] Create migrations                   ---- figure out how these work in Django



## Frontend

[] Create a layout-template that accepts partials/other html templates via something like yield
[] Create a navbar inside this template with the following stubs:
        [] (a) Register        ---- display conditionally
        [] (b) Log In          ---- display conditionally
        [] (c) Sign Out        ---- display conditionally

[] Create a universal landing page with a welcome message
[] Create a registration page
        [] Create a Form
        [] Make all fields required
            [] First name
            [] Last name
            [] Email
                [] Validate Email format --- ( xxx@xxx.com )
            [] Password
            [] URL - personal website/portfolio
                [] Validate URL format   --- ( http://xxx )

[] Create a user-landing page (for log in)
        [] Display a Welcome Message
            [] Include first name
            [] Include last name

[] Create a Log In Page
        [] Create a log in Form
            [] Email
                [] Validate Email format --- ( xxx@xxx.com )
            [] Password
                


[] BREAK DOWN THE FOLLOWING STEPS IN THIS LOG:

[x] Links for navigating to (a) a registration page, (b) a login page, and for (c) signing out. This could be via a navbar in the layout---if it works similar to Rails.
[x] Creating a registration page with a form with all required fields.
[x] The email & URL should be validated for the correct format (what is the format?).
[] Creating a login page with a form to log in with... what exactly? (e.g. email, first name? password?).
[x] Creating a User landing page that displays a welcome message, the user's first & last names.
[] Logging out should require something like a confirmation pop up when attempting to log out.
[] Users should see a confirmation upon logging out (like a flash message or alert) once the redirect view (i.e. logout confirmation page) loads.
[] The new view should display a logout confirmation message & a login link.
[] Unless Django handles things differently, I'll need at least a user model.
[] Since I'm persisting data, I'll need a migration for the User model with the indicated attributes (I will need to look into how Django deals with making them required &  validating their presence/format on the backend).
[] An admin-type super-user who is able to add, edit, and delete all users via a UI arranged in a way I see fit.  I will see how Django handles this. but it seems like I can provide an attribute to designate a User as an admin/super user.
[] A way to handle session creation (upon logging in) & termination (upon logging out)