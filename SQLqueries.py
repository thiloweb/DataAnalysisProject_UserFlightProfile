airportsbycountry_query = \
    'SELECT \
        ap.AirportLocation, \
        ap.CountryReference, \
        co.CountryName \
    FROM Airports AS ap \
        JOIN Countries AS co ON ap.CountryReference = co.CountryID;'

all_airlines_query = \
    'SELECT \
        al.AirlineName \
    FROM Flights AS fl \
        JOIN Airports AS ap1 ON fl.DepartureIataCode = ap1.AirportID \
        JOIN Airports AS ap2 ON fl.ArrivalIataCode = ap2.AirportID \
        JOIN Airlines AS al ON fl.AirlineReference = al.AirlineID \
        JOIN ContEurAm AS ac1 ON ap1.CountryReference = ac1.CountryID \
        JOIN ContEurAm AS ac2 ON ap2.CountryReference = ac2.CountryID \
    WHERE ap1.CountryReference = ac1.CountryID AND ap2.CountryReference = ac2.CountryID'

facts_total_query = \
    'SELECT \
        COUNT(fl.FlightID), \
        SUM(fl.FlightDistance), \
        SUM(fl.FlightTimeMinutes) \
    FROM Flights AS fl \
        JOIN Airports AS ap1 ON fl.DepartureIataCode = ap1.AirportID \
        JOIN Airports AS ap2 ON fl.ArrivalIataCode = ap2.AirportID \
        JOIN ContEurAm AS ac1 ON ap1.CountryReference = ac1.CountryID \
        JOIN ContEurAm AS ac2 ON ap2.CountryReference = ac2.CountryID \
    WHERE ap1.CountryReference = ac1.CountryID AND ap2.CountryReference = ac2.CountryID;'

facts_total_national_query = \
    'SELECT \
        COUNT(fl.FlightID), \
        SUM(fl.FlightDistance), \
        SUM(fl.FlightTimeMinutes) \
    FROM Flights AS fl \
        JOIN Airports AS ap1 ON fl.DepartureIataCode = ap1.AirportID \
        JOIN Airports AS ap2 ON fl.ArrivalIataCode = ap2.AirportID \
        JOIN AllCont AS ac1 ON ap1.CountryReference = ac1.CountryID \
        JOIN AllCont AS ac2 ON ap2.CountryReference = ac2.CountryID \
    WHERE ac1.CountryID = ac2.CountryID; '

facts_total_europe_query = \
    'SELECT \
        COUNT(fl.FlightID), \
        SUM(fl.FlightDistance), \
        SUM(fl.FlightTimeMinutes) \
    FROM Flights AS fl \
        JOIN Airports AS ap1 ON fl.DepartureIataCode = ap1.AirportID \
        JOIN Airports AS ap2 ON fl.ArrivalIataCode = ap2.AirportID \
        JOIN AllCont AS ac1 ON ap1.CountryReference = ac1.CountryID \
        JOIN AllCont AS ac2 ON ap2.CountryReference = ac2.CountryID \
    WHERE ac1.ContinentName = "Europe" AND ac2.ContinentName = "Europe"; '

facts_total_americas_query = \
    'SELECT \
        COUNT(fl.FlightID), \
        SUM(fl.FlightDistance), \
        SUM(fl.FlightTimeMinutes) \
    FROM Flights AS fl \
        JOIN Airports AS ap1 ON fl.DepartureIataCode = ap1.AirportID \
        JOIN Airports AS ap2 ON fl.ArrivalIataCode = ap2.AirportID \
        JOIN AllCont AS ac1 ON ap1.CountryReference = ac1.CountryID \
        JOIN AllCont AS ac2 ON ap2.CountryReference = ac2.CountryID \
    WHERE (ac1.ContinentName = "Central America / Caribbean" OR ac1.ContinentName = "North America" OR ac1.ContinentName = "South America") AND (ac2.ContinentName = "Central America / Caribbean" OR ac2.ContinentName = "North America" OR ac2.ContinentName = "South America"); '

facts_total_transatlantic_query = \
    'SELECT \
        COUNT(fl.FlightID), \
        SUM(fl.FlightDistance), \
        SUM(fl.FlightTimeMinutes) \
    FROM Flights AS fl \
        JOIN Airports AS ap1 ON fl.DepartureIataCode = ap1.AirportID \
        JOIN Airports AS ap2 ON fl.ArrivalIataCode = ap2.AirportID \
        JOIN AllCont AS ac1 ON ap1.CountryReference = ac1.CountryID \
        JOIN AllCont AS ac2 ON ap2.CountryReference = ac2.CountryID \
    WHERE (ac1.ContinentName = "Europe" AND (ac2.ContinentName = "Central America / Caribbean" OR ac2.ContinentName = "North America" OR ac2.ContinentName = "South America")) OR ((ac1.ContinentName = "Central America / Caribbean" OR ac1.ContinentName = "North America" OR ac1.ContinentName = "South America") AND ac2.ContinentName = "Europe"); '


queries = [
    {"AllAirports":airportsbycountry_query},
    {"AllAirlines":all_airlines_query},
    {"FactsTotal":facts_total_query},
    {"FactsTotalNational":facts_total_national_query},
    {"FactsTotalEurope":facts_total_europe_query},
    {"FactsTotalAmerica":facts_total_americas_query},
    {"FactsTotalTransatlantic":facts_total_transatlantic_query},
]
