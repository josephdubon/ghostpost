# 👻GhostPost 👻

The GhostPost Machine™ is a website where people can anonymously post Boasts or Roasts of whatever they want. Like most
services, there is a character limit: 280 characters. We are deliberately not dealing with logins, as that is outside
the scope of the project (and beyond our time constraints).

#### Features

Back end:

* <span>One model to represent both boasts and roasts</span>
    * <span>Boolean to tell whether it's a boast or a roast</span>
    * <span>CharField to put the content of the post in</span><span></span>
    * IntegerField for up votes
    * IntegerField for down votes
    * DateTimeField for submission time

Front end:

* Homepage that displays boasts and roasts, sorted by time submitted (hint
* Buttons to filter the content by either boasts or roasts, sorted by time submitted
* Upvote and downvote buttons for each boast and roast
    * when clicked, these buttons affect the numbers on the relevant post appropriately
* Page to submit a boast or a roast