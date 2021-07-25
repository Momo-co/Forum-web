# Forum-web

## Introduction
For my project I decided to make a Forum Website where users can share a post about an idea they would like to discuss or raise an issue. Other users can then view the post and add their own comment to give their opinions to discuss about the post. 

The following is how my CRUD functionailty will be implemented.

Create:
* A brand new post
* A new comment in a post that have already been created

Read:
* Any posts that have already been created
* Any comments that have already been created

Update:
* Any posts that have already been created
* Any comments that have already been created

Delete:
* Any posts that have already been created
* Any comments that have already been created

## Software Design

### Entity Relationship Diagram
For the first draft of desgining my Entity Relationship Diagram (ERD), I started with three entities. The following image is what my entity relationship digram looked like.

I then decided to change it since I realised that there was no longer going to have a user log-in feature in the application.

For the new entity relationship digram I decided to remove the user entity and its relationships towards other entities. This means that any user can use the app without any sign-up or registration.

With my new entity relationship, it is a one to many relationship where a single post can contain one or many comments while an individual comment belongs to one post. 

This ERD would then ensure that user must require a post to be created before they can start creating a comment. 

### User Story
Looking at an end-user point of view, there are objectives that matters to end-users. The following user stories explores the end-goal that a user would like to obtain at first glance. 

First User Story
* As a User
* I want to create a post
* So that I can share a new idea to other users

Second User Story
* As a User
* I want to create a comment on a post
* So that I can discuss and share my ideas on a post I picked

Third User Story
* As a User
* I want to view all the posts
* So that I can pick the post I want to discuss about

Even though the above user story seems sufficient, I noticed it lacked update and delete features for my CRUD application. Since the above user story covers the create functionality, user story regarding the update and delete functionality can be built. Then I decided to have more user stories that would involve update and delete features resulting in the following user story.

Fourth User Story
* As a User
* I want to re-edit a created post
* So that I can fix any spelling errors or add additional information on the post

Fifth User Story
* As a User
* I want to re-edit a created comment
* So that I can fix any spelling errors or add additional information on the comment

Sixth User Story
* As a User
* I want to delete a created post
* So that I can either consider its issue or discussion to be solved or consider it to be no longer productive/useful

Seventh User Story
* As a User
* I want to delete a created comment
* So that I can remove it given that it isn't a helpful suggestion

Finally I remembered that the comments should be viewed at a relavent place rather than a random home page. Therefore the user story below should sufice 

Eigth User Story
* As a User
* I want to view all comments of a post
* So that I read discussion of the post from other users

### CI Pipeline










