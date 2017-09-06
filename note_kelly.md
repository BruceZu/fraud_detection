### Fata
- Fraud:
False    13044
True      1293

### Data Investigation
- If 'num_payouts' == 0, 90% chance being fraud, but we don't include this in model because this is data leakage.
- If 'previous_payouts' is '[]', higher chance of being fraud.
  + If 'previous_payouts' is empty, 'num_payouts' == 0
  + Binary variable **'have_previous_payouts'** is created.
- 'show_map' col is not important because there's no significant relationship between 'show_map' and 'fraud'
- 'ticket_types' listed out different ticket types under single event. e.g An Eventbrite event can have 'early bird', 'vip', 'general' ticket types.
  + If we want to include t into model, we use len('ticket_types'). Non-fraud events have higher mean number of 'ticket_types' than fraud events, but most event only have 1-2 ticket types. I think this column can be ignored for now.
- **'user_age'**: should be included. 'fraud' events have smaller mean user age of 87.1523588554, non-fraud events have a mean user age of 402.683072677.
- 'user_created': not necessary, timestamp, if convert to datetime, all 1970-01-01.
- **'user_type'**: don't know the meaning of each type, but fraud events tend to have more user with user_type as 1.
- 'user_created': not useful
- 'venue_address': street address, not necessary.
- 'venue_state': should look at if the % of events that are fraud in a specific state,
  + dummified this column into 'highly_suspect_state' with value 0 or 1.
  + If venue_state in ['MT', 'Mt', 'AK', 'FL', 'NEW SOUTH WALES', 'Florida'] then we highly suspect.
- **'venue_country'**: 64% fraud transactions are happening outsite US, 60% non-fraud transactions are happening within US. Thus we tend to suspect an overseas transaction. create another column as 'within_US'
- **'name'**: If an event name consists of only CAPITAL LETTERS, there's higher chance it is a fraud.
  + A new feature **'cap_name'** is created.


### What if...
1. What if we consider unbalanced class?
