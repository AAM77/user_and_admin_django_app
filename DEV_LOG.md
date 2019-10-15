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
[x] Create routes
    [x] home
    [x] registration page
    [x] logout

[x] Create views
    [x] home
    [x] register
    [x] login
    [x] logout

    [x]  SESSION
        [x] Create - login
        [x] Delete/Destroy - logout

    [x] USER
        [x] New/    Create

[x] Create Migrations
[x] Migrate
[x] Create a superuser who can add, edit, & delete other users via a webpage (will admins have the same capability?)
```



## Frontend

```
[x] Create a layout-template that accepts partials/other html templates via something like yield
[x] Create a navbar inside this template with the following stubs:
        [x] (a) Register        ---- display conditionally
        [x] (b) Log In          ---- display conditionally
        [x] (c) Sign Out        ---- display conditionally

[x] Create a universal landing page with a welcome message
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


[x] Create a user-landing page (for log in)
        [x] Display a Welcome Message
            [x] Include first name
            [x] Include last name

[x] Create a confirmation page that logging out redirects to (a page users see when they successfully log out)
        [x] Display a confirmation message
        [x] Provide an additional link to log in

[x] Create a page/UI for an admin-type super-user
    [x] Manage Users
        [x] can add
        [x] can edit
        [x] can delete