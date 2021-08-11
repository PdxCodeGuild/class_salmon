#Project Name: **Boxy**

##Overview
Boxy is an application that allows users to *quickly bet on live football square pools*. Workplaces have long been the place to bet on football squares. This required an "admin" to print the poster board, draw crooked boxes, and illegibly write names in tiny square. In more recently, people would create excel spreadsheets and pass around old outdated files through email chains to keep track. Boxy aims to create an *easy to use*, *secure*, and *fast football square experience*.

##User Story
- As a user, I want to *log in to Boxy*, and *see my current sports pools*, because knowing which pools I'm betting on is relative to me.
- As a user, I want to **see which teams are playing**, so I can decided if I want to get into that pool.
- As a user, I want to see *how much I have won or loss*, because that will keep me informed.
- As a user, I want to know *how much I can win* in a sports pool, because this entices me to participate
- As a user, I want to know how much **time I have left to enter a pool**, because I play after the game is completed
- As a user, I want to know **how much money I have** in my wallet to play with, because I want to join into pools

##Features / Tasks
- Create a sign up
  - Register new users with fname, lname, email, username, password. No duplicate usernames allowed.

- Crete a log in / Log out portal
  - Users log in / log out at home page

- Create a wallet for funds
  - Each user receives a virtual wallet to load funds in to

- Create a shop for prizes
  - shop will contain gift cards which can be purchased with wallet funds

- Create a football square
  - make a 10x10 grid where users can claim cells
  - add a 1x10 top and a 10x1 side that contains numbers 0-9
  - add team name and logo to side and top
  - make 5 boards, one for each quarter
  - display total prize pool
  - display total players
  - display time left

- Crete a user dashboard with PnL and funds
  - show user wallet with Funds
  - show current boards in play
  - show wins and losses

- Crete a list of current teams playing
  - show live boards on home page

- Show historical boards
  - show finished boards on home page

- Pull sports scores down from [API](https://suredbits.com/api/#info)

##Data Model
- User
  - username
  - password
  - fname
  - lname
  - email
  - wallet
    - funds
  - Wins
  - losses

- Squares
  - teams
  - Users
  - positions

- Store
  - prizes

##Schedule
Aug 9 - Aug 12: Milestone 1
Aug 13 - Aug 18: Milestone 2
Aug 19 - Aug 20: Milestone 3
Aug 23 - Aug 25: Milestone 4
Aug 25 -Aug 26: Milestone 5

###Milestones
1. Set up new [Django Project](https://github.com/PdxCodeGuild/class_salmon/blob/main/4%20Django/docs/Django%20Project%20Setup.md)
  - Create home page template
    - show live boards and completed boards
  - Create square view
    - optimize for mobile
  - Create user profile page template

2. Create backend logic for board
  - 2 Teams should be assigned to a board
  - board shall load 0-9 on the top and side
  - users can click on a cell and confirm a bet on that cell
  - When the board is closed, the total prize shall be awarded to whichever player is on the correct cell

3. Integrate the API
  - Use get to receive data from the API
  - load the time remaining and scores into the backend logic
    - time remaining for when board should be closed
    - score to determine winner

4. Wallet and Funds
  - Users shall have a wallet that can be loaded with Funds
  - funds can be used to bet and to purchase items from a Store

5. Create a store page
  - create a store page that has different prizes which can be purchased by a user
  - the purchase will subtract funds from the user wallet
