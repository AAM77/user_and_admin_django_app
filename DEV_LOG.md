


[]Links for navigating to (a) a registration page, (b) a login page, and for (c) signing out. This could be via a navbar in the layout---if it works similar to Rails.
[]Creating a registration page with a form with all required fields.
[]The email & URL should be validated for the correct format (what is the format?).
[]Creating a login page with a form to log in with... what exactly? (e.g. email, first name? password?).
[]Creating a User landing page that displays a welcome message, the user's first & last names.
[]Logging out should require something like a confirmation pop up when attempting to log out.
[]Users should see a confirmation upon logging out (like a flash message or alert) once the redirect view (i.e. logout confirmation page) loads.
[]The new view should display a logout confirmation message & a login link.
[]Unless Django handles things differently, I'll need at least a user model.
[]Since I'm persisting data, I'll need a migration for the User model with the indicated attributes (I will need to look into how Django deals with making them required &  validating their presence/format on the backend).
[]An admin-type super-user who is able to add, edit, and delete all users via a UI arranged in a way I see fit.  I will see how Django handles this. but it seems like I can provide an attribute to designate a User as an admin/super user.
[]A way to handle session creation (upon logging in) & termination (upon logging out)