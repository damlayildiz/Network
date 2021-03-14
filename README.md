# Network
This is a Twitter-like social network website for making posts and following users.

## Features 
-   Users **create new text-based post**.
-   **All Posts Page** where users can see all posts from all users, with the most recent posts first. Each post includes the username of the poster, the post content, the date and time at which the post was made, and the number of *likes* the post has.
-   Clicking on a username takes users to **Profile Page**. This page displays
	- the number of followers the user has, and the number of people that the user follows.
    -  all of the posts for that user, in reverse chronological order.
    - *Follow* or *Unfollow* button that will let the current user toggle whether or not they are following this user’s posts.
-   **Following Page** which displays all posts made by users that the current user follows.
-   If there are more than ten posts on a page, a *Next* button takes the user to the next page of posts. If not on the first page, a *Previous* button takes the user to the previous page of posts.
-   By clicking **Edit button**,  user can edit the content of their post.
-   User and can **like or unlike** a post. 

## Screenshots and Demo
  ![Screenshot from 2021-03-14 01-09-43](https://user-images.githubusercontent.com/56313500/111062826-77967800-84bc-11eb-84d7-f2fbe10bed64.png)
---
  ![Screenshot from 2021-03-14 01-10-03](https://user-images.githubusercontent.com/56313500/111062875-bdebd700-84bc-11eb-9b2a-b816b5b55212.png)


[Youtube Demo Link](https://youtu.be/xZ2BfXU8EF8)

## Run Search locally

### Step 1: Clone project
```
 git clone https://github.com/damlayildiz/Network.git
 cd Network 
 ```
### Step 2: Run the project
```
 python manage.py runserver
 ```
