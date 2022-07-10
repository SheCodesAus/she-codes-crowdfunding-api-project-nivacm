# she-codes-crowdfunding-api-project-nivacm
The title of my project: **_CREAtive MigARTion._**

Target audience: **Migrant students and young artists**


As a young immigrant in Australia, you have the opportunity to become part of **CREAtive MigARTion** through art and critical thought.
An opportunity to reinterpret migration as a creative and positive experience that promotes personal and social development. 
## Links
[Github Pages] (https://github.com/SheCodesAus/she-codes-crowdfunding-api-project-nivacm)

### Projects
(https://desolate-meadow-66943.herokuapp.com/projects/)

### Users
(https://desolate-meadow-66943.herokuapp.com/users/)

### Pledges 
(https://desolate-meadow-66943.herokuapp.com/pledges/)

## A list of features will include:
1) Create Accounts.

    a) Fields:

        Name
        Email
        Username
        Password
        Bio
        Website
        image
    
    b) Link with the login page.
2) Login/Log out

    Error message if no creator(user) found prompt to create account.
3) Public profile

    Click on a user profile to see how many projects(workshops) a user has created.
        
        Edit profile
        All project list ordered by date and place.
        View pledges
            
            Art supplies
            Money

4) Workshops(Projects)

   Create Workshop(project)

        A) Fields 

           Title
           Owner
           Description
           Image
           Art supplies needed 
           Dates offering the workshops and place.

        B) Users can only create while logged in (connect user Login/sign up)
        
        C) Creators(users) can add multiples projects.
            
            Edit projects(only owners)
            Delete(only owners)

5) Pledges
    
    Form to pledge to project
         
         Fields
            
            Art supplies
            Anonymous
            Money
            Suggestions
    
    Pledges and suggestions are listed on the workshop detail page.
         
         User icon/photo, date, amount, comment.

## At least 3 additional features.

    Filters. Keyword search
    Profile. Add social media.
    Categories.

## An API specification table
    
**User1**
    
    username: annaleto
    Password: 123anna12

**User2**

    username: patribelen
    password: 123123pat12

 
| Method | URL          | Purpose       | Request body | Successful Response Code | Authorisation/Authentication |
| ------ | -----------  | ------------- | ------------ | ------------------------ | ---------------------------- | 
| GET    | /projects/   | Returns all   |              |        200               | n/a                          |
|        |              | project       |              |                          |                              |
| ------ | ----------   | ------------- | ------------ | ------------------------ | ---------------------------- | 
| Post   | /projects/   | Create a new  | Project      |        201               | Bearer Token                 |
|        |              | project       | object       |                          |                              |
| ------ | ----------   | ------------- | ------------ | -----------------------  | ---------------------------- | 
| get    | /users/1/    | View user     | User         |        200               | n/a                          |
|        |              | profile ID "1"| object       |                          |                              |
| ------ | ----------   | ------------- |------------- |------------------------- | ---------------------------- | 
| Post   | /users/      | Create a new  | User         |        201               | n/a                          |
|        |              | user          | object       |                          |                              |
| ------ | ----------   | ------------- | -----------  | ------------------------ |----------------------------  |
| Put    | /projects/1/ | Update the    | n/a          |        200               | Bearer Token                 |
|        |              | project ID"1" |              |                          |                              |
| ------ | ----------   | ------------- | ------------ | ------------------------ | ---------------------------- |
| get    | /pledges/    | All pledges   |              |        200               | n/a                          |
|        |              |               |              |                          |                              |
| ------ |  ---------   | --------------| ------------ | ------------------------ | ---------------------------- | 
| Post   | /pledges/    | Create a new  | Pledge       |        201               | n/a                          |
|        |              | pledge        | object       |                          |                              |
| -------|-----------   |---------------|------------- |------------------------  | ---------------------------- |
|Put     |/pledges/1/   | Update the    | n/a          |        200               |Bearer Token                  |
|        |              | pledge  ID "1"|              |                          |                              |
|------- |-----------   | ------------- |------------- | -------------------------| ---------------------------- |
| Delete |/pledges/1/   | Deletes the   | n/a          |        200               | Bearer Token                 |
|        |              |pledge  ID "1" |              |                          |                              |


# Do you want to register a new user?

First: 
    
    Open Insomnia and create a POST request on the URL https://desolate-meadow-66943.herokuapp.com/users/
    Then select JSON in the body of the POST request. Enter the following code:

'''
{
    "username": "solcito",
    "email": "solcito@gmail.com",
    "password": "stringsolcito",
}
'''

Select now SEND. If all the parameters are corrects you will obtain a 201 created success message and the new account will be created. If some of the parameters are incorrect you will receive a 400 bad request error.

# Do you want to create a Project?
First you need to be login in your account. For that, you need to create a POST request on the https://desolate-meadow-66943.herokuapp.com/api-token-auth/ to obtain your authentication token. You need to put the next code into the Body and selecting JSON.

'''
{
    "username": "solcito",
    "password": "stringsolcito",
}
'''


Then hit SEND. Copy the Token founded. Create a new POST request, but first make sure that the URL is
https://desolate-meadow-66943.herokuapp.com/projects/.
 Same as before in the body of the POST request select JSON. Enter the following code:

 '''
 {
	"title": "Reflexion",
	"description": "Reflexion of migration.",
	"goal": 150,
	"image": "https://via.placeholder.com/300.jpg",
	"is_open": true,
	"date_created": "2022-04-2T14:28:23.382748Z",
	"owner": "Real Creator"
 }
