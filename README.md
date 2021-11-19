# Rust Code Raiding

A repository for generating .csv files helpful for code raiding in the video game Rust.

# Motivation

Code raiding is a unique approach to success in Rust - rather than building up your own base, just take over someone 
else's. In order to do that, you have to be prepared to spend a good few hours standing outside the door trying out 
four-digit key codes. But do we just guess randomly? No no no! Certain codes are far more common than others, and it 
pays off to start with those, and slowly work your way down to the less frequently used ones. 
[This list of four-digit codes](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/four-digit-pin-codes-sorted-by-frequency-withcount.csv) 
has been used by many a code raider to more efficiently finagle their way into a stranger's base.

But by far the more effective method at cutting down the required time is to invite some friends to help - the more the 
merrier! If the workload is divided up properly, this can cut your average `TTL` ("time-to-loot") down to a fraction of 
what you could achieve on your own. How does one divide up the workload properly, you ask? **Striping!**

Take, for instance, this example:<br>
Mark, John, and Bartholomew are trying to code raid a zerg base. They each put their sleeping bags down, ready 
themselves at separate doors, and take to the code list. With 10000 codes to work through, they agree that Mark will try
the first 3333 codes, John the second 3333, and Bartholomew the last 3334. After hours of intense code entry, the three 
have entered 1500 codes each, and are 45% done (4500/10000). But the zerg comes online, sees what has been happening, 
and AKs them! The zerg leader changes the door codes to be even more secure, perhaps setting different codes on 
each door. `mission-failed.wav`

What did Mark, John, and Bartholomew do wrong? They chunked the codes, when they should have striped. You see, Mark was 
the only one who started at the top of the list. John began a third of the way down the list, and Bartholomew two thirds
down the list. John and Bartholomew may have been trying their hardest, but they were working with codes less likely than 
Mark's from the very beginning. What they should have done is _all_ start with codes near the top of the list, like so:

| Mark | John | Bartholomew |
| ------ | ------ | ------ |
| Code 1 | Code 2 | Code 3 |
| Code 4 | Code 5 | Code 6 |
| Code 7 | Code 8 | Code 9 |
| ...    | ...    | ...    |

See how the codes are striped across the columns?

Instead of breaking up sections of the code list into chunks, which sacrifices likelihood the further down the list you 
start, striping the codes ensures that every team member starts with the likeliest codes possible, lowering your average
`TTL` even further. Depending on team size, this effect can be anywhere from 5% to 10% (see `average_tries.py`).

Following this strategy, Mark, John, and Bartholomew would have had a 7.6% better chance of guessing the base code and reaching
pog loot before the zerg came online.

# Breakdown

The script `team_generator.py` will generate striped .csv files for you, given a range of team sizes. If you would just
like a single file, enter the same team size twice. Pre-generated files for team sizes 2 - 100 can be found in the
`output` directory, and for team sizes 2 - 20 in this
[Google Sheets document](https://docs.google.com/spreadsheets/d/10VRfXBZ0gLTXefnJBM9CfOjDZZlOhkBDhS46A3SUcO0/edit?usp=sharing).

`probability_generator.py` generates the original code list with two additional columns for individual probability and
cumulative probability that the respective code will open any given door. This file can also be found in the `output`
directory, and in the above-linked Google Sheets document.

`average-tries.py` will calculate for any team size the average number of code attempts to unlock a door, using both
striping and chunking methodologies.
