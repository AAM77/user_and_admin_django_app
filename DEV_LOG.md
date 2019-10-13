# DEV LOG

## Backend

[] Create a User model                 ---- (if not an internal component of Django)
[] Create routes                       ---- see how these work compared to controllers
[] Create a view (multiple views?)     ---- figure out how these work compared to controllers
    []  SESSION
        [] Create
        [] Delete/Destroy

    [] USER
        [] New/    Create
        [] Edit/   Update
        [] Delete/ Destroy

[] Create migrations                   ---- figure out how these work in Django
[] Set up an 'Admin'-'Super-User' who can add, edit, & delete other users via a webpage



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

[] Create a Log In Page
        [] Create a log in Form
            [] Email
                [] Validate Email format --- ( xxx@xxx.com )
            [] Password


[] Create a user-landing page (for log in)
        [] Display a Welcome Message
            [] Include first name
            [] Include last name

[] LOG OUT should trigger confirmation pop up
[] Create a confirmation page that logging out redirects to (a page users see when they successfully log out)
        [] Display a confirmation message
        [] Provide an additional link to log in

[] Create a page/UI for an admin-type super-user
    [] Manage Users
        [] can add
        [] can edit
        [] can delete