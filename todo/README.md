# Todo App

![alt text](https://raw.githubusercontent.com/kshintaku/django-apps/master/todo/ss-todo.png "Screen Shot")

Replicating a Todo app in Django for practice and fun.

## Things I learned

Learned how to modify database entries from the front end or user perspective without having to go into an admin or command line interface. I'm also getting better at front end elements with containers and implemented some Font Awesome icons.

Learned how to properly handle redirects to clear responses so a refresh doesn't resend data.

## Challenges I faced

I had an issue deploying to Heroku due to some iterations I made along the way to the database model and had to manually edit migration files in order for the database to be properly created and deployed.

Another challenge I faced was working with the collapsible menues; I had an issue with the initially open menu closing too quickly. I made a workaround by having a line in the javascript to edit the maxHeight of the object on load and that fixed the issue I was seeing.

## Improvements

- [ ] Create accounts so tasks aren't shared or modifiable by everyone.
- [x] Add the progress bar to show how much has been done.
- [ ] Limit the tasks to one week in duration with proper database filtering.
- [x] Animate collapse icon for smoother transition.
- [ ] Animate progress bar on task changes
