# Vibe-Server

Dating suggestions app backend, built with the django rest framework and using a postgres database.

## Usage

- `cd Vibe`
- run `docker-compose up`
- navigate to http://localhost:8000/


## PostgreSQL Schema

<img src="db_schema.png" width="700">

## API endpoints

| Route name   | Path                                            | Method        | Purpose                            |
| ------------ | ----------------------------------------------- | ------------- | ---------------------------------- |
| create       | `/users/register`                               | `POST`        | Register a new account             |
| update       | `/users/login`                                  | `POST`        | Login to an account                |
| show/create  | `/places/restaurants`                           | `GET/POST`    | get all or create new              |
| detail       | `/places/restaurants/:id`                       | `All methods` | Detail view, specific restaurant   |
| show         | `/places/restaurants/reviews/:id`               | `GET`         | Show reviews for restaurant        |
| show/create  | `/places/restaurant-reviews`                    | `GET/POST`    | get all or create new              |
| detail       | `/places/restaurant-reviews/:id`                | `All methods` | Detail view, specific review       |
| show/create  | `/places/events`                                | `GET/POST`    | get all or create new              |
| detail       | `/places/events/:id`                            | `All methods` | Detail view, specific event        |
| show/create  | `/places/event-reviews`                         | `GET/POST`    | get all or create new              |
| detail       | `/places/event-reviews/:id`                     | `All methods` | Detail view, specific review       |
| show         | `/places/events/reviews/:id`                    | `GET`         | Show reviews for event             |
| show         | `/apis/restaurant-search/:query`                | `GET`         | Find restaurants in area           |
| show         | `/apis/restaurant-search/website/:place_id`     | `GET`         | Find website given place_id        |
| show         | `/apis/event-search/:query`                     | `GET`         | Show all events in area            |
| show         | `/apis/event-search/:query/:eventcode`          | `GET`         | events in area for given code      |


## POST methods body properties

| Path                                      |  Body Properties                                                            |
| ----------------------------------------- | --------------------------------------------------------------------------- |
| `/users/register`                         | username, password, password_confirmation                                   |
| `/users/login`                            | username, password                                                          |
| `/places/restaurants`                     | name, url, location, username                                               |
| `/places/restaurant-reviews`              | message, restaurant_id, username, rating                                    |
| `/places/events`                          | name, event_type, url, location, username, event_date, start_date, end_date |
| `/places/event-reviews`                   | message, restaurant_id, username, rating                                    |

## Wednesday to do

- [ ] Finish search resukts page
- [ ] Pad out the landing page
- [ ] Pad out the account page
- [ ] Create endpoint to be used to get 5 top places
- [ ] Work on functionality to save and add reviews to a location
- [ ] Work out how do show reviews when someone searches, or just have reviews on recent recommendations page..?

