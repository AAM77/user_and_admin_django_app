# DEV LOG

## Backend

```
[x] Create a users app
[x] add users to INSTALLED_APPS
[x] Create a Custom User model
        [x] Make all fields required
            [x] First name
            [x] Last name
            [x] Email
                [] Validate Email format --- ( xxx@xxx.com )
                [x] Email should be unique
                [] Email should be case insensitive
            [x] Password
            [x] URL - personal website/portfolio
                [] Validate URL format   --- ( http://xxx )
[] Create routes
    [x] home
    [x] registration page
    [x] logout

[] Create views
    [x] home
    [x] register
    [] login
    [x] logout

    [x]  SESSION
        [x] Create - login
        [x] Delete/Destroy - logout

    [] USER
        [x] New/    Create
        [] Edit/   Update
        [] Delete/ Destroy

[x] Create Migrations
[x] Migrate
[x] Create a superuser who can add, edit, & delete other users via a webpage (will admins have the same capability?)
```



## Frontend

```
[x] Create a layout-template that accepts partials/other html templates via something like yield
[] Create a navbar inside this template with the following stubs:
        [] (a) Register        ---- display conditionally
        [] (b) Log In          ---- display conditionally
        [] (c) Sign Out        ---- display conditionally

[] Create a universal landing page with a welcome message --- ((( is this even possible in Django? )))
[] Create a registration page
        [x] Create a Form
        [x] Make all fields required
            [x] First name
            [x] Last name
            [x] Email
                [] Validate Email format --- ( xxx@xxx.com )
            [x] Password
            [x] URL - personal website/portfolio
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

[] LOG OUT should trigger confirmation pop up --- OPTIONAL
[x] Create a confirmation page that logging out redirects to (a page users see when they successfully log out)
        [x] Display a confirmation message
        [] Provide an additional link to log in

[] Create a page/UI for an admin-type super-user
    [x] Manage Users
        [x] can add
        [x] can edit
        [x] can delete