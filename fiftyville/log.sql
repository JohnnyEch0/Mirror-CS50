-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Check the Crime Scene reports for matching Reports
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street' AND month = 7 AND day = 28;

-- all 3 witnesses mention the bakery
-- Time: 10:15am
-- also there was a littering

-- read the bakeries sec logs at the given hour, sort by time
SELECT activity, license_plate, hour, minute FROM bakery_security_logs WHERE
    month = 7 AND day = 28 AND year = 2023 AND hour = 10 ORDER BY hour;

-- rerun with .output results.txt bc i cant copy from the terminal


-- read the police interviews and select the ones concerning our theft
SELECT name, transcript FROM interviews WHERE
    month = 7 AND day = 28 AND year = 2023;

-- switch to .output stdout


-- Eugene: I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery,
-- I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.

SELECT account_number, transaction_type, amount FROM atm_transactions WHERE
    month = 7 AND day = 28 AND year = 2023 AND atm_location = 'Leggett Street';

-- Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--      In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--      The thief then asked the person on the other end of the phone to purchase the flight ticket.

-- get possible calls
SELECT caller, receiver FROM phone_calls WHERE
    month = 7 AND day = 28 AND year = 2023 AND duration < 60;

-- now we have:
    -- possible License plate of the Thief
    -- possible ATM-Number of the Thief
    -- possible phone numbers of the Thief and the Complice

-- get fiftyvilles airport ID's
SELECT * FROM airports WHERE
    city = "Fiftyville";

-- get the earliest flight on 29th from fiftyville airport (id = 8)
SELECT id, hour, minute, destination_airport_id FROM flights WHERE
    month = 7 AND day = 29 AND year = 2023 AND origin_airport_id = 8;

-- its flight nr 36 to aiport (id 4)
SELECT * FROM airports WHERE
    id = 4;

-- get passenger data?
SELECT passport_number FROM passengers
    WHERE flight_id = 36;

-- now we have:
    -- possible License plate of the Thief
    -- possible ATM-Number of the Thief
    -- possible phone numbers of the Thief and the Complice
    -- possible passport_numbers
-- what we can do:
    -- search the bank accounts with atm data

-- get possible Thiefs from people via passport numbers from the flight
    -- also filter out phone numbers from outgoing call at the bakery
    -- also filter out license plates from bakery sec logs
SELECT * FROM people WHERE
    passport_number IN (
        SELECT passport_number FROM passengers
            WHERE flight_id = 36
    )
    AND phone_number IN (
        SELECT caller FROM phone_calls WHERE
            month = 7 AND day = 28 AND year = 2023 AND duration < 60
    )
    AND license_plate IN (
        SELECT license_plate FROM bakery_security_logs WHERE
            month = 7 AND day = 28 AND year = 2023 AND hour = 10 AND minute > 15
    );

-- this gives us 4 options, we need to dig deeper
-- lets check the bank accounts with possible account_numbers


SELECT  * FROM people JOIN bank_accounts
ON people.id = bank_accounts.person_id WHERE
    account_number IN (
        SELECT account_number FROM atm_transactions WHERE
            month = 7 AND day = 28 AND year = 2023 AND atm_location = 'Leggett Street'
    );

-- only matches with last search are valid
    -- Only Bruce and Taylor are left


-- One of them had a call with the buyer of the flight

-- get atm_transactions for possible complice
    -- we can get the phone calls receiver's account number IN
        -- Select account_number from bank_accounts WHERE person_id IN
            -- SELECT id from people WHERE phone Number IN
                -- SELECT receiver FROM phone_calls WHERE caller IN
                    -- SELECT phone_number FROM people WHERE
                        -- previous 2 querries
-- maybe this is stupid, as u dont need to withdraw cash for buying a flight

SELECT * FROM atm_transactions WHERE account_number IN (
    SELECT account_number FROM bank_accounts WHERE person_id IN (
        SELECT id from people WHERE phone_number IN (
            SELECT receiver FROM phone_calls
            WHERE caller IN (
                SELECT phone_number FROM people JOIN bank_accounts
                    ON people.id = bank_accounts.person_id
                    WHERE

                    passport_number IN (
                        SELECT passport_number FROM passengers
                            WHERE flight_id = 36
                    )

                    AND phone_number IN (
                        SELECT caller FROM phone_calls WHERE
                            month = 7 AND day = 28 AND year = 2023 AND duration < 60
                    )

                    AND license_plate IN (
                        SELECT license_plate FROM bakery_security_logs WHERE
                            month = 7 AND day = 28 AND year = 2023 AND hour = 10 AND minute > 15
                    )
                    AND account_number IN (
                    SELECT account_number FROM atm_transactions WHERE
                        month = 7 AND day = 28 AND year = 2023 AND atm_location = 'Leggett Street'
                    )
            )
        )
    )
)
AND month = 7 AND day = 28 AND year = 2023;

-- lets try and look if the account number withdrawing 100


-- lets look if something is odd with the passport numbers
SELECT * FROM people WHERE passport_number IN (
                        SELECT passport_number FROM passengers
                            WHERE flight_id = 36
                    );
